---
source: https://alexandra-zaharia.github.io/posts/how-to-stop-a-python-thread-cleanly/ \
created: 2022-12-26T19:35:46 (UTC +01:00) \
tags: [] \
author: Alexandra Zaharia
---
# How to stop a Python thread cleanly | Alexandra Zaharia
---
Suppose a Python thread needs to be stopped cleanly (it might need to perform cleanup).

For illustration, we will take a very simple program in with a single “worker” thread that displays a message when it is done. The message is a placeholder for real cleanup, and the thread itself sleeps for a given number of iterations (as a placeholder for significant work). In our example, we want to stop the thread through a keyboard interrupt (Ctrl + C).

## By default, the thread is not stopped cleanly

In this first version, the program can be stopped by hitting Ctrl + C, but the thread keeps running. Here is the program:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 </pre></td><td><pre><span>import</span> <span>threading</span> <span>import</span> <span>time</span>   <span>def</span> <span>do_some_work</span><span>(</span><span>n_iter</span><span>):</span>     <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>n_iter</span><span>):</span>         <span>print</span><span>(</span><span>f</span><span>'iteration </span><span>{</span><span>i</span> <span>+</span> <span>1</span><span>}</span><span>/</span><span>{</span><span>n_iter</span><span>}</span><span>'</span><span>)</span>         <span>time</span><span>.</span><span>sleep</span><span>(</span><span>0.5</span><span>)</span>     <span>print</span><span>(</span><span>'Thread done'</span><span>)</span>   <span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>     <span>n_iter</span> <span>=</span> <span>10</span>     <span>thread</span> <span>=</span> <span>threading</span><span>.</span><span>Thread</span><span>(</span><span>target</span><span>=</span><span>do_some_work</span><span>,</span> <span>args</span><span>=</span><span>(</span><span>n_iter</span><span>,))</span>     <span>thread</span><span>.</span><span>start</span><span>()</span>     <span>thread</span><span>.</span><span>join</span><span>()</span>     <span>print</span><span>(</span><span>'Program done'</span><span>)</span> </pre></td></tr></tbody></table>`

Here is what happens when stopping it via a keyboard interrupt (`...` denotes output that was snipped for readability purposes):

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 </pre></td><td><pre>iteration 1/10 iteration 2/10 ^CTraceback (most recent call last):   ... KeyboardInterrupt iteration 3/10 iteration 4/10 ^CException ignored in: &lt;module 'threading' from '/home/alex/miniconda3/lib/python3.7/threading.py'&gt;   ... KeyboardInterrupt </pre></td></tr></tbody></table>`

The first Ctrl + C stops the main program, but not the thread. The second time, the thread is stopped as well.

## Using a daemon thread is not a good idea

The Python [`threading`](https://docs.python.org/3/library/threading.html) documentation explains that a thread may be started as a daemon, meaning that “the entire Python program exits when only daemon threads are left”. The main program itself is not a daemon thread.

While this approach has the merit of effectively stopping the thread, it does not allow to exit it cleanly. From the Python documentation:

> **Note:** Daemon threads are abruptly stopped at shutdown. Their resources (such as open files, database transactions, etc.) may not be released properly. If you want your threads to stop gracefully, make them non-daemonic and use a suitable signalling mechanism such as an `Event`.

## A clean thread exit using events and signals

Following on the previous note, a threading [`Event`](https://docs.python.org/3/library/threading.html#threading.Event) is a simple object that can be set or cleared. It can be used to signal to the thread that it needs perform its cleanup and then stop.

The idea is to use such an event here (let us call it a _stop event_). Initially not set, the stop event becomes set when a keyboard interrupt is received. The worker thread then breaks out from the loop if the stop event is set and performs its cleanup.

Creating the stop event is straightforward (it can take any name):

`<table><tbody><tr><td><pre>1 </pre></td><td><pre><span>stop_event</span> <span>=</span> <span>threading</span><span>.</span><span>Event</span><span>()</span> </pre></td></tr></tbody></table>`

The worker thread checks whether the stop event is set:

`<table><tbody><tr><td><pre>1 2 </pre></td><td><pre><span>if</span> <span>stop_event</span><span>.</span><span>is_set</span><span>():</span>     <span>break</span> </pre></td></tr></tbody></table>`

The stop event needs to be set when a keyboard interrupt is intercepted. This is done by registering the SIGINT [signal](https://en.wikipedia.org/wiki/Signal_(IPC)) with a handler function. The registration is done in the main program:

`<table><tbody><tr><td><pre>1 </pre></td><td><pre><span>signal</span><span>.</span><span>signal</span><span>(</span><span>signal</span><span>.</span><span>SIGINT</span><span>,</span> <span>handle_kb_interrupt</span><span>)</span> </pre></td></tr></tbody></table>`

The handler function `handle_kb_interrupt` must have two arguments, the signal and the frame, even though the second argument is not used:

`<table><tbody><tr><td><pre>1 2 </pre></td><td><pre><span>def</span> <span>handle_kb_interrupt</span><span>(</span><span>sig</span><span>,</span> <span>frame</span><span>):</span>     <span>stop_event</span><span>.</span><span>set</span><span>()</span> </pre></td></tr></tbody></table>`

Here is the full program:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 </pre></td><td><pre><span>import</span> <span>signal</span> <span>import</span> <span>threading</span> <span>import</span> <span>time</span>   <span>def</span> <span>do_some_work</span><span>(</span><span>n_iter</span><span>):</span>     <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>n_iter</span><span>):</span>         <span>if</span> <span>stop_event</span><span>.</span><span>is_set</span><span>():</span>             <span>break</span>         <span>print</span><span>(</span><span>f</span><span>'iteration </span><span>{</span><span>i</span> <span>+</span> <span>1</span><span>}</span><span>/</span><span>{</span><span>n_iter</span><span>}</span><span>'</span><span>)</span>         <span>time</span><span>.</span><span>sleep</span><span>(</span><span>0.5</span><span>)</span>     <span>print</span><span>(</span><span>'Thread done'</span><span>)</span>   <span>def</span> <span>handle_kb_interrupt</span><span>(</span><span>sig</span><span>,</span> <span>frame</span><span>):</span>     <span>stop_event</span><span>.</span><span>set</span><span>()</span>   <span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>     <span>stop_event</span> <span>=</span> <span>threading</span><span>.</span><span>Event</span><span>()</span>     <span>signal</span><span>.</span><span>signal</span><span>(</span><span>signal</span><span>.</span><span>SIGINT</span><span>,</span> <span>handle_kb_interrupt</span><span>)</span>     <span>n_iter</span> <span>=</span> <span>10</span>     <span>thread</span> <span>=</span> <span>threading</span><span>.</span><span>Thread</span><span>(</span><span>target</span><span>=</span><span>do_some_work</span><span>,</span> <span>args</span><span>=</span><span>(</span><span>n_iter</span><span>,))</span>     <span>thread</span><span>.</span><span>start</span><span>()</span>     <span>thread</span><span>.</span><span>join</span><span>()</span>     <span>print</span><span>(</span><span>'Program done'</span><span>)</span>  </pre></td></tr></tbody></table>`

Here is the output when hitting Ctrl + C in the new version of the program:

`<table><tbody><tr><td><pre>1 2 3 4 5 </pre></td><td><pre>iteration 1/10 iteration 2/10 iteration 3/10 ^CThread done Program done </pre></td></tr></tbody></table>`

Notice that when the thread is stopped it now finally gets to the `print('Thread done')` line (a placeholder for an actual cleanup task). Moreover, the main program also gets to the `print('Program done')` line. Clean exit from a thread can therefore be achieved using a threading event and a signal handler.

## Further reading

-   [`threading`](https://docs.python.org/3/library/threading.html) (Python documentation)
-   [`signal`](https://docs.python.org/3/library/signal.html) (Python documentation)
-   [Signals](https://en.wikipedia.org/wiki/Signal_(IPC)) (Wikipedia)
