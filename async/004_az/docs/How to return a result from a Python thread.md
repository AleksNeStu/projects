---
source: https://alexandra-zaharia.github.io/posts/how-to-return-a-result-from-a-python-thread/ \
created: 2022-12-26T19:17:08 (UTC +01:00) \
tags: [] \
author: Alexandra Zaharia
---
# How to return a result from a Python thread | Alexandra Zaharia
---
## The problem

Suppose you have a Python thread that runs your target function.

-   Simple scenario: That target function returns a result that you want to retrieve.
-   A more advanced scenario: You want to retrieve the result of the target function if the thread does not time out.

There are several ways to retrieve a value from a Python thread. You can use [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html), [`multiprocessing.pool.ThreadPool`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.dummy) or just [`threading`](https://docs.python.org/3/library/threading.html) with [`Queue`](https://docs.python.org/3/library/queue.html).

This post proposes an alternative solution that does not require any other package aside from `threading`.

## The solution

If you don’t want to use anything else beside the `threading` module, the solution is simple:

1.  Extend the `threading.Thread` class and add a `result` member to your new class. Make sure to take into account positional and keyword arguments in the constructor.
2.  Override the base class’s `run()` method: in addition to running the target function as expected (with its args and kwargs intact), it has to store the target’s result in the new member `result`.
3.  Override the base class’s `join()` method: with args and kwargs intact, simply `join()` as in the base class but also return the result.
4.  Then when you instantiate your new thread class, intercept the result returned by `join()`.

Note the stress placed upon preserving the target’s positional and keyword arguments: this ensures that you can also `join()` the thread with a timeout, as you would a with a `threading.Thread` instance.

The following section illustrates these steps.

## Implementation: ReturnValueThread class

Below, the class `ReturnValueThread` extends `threading.Thread` (lines 4-19).

1.  In the constructor, we declare a `result` member that will store the result returned by the target function (lines 6-8).
2.  We override the `run()` method by storing the result of the target in the `result` member (lines 10-16).
3.  We override the `join()` method such as to return the `result` member (lines 18-20).

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 </pre></td><td><pre><span>import</span> <span>threading</span> <span>import</span> <span>sys</span>   <span>class</span> <span>ReturnValueThread</span><span>(</span><span>threading</span><span>.</span><span>Thread</span><span>):</span>     <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>*</span><span>args</span><span>,</span> <span>**</span><span>kwargs</span><span>):</span>         <span>super</span><span>().</span><span>__init__</span><span>(</span><span>*</span><span>args</span><span>,</span> <span>**</span><span>kwargs</span><span>)</span>         <span>self</span><span>.</span><span>result</span> <span>=</span> <span>None</span>      <span>def</span> <span>run</span><span>(</span><span>self</span><span>):</span>         <span>if</span> <span>self</span><span>.</span><span>_target</span> <span>is</span> <span>None</span><span>:</span>             <span>return</span>  <span># could alternatively raise an exception, depends on the use case </span>        <span>try</span><span>:</span>             <span>self</span><span>.</span><span>result</span> <span>=</span> <span>self</span><span>.</span><span>_target</span><span>(</span><span>*</span><span>self</span><span>.</span><span>_args</span><span>,</span> <span>**</span><span>self</span><span>.</span><span>_kwargs</span><span>)</span>         <span>except</span> <span>Exception</span> <span>as</span> <span>exc</span><span>:</span>             <span>print</span><span>(</span><span>f</span><span>'</span><span>{</span><span>type</span><span>(</span><span>exc</span><span>).</span><span>__name__</span><span>}</span><span>: </span><span>{</span><span>exc</span><span>}</span><span>'</span><span>,</span> <span>file</span><span>=</span><span>sys</span><span>.</span><span>stderr</span><span>)</span>  <span># properly handle the exception </span>     <span>def</span> <span>join</span><span>(</span><span>self</span><span>,</span> <span>*</span><span>args</span><span>,</span> <span>**</span><span>kwargs</span><span>):</span>         <span>super</span><span>().</span><span>join</span><span>(</span><span>*</span><span>args</span><span>,</span> <span>**</span><span>kwargs</span><span>)</span>         <span>return</span> <span>self</span><span>.</span><span>result</span> </pre></td></tr></tbody></table>`

## Usage example for ReturnValueThread

Here is how to use the `ReturnValueThread` class defined above. Imagine that the target functions both compute and return the square of the argument that gets passed to them:

-   `square()` returns the square of its argument instantly (lines 4-5);
-   `think_about_square()` returns the square of its argument after having… thought about it for a while (lines 8-10).

Why do we have two target functions in this example? Remember the scenarios mentioned at the beginning of this post:

1.  A simple scenario is to simply retrieve the value returned by the target function (lines 16-19);
2.  A more advanced scenario is to retrieve the value if the function finishes running before a specified timeout (lines 21-27).

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 </pre></td><td><pre><span>import</span> <span>time</span>   <span>def</span> <span>square</span><span>(</span><span>x</span><span>):</span>     <span>return</span> <span>x</span> <span>**</span> <span>2</span>   <span>def</span> <span>think_about_square</span><span>(</span><span>x</span><span>):</span>     <span>time</span><span>.</span><span>sleep</span><span>(</span><span>x</span><span>)</span>     <span>return</span> <span>square</span><span>(</span><span>x</span><span>)</span>   <span>def</span> <span>main</span><span>():</span>     <span>value</span> <span>=</span> <span>3</span>      <span>thread1</span> <span>=</span> <span>ReturnValueThread</span><span>(</span><span>target</span><span>=</span><span>square</span><span>,</span> <span>args</span><span>=</span><span>(</span><span>value</span><span>,))</span>     <span>thread1</span><span>.</span><span>start</span><span>()</span>     <span>result</span> <span>=</span> <span>thread1</span><span>.</span><span>join</span><span>()</span>     <span>print</span><span>(</span><span>f</span><span>'square(</span><span>{</span><span>value</span><span>}</span><span>) = </span><span>{</span><span>result</span><span>}</span><span>'</span><span>)</span>      <span>thread2</span> <span>=</span> <span>ReturnValueThread</span><span>(</span><span>target</span><span>=</span><span>think_about_square</span><span>,</span> <span>args</span><span>=</span><span>(</span><span>value</span><span>,))</span>     <span>thread2</span><span>.</span><span>start</span><span>()</span>     <span>result</span> <span>=</span> <span>thread2</span><span>.</span><span>join</span><span>(</span><span>timeout</span><span>=</span><span>1</span><span>)</span>     <span>if</span> <span>thread2</span><span>.</span><span>is_alive</span><span>():</span>         <span>print</span><span>(</span><span>'Timeout in think_about_square'</span><span>)</span>  <span># properly handle timeout </span>    <span>else</span><span>:</span>         <span>print</span><span>(</span><span>f</span><span>'think_about_square(</span><span>{</span><span>value</span><span>}</span><span>) = </span><span>{</span><span>result</span><span>}</span><span>'</span><span>)</span>   <span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>     <span>main</span><span>()</span> </pre></td></tr></tbody></table>`

`thread1` is the thread running `square()` (instant result, retrieved as expected). `thread2`, on the other hand, runs `think_about_square()`, and it just so happens that it does not finish within the allotted time. We test whether the thread finished at line 24 via `thread2.is_alive()`.

## Caveat

The more observant types have probably noticed that although `ReturnValueThread` returns the result of the target function, our `thread2` in the above example (the thread that times out) does not exit cleanly. In fact, it runs until the `sleep()` ends. In a [previous post](https://alexandra-zaharia.github.io/posts/how-to-stop-a-python-thread-cleanly/) we have seen how to exit a Python thread cleanly. Another solution is to use a process instead of a thread, but this comes with its own set of complications. The most notable difficulty is the fact that, unlike threads, processes run in separate memory spaces, which tends to complicate things since resources now have to be [shared](https://alexandra-zaharia.github.io/posts/multiprocessing-in-python-with-shared-resources/).

## Further reading

-   [How to exit a Python thread cleanly](https://alexandra-zaharia.github.io/posts/how-to-stop-a-python-thread-cleanly/) (using a threading event)
-   [Multiprocessing in Python with shared resources](https://alexandra-zaharia.github.io/posts/multiprocessing-in-python-with-shared-resources/)
-   [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html) (Python documentation)
-   [`multiprocessing.pool.ThreadPool`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.dummy) (Python documentation)
-   [`threading`](https://docs.python.org/3/library/threading.html) (Python documentation)
-   [`Queue`](https://docs.python.org/3/library/queue.html) (Python documentation)

This post is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) by the author.
