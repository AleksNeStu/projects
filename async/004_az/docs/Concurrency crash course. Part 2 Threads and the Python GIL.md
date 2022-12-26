---
source: https://alexandra-zaharia.github.io/posts/concurrency-crash-course-part-2/ \
created: 2022-12-26T12:50:03 (UTC +01:00) \
tags: [] \
author: Alexandra Zaharia
---
# Concurrency crash course. Part 2: Threads and the Python GIL | Alexandra Zaharia
---
This is a multi-part post:

-   [Part 1](https://alexandra-zaharia.github.io/posts/concurrency-crash-course-part-1/) establishes terminology (tasks, threads and processes and how they relate to concurrency and parallelism) and gives an overview of challenges faced in concurrent programming.
-   Part 2 (this article) shows what can go wrong when using threads without synchronization and explains the role and effects of the Global Interpreter Lock (GIL) in Python.
-   Part 3 (TODO) explains some common thread synchronization primitives, accompanied by Python examples.
-   Part 4 (TODO) explains some common process synchronization primitives (inter-process communication mechanisms), accompanied by Python examples.
-   Part 5 (TODO) tackles parallel algorithm design and performance evaluation.

## Threads

Remember from our [last](https://alexandra-zaharia.github.io/posts/concurrency-crash-course-part-1/) post that threads are the smallest set of instructions that can be managed by the scheduler. Unlike processes, multiple threads of a program share the same **address space** and are capable of accessing the same **data**.

Each thread has its own program counter and registers. The program counter is a special register that tracks the instruction that is currently being executed (or the next instruction to be executed). When the scheduler switches between two threads running on a single CPU, a **context switch** takes place in which the state of the registers of the thread being _switched from_ are stored and the registers of the thread being _switched to_ are restored.

Here’s an inspirational quote from [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/) (Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau, chapter 26, _Concurrency and threads_) to get us started:

> Computers are hard enough to understand without concurrency. Unfortunately, with concurrency, it simply gets worse. Much worse.

In Python, we can create and manage threads using the [`threading`](https://docs.python.org/3/library/threading.html) module. In the following example we create and start two threads that run the method `my_task()` (which essentially does nothing of interest beside sleep for a given amount of time):

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 </pre></td><td><pre><span>import</span> <span>threading</span> <span>import</span> <span>time</span>   <span>def</span> <span>my_task</span><span>(</span><span>x</span><span>,</span> <span>y</span><span>):</span>     <span>print</span><span>(</span><span>'{} got x={}, y={}'</span><span>.</span><span>format</span><span>(</span><span>threading</span><span>.</span><span>current_thread</span><span>().</span><span>getName</span><span>(),</span> <span>x</span><span>,</span> <span>y</span><span>))</span>     <span>time</span><span>.</span><span>sleep</span><span>(</span><span>x</span> <span>+</span> <span>y</span><span>)</span>     <span>print</span><span>(</span><span>'{} finished after {:.2f} seconds'</span><span>.</span><span>format</span><span>(</span>         <span>threading</span><span>.</span><span>current_thread</span><span>().</span><span>getName</span><span>(),</span> <span>x</span> <span>+</span> <span>y</span><span>))</span>   <span>def</span> <span>main</span><span>():</span>     <span>thr1</span> <span>=</span> <span>threading</span><span>.</span><span>Thread</span><span>(</span><span>target</span><span>=</span><span>my_task</span><span>,</span> <span>name</span><span>=</span><span>'Thread 1'</span><span>,</span> <span>args</span><span>=</span><span>(</span><span>1</span><span>,</span> <span>2</span><span>,))</span>     <span>thr2</span> <span>=</span> <span>threading</span><span>.</span><span>Thread</span><span>(</span><span>target</span><span>=</span><span>my_task</span><span>,</span> <span>name</span><span>=</span><span>'Thread 2'</span><span>,</span> <span>args</span><span>=</span><span>(.</span><span>1</span><span>,</span> <span>.</span><span>2</span><span>,))</span>      <span>thr1</span><span>.</span><span>start</span><span>()</span>     <span>thr2</span><span>.</span><span>start</span><span>()</span>      <span>thr1</span><span>.</span><span>join</span><span>()</span>     <span>thr2</span><span>.</span><span>join</span><span>()</span>      <span>print</span><span>(</span><span>'Main thread finished'</span><span>)</span>   <span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>     <span>main</span><span>()</span> </pre></td></tr></tbody></table>`

In `main()`, we create the threads, then actually `start()` them, and finally `join()` them. _Joining_ a thread means to wait until it terminates. Unsurprisingly, here is the output of the above program:

`<table><tbody><tr><td><pre>1 2 3 4 5 </pre></td><td><pre>Thread 1 got x=1, y=2 Thread 2 got x=0.1, y=0.2 Thread 2 finished after 0.30 seconds Thread 1 finished after 3.00 seconds Main thread finished </pre></td></tr></tbody></table>`

## Why do we need synchronization?

_But everything works fine. Why do we need synchronization?_ Glad you’ve asked! Concurrency can be tricky. Remember that we have discussed some common concurrency pitfalls in [Part 1](https://alexandra-zaharia.github.io/posts/concurrency-crash-course-part-1/) of this series. It might have all seemed a bit abstract, so let us now look at an example where things don’t go according to plan. Suppose we have two threads and each one increments a global counter:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 </pre></td><td><pre><span>import</span> <span>threading</span>   <span>counter</span> <span>=</span> <span>0</span>  <span>def</span> <span>increment</span><span>(</span><span>n</span><span>):</span>     <span>global</span> <span>counter</span>     <span>for</span> <span>_</span> <span>in</span> <span>range</span><span>(</span><span>n</span><span>):</span>         <span>counter</span> <span>+=</span> <span>1</span>   <span>def</span> <span>main</span><span>():</span>     <span>thr1</span> <span>=</span> <span>threading</span><span>.</span><span>Thread</span><span>(</span><span>target</span><span>=</span><span>increment</span><span>,</span> <span>args</span><span>=</span><span>(</span><span>500000</span><span>,))</span>     <span>thr2</span> <span>=</span> <span>threading</span><span>.</span><span>Thread</span><span>(</span><span>target</span><span>=</span><span>increment</span><span>,</span> <span>args</span><span>=</span><span>(</span><span>500000</span><span>,))</span>      <span>thr1</span><span>.</span><span>start</span><span>()</span>     <span>thr2</span><span>.</span><span>start</span><span>()</span>      <span>thr1</span><span>.</span><span>join</span><span>()</span>     <span>thr2</span><span>.</span><span>join</span><span>()</span>      <span>print</span><span>(</span><span>f</span><span>'counter = </span><span>{</span><span>counter</span><span>}</span><span>'</span><span>)</span>   <span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>     <span>main</span><span>()</span> </pre></td></tr></tbody></table>`

The result is not what we expect. Even worse, it is inconsistent from run to run:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 </pre></td><td><pre>$ python 02_b_sum_without_synchronization.py counter = 793916 $ python 02_b_sum_without_synchronization.py counter = 1000000 $ python 02_b_sum_without_synchronization.py counter = 697999 $ python 02_b_sum_without_synchronization.py counter = 872864 </pre></td></tr></tbody></table>`

Let us understand what just happened:

[![Thread synchronization](https://alexandra-zaharia.github.io/assets/img/posts/thread_sync.png)](https://alexandra-zaharia.github.io/assets/img/posts/thread_sync.png)

### Critical section

A **critical section** refers to code that can result in a race condition when executed by multiple threads, because a a shared resource is involved.

In our example, both threads attempt to modify the global `counter` variable by incrementing it. In other words, both threads access a shared resource in a critical section in write mode, without using thread synchronization.

### Race condition

A **race condition** occurs when several threads execute a critical section without synchronization mechanisms in place. Depending on the order in which the threads execute the critical section, the result of the program is different.

In our example, both threads attempt to increment the global counter; as we’ve seen, not all increments are successful.

### Atomic operations

A series of actions is **atomic** if the actions are “all or nothing”, meaning they either _all_ occur, or _none_ occur. (You might be familiar with database _transactions_: by definition, they are atomic.)

In our example, increments do not succeed because the increment operation itself is not atomic. Suppose the `counter` contains the value 3. In order to increment it, the first step is to read its current value (3) into a temporary location. The second step is to increment this temporary value (it now becomes 4). The final step is to copy the new value from the temporary location (4) into the counter. However, if a second thread accesses the counter concurrently, it can change its value while the “lagging” thread uses the stale value from the temporary location.

This problem can be solved by rendering critical sections atomic through thread synchronization primitives such as _locks_ or _semaphores_. What we mean by that is that we allow one thread to execute the critical section while the others are denied access to the critical section until the thread that is in control releases it. We will look into thread synchronization primitives in detail in the next post.

## Thread communication

Apart from thread synchronization, concurrency can also involve thread communication. While thread synchronization and thread communication are related, in thread communication the focus is shifted to threads _waiting_ on other threads to finish before executing. In the next part of this series we will see how **condition variables** help us achieve thread communication.

## The Global Interpreter Lock (GIL) in Python

Now that we’ve seen why thread synchronization is necessary, we cannot simply jump right in without first mentioning the dreaded Python GIL, short for the [Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock).

### Python interpreters

Before properly defining the GIL, we need to take a step back and talk about… Python. In the strictest sense, Python is “just” a programming language _specification_. Python _interpreters_ are different implementations of the Python language specification. The most popular implementation is CPython (written in C), commonly called `python` by language abuse. Alternative Python implementations [exist](https://www.python.org/download/alternatives/).

The image below summarizes the relationship between language _specification_ and _implementation_:

[![Specification vs implementations](https://alexandra-zaharia.github.io/assets/img/posts/python_implementations.png)](https://alexandra-zaharia.github.io/assets/img/posts/python_implementations.png)

### CPython and the GIL

When we run a Python script using the `python` (i.e. CPython) interpreter, the source code is first _compiled_ into byte code, a low-level platform-independent representation that is executed by the Python virtual machine. You have probably already seen the `.pyc` files in the `__pycache__` directory – that is byte code. The Python virtual machine is not a separate component, but rather a loop running inside the Python interpreter. It simply executes the generated byte code line by line.

The GIL is a mechanism that limits Python (remember we’re talking about the CPython interpreter) to execute only one thread at a time. Below you can see a [GIL visualisation](http://dabeaz.com/GIL/gilvis/) showing the main thread and 4 additional threads running on a single CPU; the green blocks represent the time when threads are executing:

[![Four threads running on 1 CPU](https://alexandra-zaharia.github.io/assets/img/posts/conc_4thr_1cpu.png)](https://alexandra-zaharia.github.io/assets/img/posts/conc_4thr_1cpu.png)

### The reason behind the GIL

Why would Python designers restrict the CPython interpreter to only be able to execute a single thread at a time? When CPython was being developed, its [garbage collector](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)) was designed to use reference counting. This means that an object is released from memory when its reference count reaches zero.

We can get the reference count of an object in memory using `sys.getrefcount()`. In the example below, notice that when we assign the object to a new variable, the reference count increases:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 </pre></td><td><pre><span>In</span> <span>[</span><span>46</span><span>]:</span> <span>import</span> <span>sys</span>  <span>In</span> <span>[</span><span>47</span><span>]:</span> <span>z</span> <span>=</span> <span>"this is a string variable"</span>  <span>In</span> <span>[</span><span>48</span><span>]:</span> <span>sys</span><span>.</span><span>getrefcount</span><span>(</span><span>z</span><span>)</span> <span>Out</span><span>[</span><span>48</span><span>]:</span> <span>8</span>  <span>In</span> <span>[</span><span>49</span><span>]:</span> <span>z2</span> <span>=</span> <span>z</span>  <span>In</span> <span>[</span><span>50</span><span>]:</span> <span>sys</span><span>.</span><span>getrefcount</span><span>(</span><span>z</span><span>)</span> <span>Out</span><span>[</span><span>50</span><span>]:</span> <span>9</span> </pre></td></tr></tbody></table>`

If several threads are running, race conditions may modify the reference count if it is not protected by a simple synchronization mechanism called “lock” (that we will be looking into in the next post). The solution was to impose a global lock providing exclusive access to the Python interpreter. This way, the Python interpreter executes byte code using the GIL, which in turn means that only one thread is active at any given time. The advantage is that reference counting becomes thread-safe. The drawback is that the remaining threads from the byte code must wait for the GIL to become available.

You can also check out the article over at [RealPython](https://realpython.com/python-gil/) for more context.

### Effects of the GIL

The dreaded effect of the Python GIL that we’ve hinted at earlier is that, no matter how many CPUs there are, since only a single thread can run at a time, the extra CPU cores remain unused. In other words, I/O-bound problems can be sped up through multithreading, albeit the threads run one at a time, in interleaved fashion. However, because the GIL prevents threads from running in parallel, no speed-up is possible unfortunately for CPU-bound problems (which, as we’ve seen in [Part 1](https://alexandra-zaharia.github.io/posts/concurrency-crash-course-part-1/), require parallel execution).

Do not despair though: multiple CPUs _can_ be used in Python if we create _processes_ instead of threads. Since every process comes with its own interpreter, the GIL issue is effectively side-stepped. We will be looking into processes in a later article in this series.

## Conclusion

In this post we’ve seen:

-   How to launch separate threads in Python
-   That launching threads without synchronizing them is rarely a good idea. We need to:
    -   control how threads access a critical section
    -   have threads wait on other threads to finish
-   How the Python GIL (Global Interpreter Lock) complicates things further by only allowing a single thread to be active at a time

The next post in this series will present thread synchronization primitives and show how they can be used in Python. In subsequent posts we will also be discussing processes, asynchronous programming, as well as parallel algorithm design and evaluation.

## Resources

-   [`threading`](https://docs.python.org/3/library/threading.html) (Python documentation)
-   [Garbage collection](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)) (Wikipedia)
-   [Python GIL visualizations](http://dabeaz.com/GIL/gilvis/) (David Beazley)
-   [Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock) (Python wiki)
-   [Global Interpreter Lock](https://realpython.com/python-gil/) (Abhinav Ajitsaria @ RealPython, 2018)
-   [Operating systems: Three easy pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) (Arpaci-Dusseau & Arpaci-Dusseau)
-   [Python concurrency for senior engineering interviews](https://www.educative.io/courses/python-concurrency-for-senior-engineering-interviews/) (educative.io course)
