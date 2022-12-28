---
source: https://alexandra-zaharia.github.io/posts/standalone-python-script-to-run-other-python-scripts/ \
created: 2022-12-28T19:53:49 (UTC +01:00) \
tags: [] \
author: Alexandra Zaharia
---
# Standalone Python script to run other Python scripts | Alexandra Zaharia
---
In the [previous post](https://alexandra-zaharia.github.io/posts/distribute-a-python-package-with-a-standalone-script-using-setuptools/) we’ve seen how to use [`setuptools`](https://setuptools.pypa.io/) to package a Python project along with a standalone executable that can be invoked on the command-line, system-wide (or rather _environment_\-wide).

Now, what if you need that standalone script to be a **runner**, sort of like a master script running other Python scripts that import modules from the newly installed package?

Although it seems straightforward, there might be some issues with getting the Python scripts to actually run, as my recent [Stack Overflow](https://stackoverflow.com/questions/69830933) experience has shown.

## What we want to obtain

Here is how a script using your package might look like:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 </pre></td><td><pre><span># my_script.py </span><span>from</span> <span>mypackage</span> <span>import</span> <span>capitalize</span>  <span>print</span><span>(</span><span>f</span><span>'Running </span><span>{</span><span>__file__</span><span>}</span><span>'</span><span>)</span> <span>print</span><span>(</span><span>capitalize</span><span>(</span><span>'my text'</span><span>))</span> <span>print</span><span>(</span><span>f</span><span>'Done running </span><span>{</span><span>__file__</span><span>}</span><span>'</span><span>)</span> </pre></td></tr></tbody></table>`

You would invoke your standalone script, let’s call it `runner`, as follows:

And you’d obtain:

`<table><tbody><tr><td><pre>1 2 3 4 5 </pre></td><td><pre>runner v1.0.0 started on 2021-11-04 00:11:26 Running my_script.py MY TEXT Done running my_script.py runner v1.0.0 finished on 2021-11-04 00:11:26 </pre></td></tr></tbody></table>`

## Making the necessary adjustments

We start off by editing `setup.py` to which we add a new console script entry point. There is no need to have the function pointed at by the entry point to reside in a different file than the `__main__.py` that we already have:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 </pre></td><td><pre><span>from</span> <span>setuptools</span> <span>import</span> <span>setup</span><span>,</span> <span>find_packages</span>  <span>setup</span><span>(</span>     <span>name</span><span>=</span><span>"mypackage"</span><span>,</span>     <span># [snip] </span>    <span>entry_points</span> <span>=</span> <span>{</span><span>'console_scripts'</span><span>:</span> <span>[</span>         <span>'capitalize = mypackage.__main__:main'</span><span>,</span>         <span>'runner = mypackage.__main__:runner'</span><span>,</span>  <span># this gets added </span>    <span>]},</span> <span>)</span> </pre></td></tr></tbody></table>`

The `__main__.py` file gets a new `runner()` function:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 </pre></td><td><pre><span>import</span> <span>argparse</span> <span>from</span> <span>datetime</span> <span>import</span> <span>datetime</span> <span>import</span> <span>sys</span>   <span>def</span> <span>now</span><span>():</span>     <span>return</span> <span>datetime</span><span>.</span><span>now</span><span>().</span><span>strftime</span><span>(</span><span>'%Y-%m-%d %H:%m:%S'</span><span>)</span>   <span>def</span> <span>runner</span><span>():</span>     <span>version</span> <span>=</span> <span>'1.0.0'</span>     <span>parser</span> <span>=</span> <span>argparse</span><span>.</span><span>ArgumentParser</span><span>(</span><span>prog</span><span>=</span><span>'runner'</span><span>)</span>     <span>parser</span><span>.</span><span>add_argument</span><span>(</span><span>'script'</span><span>,</span> <span>help</span><span>=</span><span>'Python script to run'</span><span>)</span>     <span>parser</span><span>.</span><span>add_argument</span><span>(</span><span>'-v'</span><span>,</span> <span>'--version'</span><span>,</span> <span>help</span><span>=</span><span>'display version'</span><span>,</span> <span>action</span><span>=</span><span>'version'</span><span>,</span>                         <span>version</span><span>=</span><span>f</span><span>'%(prog)s </span><span>{</span><span>version</span><span>}</span><span>'</span><span>)</span>     <span>args</span> <span>=</span> <span>parser</span><span>.</span><span>parse_args</span><span>()</span>      <span>if</span> <span>args</span><span>.</span><span>script</span><span>:</span>         <span>print</span><span>(</span><span>f</span><span>'</span><span>{</span><span>parser</span><span>.</span><span>prog</span><span>}</span><span> v</span><span>{</span><span>version</span><span>}</span><span> started on </span><span>{</span><span>now</span><span>()</span><span>}</span><span>'</span><span>)</span>         <span>exec</span><span>(</span><span>open</span><span>(</span><span>args</span><span>.</span><span>script</span><span>).</span><span>read</span><span>())</span>         <span>print</span><span>(</span><span>f</span><span>'</span><span>{</span><span>parser</span><span>.</span><span>prog</span><span>}</span><span> v</span><span>{</span><span>version</span><span>}</span><span> finished on </span><span>{</span><span>now</span><span>()</span><span>}</span><span>'</span><span>)</span>     <span>else</span><span>:</span>         <span>parser</span><span>.</span><span>print_usage</span><span>()</span>         <span>sys</span><span>.</span><span>exit</span><span>(</span><span>1</span><span>)</span> </pre></td></tr></tbody></table>`

## But does it work?

However, in the cases I’ve tested, this will not work. The `exec()` call does not seem to have any effect. One way to deal with this is to compile the script specified via command-line and execute the resulting code:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 </pre></td><td><pre><span>import</span> <span>os</span> <span>...</span> <span>def</span> <span>runner</span><span>():</span>     <span>...</span>     <span># exec(open(args.script).read()) </span>    <span>exec</span><span>(</span><span>compile</span><span>(</span><span>open</span><span>(</span><span>args</span><span>.</span><span>script</span><span>).</span><span>read</span><span>(),</span> <span>os</span><span>.</span><span>path</span><span>.</span><span>basename</span><span>(</span><span>args</span><span>.</span><span>script</span><span>),</span> <span>'exec'</span><span>))</span> </pre></td></tr></tbody></table>`

While this _does_ work, it has the disadvantage that the `__file__` builtin of the executed script gets overwritten. You might get something like this:

`<table><tbody><tr><td><pre>1 2 3 4 5 </pre></td><td><pre>runner v1.0.0 started on 2021-11-04 00:11:26 Running /full/path/to/mypackage/mypackage/__main__.py MY TEXT Done running /full/path/to/mypackage/mypackage/__main__.py runner v1.0.0 finished on 2021-11-04 00:11:26 </pre></td></tr></tbody></table>`

## The solution

There is still hope, thanks to the [`runpy`](https://docs.python.org/3/library/runpy.html) module in the standard library:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 </pre></td><td><pre><span>...</span> <span>def</span> <span>runner</span><span>():</span>     <span>...</span>     <span># exec(open(args.script).read()) </span>    <span># exec(compile(open(args.script).read(), os.path.basename(args.script), 'exec')) </span>    <span>argparse</span><span>.</span><span>Namespace</span><span>(</span><span>**</span><span>runpy</span><span>.</span><span>run_path</span><span>(</span><span>args</span><span>.</span><span>script</span><span>))</span> </pre></td></tr></tbody></table>`

Now we finally get the expected output, with `__file__` in `my_script.py` not being overwritten since `runpy` takes care to set it along with several other special global variables before `exec()`ing the code.

## Accompanying code

The full code accompanying this post can be found on my [GitHub](https://github.com/alexandra-zaharia/python-playground/tree/main/packaging_a_standalone_runner) repository.
