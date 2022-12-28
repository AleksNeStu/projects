---
source: https://alexandra-zaharia.github.io/posts/distribute-a-python-package-with-a-standalone-script-using-setuptools/ \
created: 2022-12-28T19:32:34 (UTC +01:00) \
tags: [] \
author: Alexandra Zaharia
---
# Distribute a Python package with a standalone script using setuptools | Alexandra Zaharia
---
Suppose you’ve written a Python package that you want to be able to `pip install` locally. Additionally, you also want to be able to run one of the scripts in the package via its name, without the `.py` extension and without explicitly using the Python interpreter to launch it. In other words, you want to be able to run

instead of

`<table><tbody><tr><td><pre>1 </pre></td><td><pre>python /path/to/my/package/standalone_script.py </pre></td></tr></tbody></table>`

This post explains how to achieve this using [`setuptools`](https://setuptools.pypa.io/).

Suppose the package is a simple one, containing only a readme file and a single module `core.py`. There is also going to be a `__init__.py` file detailing the imports from `core.py` that you would want to have available when you `import mypackage`. The starting project structure may look something like this:

`<table><tbody><tr><td><pre>1 2 3 4 </pre></td><td><pre>mypackage/     README.md     __init__.py     core.py </pre></td></tr></tbody></table>`

For the purpose of illustration, let us suppose that `core.py` contains a function `capitalize()` that takes a string and returns it in all caps (uppercase):

`<table><tbody><tr><td><pre>1 2 3 4 5 6 </pre></td><td><pre><span># core.py </span> <span>def</span> <span>capitalize</span><span>(</span><span>text</span><span>):</span>     <span>if</span> <span>not</span> <span>isinstance</span><span>(</span><span>text</span><span>,</span> <span>str</span><span>):</span>         <span>raise</span> <span>ValueError</span><span>(</span><span>'Need string to capitalize'</span><span>)</span>     <span>return</span> <span>text</span><span>.</span><span>upper</span><span>()</span> </pre></td></tr></tbody></table>`

The `__init__.py` file imports the only thing it can, i.e. the `capitalize()` function:

`<table><tbody><tr><td><pre>1 2 3 </pre></td><td><pre><span># __init__.py </span> <span>from</span> <span>mypackage.core</span> <span>import</span> <span>capitalize</span> </pre></td></tr></tbody></table>`

This way, each time you want to use the `mypackage` module, `capitalize()` becomes available. But you would need to go through the very tedious and error-prone approach of manually adding the path to `mypackage` every time you want to use it:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 </pre></td><td><pre><span># some_script.py </span> <span>import</span> <span>sys</span> <span>sys</span><span>.</span><span>path</span><span>.</span><span>append</span><span>(</span><span>'/path/to/mypackage'</span><span>)</span> <span>from</span> <span>mypackage</span> <span>import</span> <span>capitalize</span>  <span>print</span><span>(</span><span>capitalize</span><span>(</span><span>'this'</span><span>))</span> </pre></td></tr></tbody></table>`

That’s pretty lame, but fortunately we can do better.

You can package the project and then install it via `pip` locally. Then any script that needs the newly installed package can simply `import` it:

`<table><tbody><tr><td><pre>1 2 3 4 5 </pre></td><td><pre><span># some_script.py </span> <span>from</span> <span>mypackage</span> <span>import</span> <span>capitalize</span>  <span>print</span><span>(</span><span>capitalize</span><span>(</span><span>'this'</span><span>))</span> </pre></td></tr></tbody></table>`

In order to achieve this, only two steps are involved:

1.  reorganize the project structure
2.  create a `setup.py` file

For the project structure, simply create a subdirectory with the same name as the package name and move modules i.e. `.py` files inside it:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 </pre></td><td><pre>mypackage/     README.md     setup.py     mypackage/         __init__.py         core.py </pre></td></tr></tbody></table>`

The `setup.py` file has the following contents:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 </pre></td><td><pre><span>from</span> <span>setuptools</span> <span>import</span> <span>setup</span><span>,</span> <span>find_packages</span>  <span>setup</span><span>(</span>     <span>name</span><span>=</span><span>'mypackage'</span><span>,</span>     <span>version</span><span>=</span><span>'1.0.0'</span><span>,</span>     <span>description</span><span>=</span><span>'Capitalize strings'</span><span>,</span>     <span>author</span><span>=</span><span>'John Doe'</span><span>,</span>     <span>author_email</span><span>=</span><span>'doe@example.com'</span><span>,</span>     <span>packages</span><span>=</span><span>find_packages</span><span>(),</span> <span>)</span> </pre></td></tr></tbody></table>`

We can then install the package locally using `pip`:

`<table><tbody><tr><td><pre>1 </pre></td><td><pre>pip install -e /path/to/mypackage </pre></td></tr></tbody></table>`

The `/path/to/mypackage` above refers to the _top-level_ `mypackage/` directory.

The package may be uninstalled with:

`<table><tbody><tr><td><pre>1 </pre></td><td><pre>pip uninstall mypackage </pre></td></tr></tbody></table>`

## Standalone script

What if we wanted a standalone script to be installed along with `mypackage` that would run the `capitalize()` function on any string that we pass through the command line? Here is how the script would be used:

`<table><tbody><tr><td><pre>1 2 3 4 </pre></td><td><pre>$ capitalize usage: capitalize [-h] [-v] [string [string ...]] $ capitalize my text MY TEXT </pre></td></tr></tbody></table>`

In order to achieve this, we need to:

1.  create the script that runs the `capitalize()` function on the string that gets passed to it via the command line
2.  edit `setup.py` to instruct it how to “install” the script (i.e. how to make it accessible system-wide)

We will be creating the standalone script in a file called `__main__.py` that we place in the subdirectory containing the other Python modules:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 </pre></td><td><pre>mypackage/     README.md     setup.py     mypackage/         __init__.py         __main__.py         core.py </pre></td></tr></tbody></table>`

Then we write the script in the `main()` method of `__main__.py`:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 </pre></td><td><pre><span>import</span> <span>argparse</span> <span>import</span> <span>sys</span> <span>from</span> <span>mypackage</span> <span>import</span> <span>capitalize</span>   <span>def</span> <span>main</span><span>():</span>     <span>parser</span> <span>=</span> <span>argparse</span><span>.</span><span>ArgumentParser</span><span>(</span><span>prog</span><span>=</span><span>'capitalize'</span><span>)</span>     <span>parser</span><span>.</span><span>add_argument</span><span>(</span><span>'string'</span><span>,</span> <span>nargs</span><span>=</span><span>'*'</span><span>,</span> <span>help</span><span>=</span><span>'string to capitalize'</span><span>)</span>     <span>parser</span><span>.</span><span>add_argument</span><span>(</span><span>'-v'</span><span>,</span> <span>'--version'</span><span>,</span> <span>help</span><span>=</span><span>'display version'</span><span>,</span> <span>action</span><span>=</span><span>'version'</span><span>,</span>                         <span>version</span><span>=</span><span>f</span><span>'%(prog)s 1.0.0'</span><span>)</span>     <span>args</span> <span>=</span> <span>parser</span><span>.</span><span>parse_args</span><span>()</span>      <span>if</span> <span>args</span><span>.</span><span>string</span><span>:</span>         <span>text</span> <span>=</span> <span>' '</span><span>.</span><span>join</span><span>(</span><span>word</span> <span>for</span> <span>word</span> <span>in</span> <span>args</span><span>.</span><span>string</span><span>)</span>         <span>print</span><span>(</span><span>capitalize</span><span>(</span><span>text</span><span>))</span>     <span>else</span><span>:</span>         <span>parser</span><span>.</span><span>print_usage</span><span>()</span>         <span>sys</span><span>.</span><span>exit</span><span>(</span><span>1</span><span>)</span>   <span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>     <span>sys</span><span>.</span><span>exit</span><span>(</span><span>main</span><span>())</span> </pre></td></tr></tbody></table>`

At lines 7-11, we add an [argument parser](https://docs.python.org/3/library/argparse.html). It can either display the program version (through `-v` or `--version`) or consume all the command line arguments (`nargs='*'`) in order to pass them to the `capitalize()` function (lines 13-15).

The only thing left to do now is to point `setup.py` to the `main()` function of the `__main__.py` module and to ask it to add it as a console script “entry point” called `capitalize`:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 </pre></td><td><pre><span>from</span> <span>setuptools</span> <span>import</span> <span>setup</span><span>,</span> <span>find_packages</span>  <span>setup</span><span>(</span>     <span>name</span><span>=</span><span>"mypackage"</span><span>,</span>     <span># [snip] </span>    <span>entry_points</span> <span>=</span> <span>{</span><span>'console_scripts'</span><span>:</span> <span>[</span><span>'capitalize = mypackage.__main__:main'</span><span>]},</span> <span>)</span> </pre></td></tr></tbody></table>`

That’s it! Now the package may be installed with `pip` as shown above and the `capitalize` script becomes available system-wide in the current Python environment. You might want to read the [next post](https://alexandra-zaharia.github.io/posts/standalone-python-script-to-run-other-python-scripts/) for a special tricky situation involving the use of the standalone script as a runner.

## Accompanying code

The full code accompanying this post can be found on my [GitHub](https://github.com/alexandra-zaharia/python-playground/tree/main/packaging_a_standalone) repository.
