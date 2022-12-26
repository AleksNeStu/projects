---
source: https://alexandra-zaharia.github.io/posts/function-timeout-in-python-multiprocessing/ \
created: 2022-12-26T19:43:21 (UTC +01:00) \
tags: [] \
author: Alexandra Zaharia
---
# Function timeout in Python using the multiprocessing module | Alexandra Zaharia
---
## The problem

Sometimes you may want to impose a timeout on a Python function. Why would you want to do such a thing? Let’s say you’re computing something but you know there are some hopeless scenarios where the computation just takes too long, and you’d be OK to just skip them and go on with the rest of the workflow.

For an illustration, the figure below shows several tasks. Those that take longer than the specified timeout should be aborted (orange) and the remaining tasks that take a reasonable amount of time should be executed normally (green).

[![A timeout is a cutoff for the duration of a task](https://alexandra-zaharia.github.io/assets/img/posts/function_timeout.png)](https://alexandra-zaharia.github.io/assets/img/posts/function_timeout.png)

There are several ways in which setting a timeout on a function may be achieved such that the execution continues past the timed-out method. We will be examining two solutions here:

-   in the [previous post](https://alexandra-zaharia.github.io/posts/function-timeout-in-python-signal/) we have used the [`signal`](https://docs.python.org/3/library/signal.html) module;
-   in this post we will be using the [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html) module.

## Solution using the multiprocessing module

Just like in the [previous post](https://alexandra-zaharia.github.io/posts/function-timeout-in-python-signal/), suppose we have a method that can be very time-consuming:

`<table><tbody><tr><td><pre>1 2 3 4 5 </pre></td><td><pre><span>import</span> <span>time</span>  <span>def</span> <span>do_stuff</span><span>(</span><span>n</span><span>):</span>     <span>time</span><span>.</span><span>sleep</span><span>(</span><span>n</span><span>)</span>     <span>print</span><span>(</span><span>'slept for {}s'</span><span>.</span><span>format</span><span>(</span><span>n</span><span>))</span> </pre></td></tr></tbody></table>`

For the purpose of this example, we want to let this function `do_stuff()` run until it either completes or hits the 5-second mark, whichever event comes first. Actually, in the [previous post](https://alexandra-zaharia.github.io/posts/function-timeout-in-python-signal/), we let it run just below 6 seconds, because the argument to `signal.alarm()` is necessarily an integer. If that argument was 5, `do_stuff()` would not have been allowed to run for 5 seconds. Apart from the shortcomings of the `signal`\-based solution, the `multiprocessing` module also solves this nagging issue; we can now use a non-integer timeout, for example 5.01 seconds.

Although `multiprocessing` is the package that comes to mind when attempting to parallelize processes, its basic role is to simply spawn processes, as its name implies. (Processes spawned with `multiprocessing` _may_, but do not _have to_, be parallel.) We can set a timeout on the processes that are spawned, which is exactly what we are looking for here.

The script below runs indefinitely. At each passage through the infinite loop, it randomly selects a duration between 1 and 10 seconds. It then spawns a new `multiprocessing.Process` that executes the time-consuming `do_stuff()` function for the random duration. If `do_stuff()` doesn’t finish in 5 seconds (actually, 5.01 seconds), the process terminates:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 </pre></td><td><pre><span>import</span> <span>multiprocessing</span> <span>as</span> <span>mp</span> <span>import</span> <span>random</span> <span>import</span> <span>time</span>   <span>def</span> <span>do_stuff</span><span>(</span><span>n</span><span>):</span>     <span>time</span><span>.</span><span>sleep</span><span>(</span><span>n</span><span>)</span>     <span>print</span><span>(</span><span>'slept for {}s'</span><span>.</span><span>format</span><span>(</span><span>n</span><span>))</span>   <span>def</span> <span>main</span><span>():</span>     <span>max_duration</span> <span>=</span> <span>5</span>      <span>while</span> <span>True</span><span>:</span>         <span>duration</span> <span>=</span> <span>random</span><span>.</span><span>choice</span><span>([</span><span>x</span> <span>for</span> <span>x</span> <span>in</span> <span>range</span><span>(</span><span>1</span><span>,</span> <span>11</span><span>)])</span>         <span>print</span><span>(</span><span>'duration = {}: '</span><span>.</span><span>format</span><span>(</span><span>duration</span><span>),</span> <span>end</span><span>=</span><span>''</span><span>,</span> <span>flush</span><span>=</span><span>True</span><span>)</span>          <span>process</span> <span>=</span> <span>mp</span><span>.</span><span>Process</span><span>(</span><span>target</span><span>=</span><span>do_stuff</span><span>,</span> <span>args</span><span>=</span><span>(</span><span>duration</span><span>,))</span>         <span>process</span><span>.</span><span>start</span><span>()</span>         <span>process</span><span>.</span><span>join</span><span>(</span><span>timeout</span><span>=</span><span>max_duration</span> <span>+</span> <span>0.01</span><span>)</span>          <span>if</span> <span>process</span><span>.</span><span>is_alive</span><span>():</span>             <span>process</span><span>.</span><span>terminate</span><span>()</span>             <span>process</span><span>.</span><span>join</span><span>()</span>             <span>print</span><span>(</span><span>'took too long'</span><span>)</span>   <span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>     <span>main</span><span>()</span> </pre></td></tr></tbody></table>`

A `multiprocessing.Process` is spawned at line 18 with `do_stuff()` as its target and the random `duration` as argument for `do_stuff()`. Next, we start the process at line 19, and then we “join” it (meaning we wait for it to finish) at line 20, but with a twist: it is here that we actually specify the timeout. In other words, we wait for it to finish for the specified timeout. In lines 22-25 we check whether the process actually finished, in which case `is_alive()` returns false. If it is still running, we terminate the process and display a message on STDOUT.

Here is the output of this script:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 </pre></td><td><pre>duration = 7: took too long duration = 9: took too long duration = 2: slept for 2s duration = 5: slept for 5s duration = 2: slept for 2s duration = 6: took too long duration = 5: slept for 5s duration = 3: slept for 3s duration = 7: ^C </pre></td></tr></tbody></table>`

## Notes

1.  Simply spawning processes with the `multiprocessing` module does not mean we have parallelism. In order to do this we’d need to add tasks to a `multiprocessing.Pool`. [This](https://alexandra-zaharia.github.io/posts/run-python-script-as-subprocess-with-multiprocessing/) article or [this](https://alexandra-zaharia.github.io/posts/multiprocessing-in-python-with-shared-resources/) one show examples of pools.
2.  Care must be taken when using `terminate()` to stop a process. Here is what the Python documentation has to say about it:
    
    > **Warning:** If this method is used when the associated process is using a pipe or queue then the pipe or queue is liable to become corrupted and may become unusable by other process \[_sic_\]. Similarly, if the process has acquired a lock or semaphore etc. then terminating it is liable to cause other processes to deadlock.
    

## Conclusion

In this post we’ve seen another solution for setting a timeout on a function in Python, this time using the `multiprocessing` module. It is easy to implement and does not suffer from any of the drawbacks of the `signal`\-based solution described in the [previous post](https://alexandra-zaharia.github.io/posts/function-timeout-in-python-signal/).

## Further reading

-   [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html) (Python documentation)
-   [Parallel processing in Python](https://stackabuse.com/parallel-processing-in-python/) (Frank Hofmann on stackabuse)
-   [`multiprocessing` – Manage processes like threads](https://pymotw.com/3/multiprocessing/index.html) (Doug Hellmann on Python Module of the Week)
