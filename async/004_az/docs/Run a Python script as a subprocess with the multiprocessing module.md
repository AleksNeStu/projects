---
source: https://alexandra-zaharia.github.io/posts/run-python-script-as-subprocess-with-multiprocessing/ \
created: 2022-12-26T20:04:39 (UTC +01:00) \
tags: [] \
author: Alexandra Zaharia
---
# Run a Python script as a subprocess with the multiprocessing module | Alexandra Zaharia
---
## The problem

Suppose you have a Python script `worker.py` performing some long computation. Also suppose you need to perform these computations several times for different input data. If all the computations are independent from each other, one way to speed them up is to use Python’s [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html) module.

This comes down to the difference between _sequential_ and _parallel_ execution. Suppose you have the tasks A, B, C and D, requiring 1, 2, 3 and 4 seconds, respectively, to complete. When ran sequentially, meaning one after the other, you’d need 10 seconds in order for all tasks to complete, whereas running them in parallel (if you have 4 available CPU cores) would take 4 seconds, give or take, because some overhead does exist.

[![sequential vs parallel execution](https://alexandra-zaharia.github.io/assets/img/posts/seq_vs_parallel.png)](https://alexandra-zaharia.github.io/assets/img/posts/seq_vs_parallel.png)

Before we continue, it is worth emphasizing that what is meant by _parallel execution_ is each task is handled by a separate CPU, and that these tasks are ran at the same time. So in the figure above, when tasks A, B, C and D are run in parallel, each of them is ran on a different CPU.

## The worker script

Let us see a very simple example for `worker.py`; remember that it performs long computations:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 </pre></td><td><pre><span>import</span> <span>sys</span> <span>import</span> <span>time</span>   <span>def</span> <span>do_work</span><span>(</span><span>n</span><span>):</span>     <span>time</span><span>.</span><span>sleep</span><span>(</span><span>n</span><span>)</span>     <span>print</span><span>(</span><span>'I just did some hard work for {}s!'</span><span>.</span><span>format</span><span>(</span><span>n</span><span>))</span>   <span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>     <span>if</span> <span>len</span><span>(</span><span>sys</span><span>.</span><span>argv</span><span>)</span> <span>!=</span> <span>2</span><span>:</span>       <span>print</span><span>(</span><span>'Please provide one integer argument'</span><span>,</span> <span>file</span><span>=</span><span>sys</span><span>.</span><span>stderr</span><span>)</span>       <span>exit</span><span>(</span><span>1</span><span>)</span>     <span>try</span><span>:</span>         <span>seconds</span> <span>=</span> <span>int</span><span>(</span><span>sys</span><span>.</span><span>argv</span><span>[</span><span>1</span><span>])</span>         <span>do_work</span><span>(</span><span>seconds</span><span>)</span>     <span>except</span> <span>Exception</span> <span>as</span> <span>e</span><span>:</span>         <span>print</span><span>(</span><span>e</span><span>)</span> </pre></td></tr></tbody></table>`

`worker.py` fails if it does not receive a command-line argument that can be converted to an integer. It then calls the `do_work()` method with the input argument converted to an integer. In turn, `do_work()` performs some hard work (sleeping for the specified number of seconds) and then outputs a message:

`<table><tbody><tr><td><pre>1 2 </pre></td><td><pre>$ python worker.py 2 I just did some hard work for 2s! </pre></td></tr></tbody></table>`

(Just in case you were wondering, if `do_work()` is called with a negative integer, then it is the `sleep()` function that complains about it.)

## The main script

Let us now see how to run `worker.py` from within another Python script. We will create a file `main.py` that creates four tasks. As shown in the figure above, the tasks take 1, 2, 3 and 4 seconds to finish, respectively. Each task consists in running `worker.py` with a different sleep length:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 </pre></td><td><pre><span>import</span> <span>subprocess</span> <span>import</span> <span>multiprocessing</span> <span>as</span> <span>mp</span> <span>from</span> <span>tqdm</span> <span>import</span> <span>tqdm</span>   <span>NUMBER_OF_TASKS</span> <span>=</span> <span>4</span> <span>progress_bar</span> <span>=</span> <span>tqdm</span><span>(</span><span>total</span><span>=</span><span>NUMBER_OF_TASKS</span><span>)</span>   <span>def</span> <span>work</span><span>(</span><span>sec_sleep</span><span>):</span>     <span>command</span> <span>=</span> <span>[</span><span>'python'</span><span>,</span> <span>'worker.py'</span><span>,</span> <span>sec_sleep</span><span>]</span>     <span>subprocess</span><span>.</span><span>call</span><span>(</span><span>command</span><span>)</span>   <span>def</span> <span>update_progress_bar</span><span>(</span><span>_</span><span>):</span>     <span>progress_bar</span><span>.</span><span>update</span><span>()</span>   <span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>     <span>pool</span> <span>=</span> <span>mp</span><span>.</span><span>Pool</span><span>(</span><span>NUMBER_OF_TASKS</span><span>)</span>      <span>for</span> <span>seconds</span> <span>in</span> <span>[</span><span>str</span><span>(</span><span>x</span><span>)</span> <span>for</span> <span>x</span> <span>in</span> <span>range</span><span>(</span><span>1</span><span>,</span> <span>NUMBER_OF_TASKS</span> <span>+</span> <span>1</span><span>)]:</span>         <span>pool</span><span>.</span><span>apply_async</span><span>(</span><span>work</span><span>,</span> <span>(</span><span>seconds</span><span>,),</span> <span>callback</span><span>=</span><span>update_progress_bar</span><span>)</span>      <span>pool</span><span>.</span><span>close</span><span>()</span>     <span>pool</span><span>.</span><span>join</span><span>()</span>  </pre></td></tr></tbody></table>`

The tasks are ran in parallel using `NUMBER_OF_TASKS` (4) processes in a `multiprocessing` pool (lines 20-26). When we refer to the tasks being ran in parallel, we mean that the `apply_async()` method is applied to every task (line 23). The first argument to `apply_async()` is the method to execute asynchronously (`work()`), the second one is the argument for `work()` (`seconds`), and the third one is a callback, our `update_progress_bar()` function.

The `work()` method (lines 10-12) calls our previous script `worker.py` with the specified number of seconds. This is done through the Python [`subprocess`](https://docs.python.org/3/library/subprocess.html) module.

As for [`tqdm`](https://tqdm.github.io/), it is a handy little package that displays a progress bar for the number of items in an iteration. It can be installed through `pip`, `conda` or `snap`.

## Parallelization in practice

Here is the output of our `main.py` script:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 </pre></td><td><pre>$ python main.py   0%|                                                                    | 0/4 [00:00&lt;?, ?it/s] I just did some hard work for 1s!  25%|███████████████                                             | 1/4 [00:01&lt;00:03,  1.02s/it] I just did some hard work for 2s!  50%|██████████████████████████████                              | 2/4 [00:02&lt;00:02,  1.02s/it] I just did some hard work for 3s!  75%|█████████████████████████████████████████████               | 3/4 [00:03&lt;00:01,  1.01s/it] I just did some hard work for 4s! 100%|████████████████████████████████████████████████████████████| 4/4 [00:04&lt;00:00,  1.03s/it] </pre></td></tr></tbody></table>`

As you can see, the four tasks finished in about 4 seconds, meaning that the execution of the `worker.py` script has successfully been parallelized.

The next post [Multiprocessing in Python with shared resources](https://alexandra-zaharia.github.io/posts/multiprocessing-in-python-with-shared-resources/) iterates on what we have just seen in order to show how we can parallelize external Python scripts that need to access the same shared resource.

## Further reading

-   [`subprocess`](https://docs.python.org/3/library/subprocess.html) (Python documentation)
-   [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html) (Python documentation)
-   [Parallel processing in Python](https://stackabuse.com/parallel-processing-in-python/) (Frank Hofmann on stackabuse)
-   [`multiprocessing` – Manage processes like threads](https://pymotw.com/3/multiprocessing/index.html) (Doug Hellmann on Python Module of the Week)
