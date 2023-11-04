---
source: https://alexandra-zaharia.github.io/posts/fix-python-logger-printing-same-entry-multiple-times/ \
created: 2022-12-26T22:31:00 (UTC +01:00) \
tags: [] \
author: Alexandra Zaharia
---
# How to fix Python logger printing the same entry multiple times | Alexandra Zaharia
---
The [previous post](https://alexandra-zaharia.github.io/posts/make-your-own-custom-color-formatter-with-python-logging/) explained how to get a simple colored formatter for your custom logger using the Python [`logging`](https://docs.python.org/3/library/logging.html) module. This one explains why a logger may print the same record multiple times, and how to fix this.

## The scenario

Let us suppose you already have the logger from the [previous post](https://alexandra-zaharia.github.io/posts/make-your-own-custom-color-formatter-with-python-logging/) up and running. Now, the idea is to share it across several modules and/or classes.

Suppose your logger is defined in `logger.py` as follows:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 </pre></td><td><pre><span>import</span> <span>logging</span> <span>import</span> <span>datetime</span>   <span>def</span> <span>get_logger</span><span>():</span>     <span># Create custom logger logging all five levels  </span>    <span>logger</span> <span>=</span> <span>logging</span><span>.</span><span>getLogger</span><span>(</span><span>__name__</span><span>)</span>     <span>logger</span><span>.</span><span>setLevel</span><span>(</span><span>logging</span><span>.</span><span>DEBUG</span><span>)</span>      <span># Define format for logs </span>    <span>fmt</span> <span>=</span> <span>'%(asctime)s | %(levelname)8s | %(filename)s:%(lineno)2d | %(message)s'</span>      <span># Create stdout handler for logging to the console (logs all five levels) </span>    <span>stdout_handler</span> <span>=</span> <span>logging</span><span>.</span><span>StreamHandler</span><span>()</span>     <span>stdout_handler</span><span>.</span><span>setLevel</span><span>(</span><span>logging</span><span>.</span><span>DEBUG</span><span>)</span>     <span>stdout_handler</span><span>.</span><span>setFormatter</span><span>(</span><span>CustomFormatter</span><span>(</span><span>fmt</span><span>))</span>      <span># Create file handler for logging to a file (logs all five levels) </span>    <span>today</span> <span>=</span> <span>datetime</span><span>.</span><span>date</span><span>.</span><span>today</span><span>()</span>     <span>file_handler</span> <span>=</span> <span>logging</span><span>.</span><span>FileHandler</span><span>(</span><span>'my_app_{}.log'</span><span>.</span><span>format</span><span>(</span><span>today</span><span>.</span><span>strftime</span><span>(</span><span>'%Y_%m_%d'</span><span>)))</span>     <span>file_handler</span><span>.</span><span>setLevel</span><span>(</span><span>logging</span><span>.</span><span>DEBUG</span><span>)</span>     <span>file_handler</span><span>.</span><span>setFormatter</span><span>(</span><span>logging</span><span>.</span><span>Formatter</span><span>(</span><span>fmt</span><span>))</span>      <span># Add both handlers to the logger </span>    <span>logger</span><span>.</span><span>addHandler</span><span>(</span><span>stdout_handler</span><span>)</span>     <span>logger</span><span>.</span><span>addHandler</span><span>(</span><span>file_handler</span><span>)</span>      <span>return</span> <span>logger</span> </pre></td></tr></tbody></table>`

Suppose you also have a file called `module.py` where you define three classes, `A`, `B`, and `C`, each one using the same logger:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 </pre></td><td><pre><span>from</span> <span>logger</span> <span>import</span> <span>get_logger</span>   <span>class</span> <span>A</span><span>:</span>     <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>):</span>         <span>self</span><span>.</span><span>logger</span> <span>=</span> <span>get_logger</span><span>()</span>         <span>self</span><span>.</span><span>logger</span><span>.</span><span>warning</span><span>(</span><span>'This is from class A'</span><span>)</span>   <span>class</span> <span>B</span><span>:</span>     <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>):</span>         <span>self</span><span>.</span><span>logger</span> <span>=</span> <span>get_logger</span><span>()</span>         <span>self</span><span>.</span><span>logger</span><span>.</span><span>warning</span><span>(</span><span>'This is from class B'</span><span>)</span>   <span>class</span> <span>C</span><span>:</span>     <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>):</span>         <span>self</span><span>.</span><span>logger</span> <span>=</span> <span>get_logger</span><span>()</span>         <span>self</span><span>.</span><span>logger</span><span>.</span><span>warning</span><span>(</span><span>'This is from class C'</span><span>)</span>   <span>def</span> <span>main</span><span>():</span>     <span>a</span> <span>=</span> <span>A</span><span>()</span>     <span>b</span> <span>=</span> <span>B</span><span>()</span>     <span>c</span> <span>=</span> <span>C</span><span>()</span>       <span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>     <span>main</span><span>()</span> </pre></td></tr></tbody></table>`

## The problem

The problem is immediately apparent when running `module.py`:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 </pre></td><td><pre>2021-06-24 00:38:02,055 |  WARNING | module.py: 7 | This is from class A 2021-06-24 00:38:02,055 |  WARNING | module.py:13 | This is from class B 2021-06-24 00:38:02,055 |  WARNING | module.py:13 | This is from class B 2021-06-24 00:38:02,055 |  WARNING | module.py:19 | This is from class C 2021-06-24 00:38:02,055 |  WARNING | module.py:19 | This is from class C 2021-06-24 00:38:02,055 |  WARNING | module.py:19 | This is from class C </pre></td></tr></tbody></table>`

Instead of one log record for each of the three classes, we get one for class `A` as expected, but two for class `B` and three for class `C`. ![:confounded:](https://github.githubassets.com/images/icons/emoji/unicode/1f616.png ":confounded:")

## Why does this happen?

The [`logging`](https://docs.python.org/3/library/logging.html) documentation ensures us that `logging.getLogger()` returns the same logger instance each time this function is called:

> All calls to this function with a given name return the same logger instance. This means that logger instances never need to be passed between different parts of an application.

So why does this happen? The answer is that although we get the same _logger_, each time we call our `get_logger()` function from `logger.py` we are actually attaching distinct _handlers_ to it.

## Two solutions

Don’t worry, there are two fixes for this problem. In both cases we get only one printed line per record, as expected:

`<table><tbody><tr><td><pre>1 2 3 </pre></td><td><pre>2021-06-24 00:51:40,057 |  WARNING | module.py: 7 | This is from class A 2021-06-24 00:51:40,057 |  WARNING | module.py:13 | This is from class B 2021-06-24 00:51:40,057 |  WARNING | module.py:19 | This is from class C </pre></td></tr></tbody></table>`

### Import the same logger every time

We can simply create the logger in `logger.py` and import it directly in our module, without ever having to call `get_logger()`. Here is how `logger.py` changes:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 </pre></td><td><pre><span>import</span> <span>logging</span> <span>import</span> <span>datetime</span>   <span>def</span> <span>get_logger</span><span>():</span>     <span>...</span>     <span>return</span> <span>logger</span>   <span>logger</span> <span>=</span> <span>get_logger</span><span>()</span> </pre></td></tr></tbody></table>`

Everything is just as before, except that we create the logger in `logger.py` (it’s a global variable, yes, I know).

And here is how `module.py` changes:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 </pre></td><td><pre><span>from</span> <span>logger</span> <span>import</span> <span>logger</span>   <span>class</span> <span>A</span><span>:</span>     <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>):</span>         <span>self</span><span>.</span><span>logger</span> <span>=</span> <span>logger</span>         <span>self</span><span>.</span><span>logger</span><span>.</span><span>warning</span><span>(</span><span>'This is from class A'</span><span>)</span>   <span>class</span> <span>B</span><span>:</span>     <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>):</span>         <span>self</span><span>.</span><span>logger</span> <span>=</span> <span>logger</span>         <span>self</span><span>.</span><span>logger</span><span>.</span><span>warning</span><span>(</span><span>'This is from class B'</span><span>)</span>   <span>class</span> <span>C</span><span>:</span>     <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>):</span>         <span>self</span><span>.</span><span>logger</span> <span>=</span> <span>logger</span>         <span>self</span><span>.</span><span>logger</span><span>.</span><span>warning</span><span>(</span><span>'This is from class C'</span><span>)</span>   <span>def</span> <span>main</span><span>():</span>     <span>a</span> <span>=</span> <span>A</span><span>()</span>     <span>b</span> <span>=</span> <span>B</span><span>()</span>     <span>c</span> <span>=</span> <span>C</span><span>()</span>   <span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>     <span>main</span><span>()</span> </pre></td></tr></tbody></table>`

We just use the same variable in each of the three classes and the problem goes away, since no unnecessary handlers are created. However, this solution is not ideal since it involves (potentially many) modifications, and furthermore we can’t be sure that in two months from now we’ll still remember that we were not supposed to call `get_logger()` directly.

### Check if handlers are present

The best solution is to check whether any handlers are already attached before adding them to the logger. This fix only involves changing `logging.py`:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 </pre></td><td><pre><span>import</span> <span>logging</span> <span>import</span> <span>datetime</span>   <span>def</span> <span>get_logger</span><span>():</span>     <span>...</span>       <span>if</span> <span>not</span> <span>logger</span><span>.</span><span>hasHandlers</span><span>():</span>         <span>logger</span><span>.</span><span>addHandler</span><span>(</span><span>stdout_handler</span><span>)</span>         <span>logger</span><span>.</span><span>addHandler</span><span>(</span><span>file_handler</span><span>)</span>      <span>return</span> <span>logger</span>  </pre></td></tr></tbody></table>`

Problem fixed. Happy logging!

## Further reading

-   [`logging`](https://docs.python.org/3/library/logging.html) (Python documentation)
-   [Python `logging` tutorial at Real Python](https://realpython.com/python-logging/)
