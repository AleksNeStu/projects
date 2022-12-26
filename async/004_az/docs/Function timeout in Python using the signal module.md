---
source: https://alexandra-zaharia.github.io/posts/function-timeout-in-python-signal/ \
created: 2022-12-26T19:39:06 (UTC +01:00) \
tags: [] \
author: Alexandra Zaharia
---
# Function timeout in Python using the signal module | Alexandra Zaharia
---
## The problem

Sometimes you may want to impose a timeout on a Python function. Why would you want to do such a thing? Let’s say you’re computing something but you know there are some hopeless scenarios where the computation just takes too long, and you’d be OK to just skip them and go on with the rest of the workflow.

For an illustration, the figure below shows several tasks. Those that take longer than the specified timeout should be aborted (orange) and the remaining tasks that take a reasonable amount of time should be executed normally (green).

[![A timeout is a cutoff for the duration of a task](https://alexandra-zaharia.github.io/assets/img/posts/function_timeout.png)](https://alexandra-zaharia.github.io/assets/img/posts/function_timeout.png)

There are several ways in which setting a timeout on a function may be achieved such that the execution continues past the timed-out method. We will be examining two solutions here:

-   in this post we will be using [`signal`](https://docs.python.org/3/library/signal.html) module;
-   in the [next post](https://alexandra-zaharia.github.io/posts/function-timeout-in-python-multiprocessing/) we will be using the [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html) module.

## Solution using the signal module

### What are signals?

[Signals](https://en.wikipedia.org/wiki/Signal_(IPC)) are a form of [inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication) that only applies to [POSIX](https://en.wikipedia.org/wiki/POSIX)\-compliant operating systems. Note that Microsoft Windows is _not_ POSIX-compliant, so this solution cannot be used when running Python on Windows.

Signals can be regarded as software interrupts sent from the kernel to a process in order to inform it that a special event took place. The process receiving the signal can choose to handle it in a specific way (if the program was written with this intention, that is). Otherwise, signals are handled in a default manner specified by the default signal handlers. For example, when you press Ctrl + C in your Linux terminal to stop a running program, you are in fact sending it the SIGINT signal. The default handler for SIGINT is to stop process execution.

Check out this [article](https://stackabuse.com/handling-unix-signals-in-python/) for more information on handling UNIX signals in Python.

### Using signals to set a timeout

Suppose we have a method `do_stuff()` that can sometimes be very time-consuming. We’ll be keeping this very simple:

`<table><tbody><tr><td><pre>1 2 3 4 </pre></td><td><pre><span>import</span> <span>time</span>  <span>def</span> <span>do_stuff</span><span>(</span><span>n</span><span>):</span>     <span>time</span><span>.</span><span>sleep</span><span>(</span><span>n</span><span>)</span> </pre></td></tr></tbody></table>`

Let’s say we only want to run `do_stuff()` to completion if it finishes in less than 6 seconds. With the `signal` module, this can be achieved if we set a timer (an “alarm”) for 6 seconds just before calling `do_stuff()`. If the timer runs out before the function completes, SIGALRM is sent to the process. We will therefore be using `signal.alarm(6)` to set a timer for 6 seconds before calling `do_stuff()`. Note that the argument to `signal.alarm()` must be an integer. Let’s check what happens:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 </pre></td><td><pre><span>import</span> <span>signal</span> <span>import</span> <span>time</span>   <span>def</span> <span>do_stuff</span><span>(</span><span>n</span><span>):</span>     <span>time</span><span>.</span><span>sleep</span><span>(</span><span>n</span><span>)</span>     <span>print</span><span>(</span><span>'slept for {}s'</span><span>.</span><span>format</span><span>(</span><span>n</span><span>))</span>   <span>def</span> <span>main</span><span>():</span>     <span>signal</span><span>.</span><span>alarm</span><span>(</span><span>6</span><span>)</span>     <span>do_stuff</span><span>(</span><span>2</span><span>)</span>     <span>do_stuff</span><span>(</span><span>5</span><span>)</span>     <span>do_stuff</span><span>(</span><span>6</span><span>)</span>   <span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>     <span>main</span><span>()</span> </pre></td></tr></tbody></table>`

Here is the output:

`<table><tbody><tr><td><pre>1 2 3 4 5 </pre></td><td><pre>$ python timeout_signal.py  slept for 2s Alarm clock $ echo $? 142 </pre></td></tr></tbody></table>`

What happened? Well, the timer was set to 6 seconds and it finally ran out, one second before the second call to `do_stuff()` would have normally finished. The process exits with code 142 (SIGALRM). Let us change the `main()` function to reset the alarm after each call to `do_stuff()`:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 </pre></td><td><pre><span>def</span> <span>main</span><span>():</span>     <span>signal</span><span>.</span><span>alarm</span><span>(</span><span>6</span><span>)</span>     <span>do_stuff</span><span>(</span><span>2</span><span>)</span>     <span>signal</span><span>.</span><span>alarm</span><span>(</span><span>0</span><span>)</span>      <span>signal</span><span>.</span><span>alarm</span><span>(</span><span>6</span><span>)</span>     <span>do_stuff</span><span>(</span><span>5</span><span>)</span>     <span>signal</span><span>.</span><span>alarm</span><span>(</span><span>0</span><span>)</span>      <span>signal</span><span>.</span><span>alarm</span><span>(</span><span>6</span><span>)</span>     <span>do_stuff</span><span>(</span><span>6</span><span>)</span>     <span>signal</span><span>.</span><span>alarm</span><span>(</span><span>0</span><span>)</span> </pre></td></tr></tbody></table>`

Note that `signal.alarm(delay)` arms a timer for `delay` seconds. This means that if `do_stuff()` takes exactly `delay` seconds to complete, SIGALRM gets transmitted nonetheless.

We now obtain:

`<table><tbody><tr><td><pre>1 2 3 </pre></td><td><pre>slept for 2s slept for 5s Alarm clock </pre></td></tr></tbody></table>`

Next, we will define a handler for SIGALRM. A **handler** is a function that “handles a signal” in the specific way we instruct it to behave. User-defined handlers are used to override the default signal handlers. For example, suppose you want your program to ask the user to confirm her desire to quit the program when she presses Ctrl + C in the terminal. In this case you’d need a SIGINT handler that only exits upon confirmation. Note that signal handlers must respect a fixed prototype. To quote from the [Python documentation](https://docs.python.org/3/library/signal.html):

> The handler is called with two arguments: the signal number and the current stack frame (…).

Even if a a signal handler does not use these two arguments, they must be present in the handler’s prototype (and no other arguments may be passed). Here is our simple handler; it just throws a `TimeoutError`:

`<table><tbody><tr><td><pre>1 2 </pre></td><td><pre><span>def</span> <span>handle_timeout</span><span>(</span><span>sig</span><span>,</span> <span>frame</span><span>):</span>     <span>raise</span> <span>TimeoutError</span><span>(</span><span>'took too long'</span><span>)</span> </pre></td></tr></tbody></table>`

This handler only makes sense if it is registered for SIGALRM. Registering `handle_timeout()` for SIGALRM should be added to the `main()` function of the script above. Here is how to do it:

`<table><tbody><tr><td><pre>1 </pre></td><td><pre><span>signal</span><span>.</span><span>signal</span><span>(</span><span>signal</span><span>.</span><span>SIGALRM</span><span>,</span> <span>handle_timeout</span><span>)</span> </pre></td></tr></tbody></table>`

By re-running our script, we can see that it now stops with a `TimeoutError`:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 </pre></td><td><pre>slept for 2s slept for 5s Traceback (most recent call last):   File "timeout_signal.py", line 31, in &lt;module&gt;     main()   File "timeout_signal.py", line 26, in main     do_stuff(7)   File "timeout_signal.py", line 10, in do_stuff     time.sleep(n)   File "timeout_signal.py", line 6, in handle_timeout     raise TimeoutError('took too long') TimeoutError: took too long </pre></td></tr></tbody></table>`

This is great, we have an exception now – and exceptions are something we can deal with in Python.

### Making execution continue past the timeout

Next, let’s handle the `TimeoutError`. We will change our script such that it loops indefinitely and at each iteration through the loop it attempts to `do_stuff()` for a random number of seconds between 1 and 10. If `do_stuff()` is called with 6 seconds or more, then SIGALRM is sent and handled by raising a `TimeoutError`. We catch that `TimeoutError` and continue execution until hitting Ctrl + C. As an added bonus, we also include a handler for SIGINT (Ctrl + C).

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 </pre></td><td><pre><span>import</span> <span>sys</span> <span>import</span> <span>random</span> <span>import</span> <span>signal</span> <span>import</span> <span>time</span>   <span>def</span> <span>handle_sigint</span><span>(</span><span>sig</span><span>,</span> <span>frame</span><span>):</span>     <span>print</span><span>(</span><span>'SIGINT received, terminating.'</span><span>)</span>     <span>sys</span><span>.</span><span>exit</span><span>()</span>   <span>def</span> <span>handle_timeout</span><span>(</span><span>sig</span><span>,</span> <span>frame</span><span>):</span>     <span>raise</span> <span>TimeoutError</span><span>(</span><span>'took too long'</span><span>)</span>   <span>def</span> <span>do_stuff</span><span>(</span><span>n</span><span>):</span>     <span>time</span><span>.</span><span>sleep</span><span>(</span><span>n</span><span>)</span>   <span>def</span> <span>main</span><span>():</span>     <span>signal</span><span>.</span><span>signal</span><span>(</span><span>signal</span><span>.</span><span>SIGINT</span><span>,</span> <span>handle_sigint</span><span>)</span>     <span>signal</span><span>.</span><span>signal</span><span>(</span><span>signal</span><span>.</span><span>SIGALRM</span><span>,</span> <span>handle_timeout</span><span>)</span>      <span>max_duration</span> <span>=</span> <span>5</span>          <span>while</span> <span>True</span><span>:</span>         <span>try</span><span>:</span>             <span>duration</span> <span>=</span> <span>random</span><span>.</span><span>choice</span><span>([</span><span>x</span> <span>for</span> <span>x</span> <span>in</span> <span>range</span><span>(</span><span>1</span><span>,</span> <span>11</span><span>)])</span>             <span>print</span><span>(</span><span>'duration = {}: '</span><span>.</span><span>format</span><span>(</span><span>duration</span><span>),</span> <span>end</span><span>=</span><span>''</span><span>,</span> <span>flush</span><span>=</span><span>True</span><span>)</span>             <span>signal</span><span>.</span><span>alarm</span><span>(</span><span>max_duration</span> <span>+</span> <span>1</span><span>)</span>             <span>do_stuff</span><span>(</span><span>duration</span><span>)</span>             <span>signal</span><span>.</span><span>alarm</span><span>(</span><span>0</span><span>)</span>         <span>except</span> <span>TimeoutError</span> <span>as</span> <span>exc</span><span>:</span>             <span>print</span><span>(</span><span>'{}: {}'</span><span>.</span><span>format</span><span>(</span><span>exc</span><span>.</span><span>__class__</span><span>.</span><span>__name__</span><span>,</span> <span>exc</span><span>))</span>         <span>else</span><span>:</span>             <span>print</span><span>(</span><span>'slept for {}s'</span><span>.</span><span>format</span><span>(</span><span>duration</span><span>))</span>   <span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>     <span>main</span><span>()</span> </pre></td></tr></tbody></table>`

So how does the execution continue past the first timeout? As we’ve seen above, we installed a handler for SIGALRM (lines 12-13 and 22) that raises a `TimeoutError`. Exception handling is performed in the `main()` function inside an infinite loop (lines 26-36). If `do_stuff()` succeeds, the script displays a message informing the user for how long the function ran (lines 35-36). If the `TimeoutError` is caught, it is simply displayed and the script continues.

Here is how the output might look like:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 </pre></td><td><pre>duration = 3: slept for 3s duration = 1: slept for 1s duration = 10: TimeoutError: took too long duration = 7: TimeoutError: took too long duration = 5: slept for 5s duration = 9: TimeoutError: took too long duration = 2: slept for 2s duration = 5: slept for 5s duration = 1: slept for 1s duration = 6: TimeoutError: took too long duration = 2: slept for 2s duration = 10: ^CSIGINT received, terminating. </pre></td></tr></tbody></table>`

### Drawbacks

Well, _it works_ but there are two problems with this solution:

1.  As mentioned in the introduction to signals, this mechanism is only present on UNIX-like systems. If the script needs to run in a classic Windows environment, the `signal` module is not suitable.
2.  A SIGALRM can arrive at any time; however, its handler may only be ran between **atomic** instructions. By definition, atomic instructions cannot be interrupted. So if the timer runs out during such an operation, even though SIGALRM is sent, it won’t be handled until that long computation you’ve been trying to abort finally completes. Typically, when using external libraries implemented in pure C for performing long computations, the handling of SIGALRM may be delayed.

## Conclusion

In this post we’ve seen a simple solution involving UNIX signals that may be used in some situations to set a timeout on a Python function. However, this solution is less than ideal for two reasons: the operating system must be POSIX-compliant and it can only work between atomic operations. In the [next post](https://alexandra-zaharia.github.io/posts/function-timeout-in-python-multiprocessing/) we will examine a better solution using the `multiprocessing` module.

## Further reading

-   [Signals](https://en.wikipedia.org/wiki/Signal_(IPC)) (Wikipedia)
-   [`signal`](https://docs.python.org/3/library/signal.html) (Python documentation)
-   [Handling UNIX signals in Python](https://stackabuse.com/handling-unix-signals-in-python/) (Frank Hofmann on stackabuse)
