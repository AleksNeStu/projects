---
source: https://alexandra-zaharia.github.io/posts/use-cases-for-python-environment-variables/ \
created: 2022-12-28T18:52:19 (UTC +01:00) \
tags: [] \
author: Alexandra Zaharia
---
# Use cases for Python environment variables | Alexandra Zaharia
---
Today’s post focuses on environment variables in Python. They are one of several possible mechanisms for setting various configuration parameters. We can:

-   read environment variables (through [`os.environ`](https://docs.python.org/3/library/os.html) or [`dotenv`](https://pypi.org/project/python-dotenv/)) \[the current post\]
-   have the script accept command-line arguments (use [`argparse`](https://docs.python.org/3/library/argparse.html))
-   load configuration settings from a file, such as:
    -   a JSON file (use [`json`](https://docs.python.org/3/library/json.html))
    -   a YAML file (use [`pyyaml`](https://wiki.python.org/moin/YAML))
    -   a XML file (use [`lxml`](https://lxml.de/), [`ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html) or [`minidom`](https://docs.python.org/3/library/xml.dom.minidom.html))
    -   an INI file (use [`configparser`](https://docs.python.org/3/library/configparser.html)) \[check out [this post](https://alexandra-zaharia.github.io/posts/python-configuration-and-dataclasses/)\]
    -   your DIY file format (for which you will be rolling your own parser)

## What is the best solution?

The answer is… _it depends_.

There is no one-size-fits-all solution. It depends on what you’re trying to achieve and on how the current software architecture looks like. If you’re working on a command-line tool that must accommodate a plethora of options, chances are you’ll be using `argparse`. For other types of projects (such as a server or a client), a configuration file might be more practical. Yet in other situations you may also want to consider using environment variables.

We will be looking in more detail at three such use cases in this post, where we will see how environment variables can be a good choice.

But first, let’s get the next point out of the way:

## But environment variables are evil, right?

Well… _it depends_.

Indeed, using environment variables for non-sensitive information that you could just as well transmit via command-line arguments or via a configuration file is not ideal. Why? Because being _environment_ variables, they actually live _outside_ of the code base. Sure, you can access them based on their key (their name) and attach some meaning to them, but this is neither the most Pythonic, nor the most effective way, to do things (if this can be avoided).

Nevertheless, there are also legit cases where environment variables are preferable:

-   when setting execution mode (e.g. debug or development mode vs production mode)
-   when they improve security practices
-   when they are the only way to get some values into a “black box” (more on that later)

Before diving into the use cases, let us first briefly see how to access environment variables in Python.

## Accessing environment variables in Python

Environment variables are read through [`os.environ`](https://docs.python.org/3/library/os.html). Although they can also be modified or cleared, such changes are only effective in the current Python session (and for subprocesses started with `os.system()`, `popen()`, `fork()` and `execv()`). In other words, if you change an environment variable in a Python script, the change will not be reflected in the environment once that script exits.

### os.environ

In the most simple form, you can export an environment variable through the shell:

Then you can read its value through `os.environ`:

`<table><tbody><tr><td><pre>1 2 3 4 </pre></td><td><pre><span>In</span> <span>[</span><span>1</span><span>]:</span> <span>import</span> <span>os</span>  <span>In</span> <span>[</span><span>2</span><span>]:</span> <span>os</span><span>.</span><span>environ</span><span>.</span><span>get</span><span>(</span><span>'foo'</span><span>)</span> <span>Out</span><span>[</span><span>2</span><span>]:</span> <span>'bar'</span> </pre></td></tr></tbody></table>`

Note that, for non-existent keys, `os.environ.get()` returns `None`.

Also note that the values of _all_ environment variables are strings. To address this, you may want to roll your own small environment parser. Mine looks like this:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 </pre></td><td><pre><span>import</span> <span>os</span>   <span>def</span> <span>parse_string</span><span>(</span><span>value</span><span>):</span>     <span>if</span> <span>value</span><span>.</span><span>lower</span><span>()</span> <span>==</span> <span>'true'</span><span>:</span>         <span>return</span> <span>True</span>     <span>if</span> <span>value</span><span>.</span><span>lower</span><span>()</span> <span>==</span> <span>'false'</span><span>:</span>         <span>return</span> <span>False</span>      <span>try</span><span>:</span>         <span>value</span> <span>=</span> <span>int</span><span>(</span><span>value</span><span>)</span>         <span>return</span> <span>value</span>     <span>except</span> <span>ValueError</span><span>:</span>         <span>try</span><span>:</span>             <span>value</span> <span>=</span> <span>float</span><span>(</span><span>value</span><span>)</span>         <span>finally</span><span>:</span>             <span>return</span> <span>value</span>   <span>def</span> <span>get_env_setting</span><span>(</span><span>setting</span><span>):</span>     <span>if</span> <span>setting</span> <span>not</span> <span>in</span> <span>os</span><span>.</span><span>environ</span><span>:</span>         <span>return</span> <span>None</span>      <span>return</span> <span>parse_string</span><span>(</span><span>os</span><span>.</span><span>environ</span><span>[</span><span>setting</span><span>])</span> </pre></td></tr></tbody></table>`

I use `get_env_setting()` to retrieve a value from `os.environ` (if the key exists) and I try to convert it to different data types:

-   first, as a bool (this is because if I set boolean environment variables in Python, I store their `str()` representation, meaning `'True'` for `True` and `'False'` for `False`);
-   if this fails, the value is converted to an `int`;
-   if this fails as well, the value is converted to a `float`:
    -   if successful, `parse_string()` returns a `float`;
    -   if not, it returns a `str`.

### dotenv

To set multiple environment variables, you could create a bash script and ensure you run it before starting the Python script that needs these environment variables. But there is something more effective than this: [`dotenv`](https://pypi.org/project/python-dotenv/) allows you to load environment variables from a `.env` file having the following format:

`<table><tbody><tr><td><pre>1 2 3 4 </pre></td><td><pre><span># Development settings</span> <span>DOMAIN</span><span>=</span>example.org <span>ADMIN_EMAIL</span><span>=</span>admin@<span>${</span><span>DOMAIN</span><span>}</span> <span>ROOT_URL</span><span>=</span><span>${</span><span>DOMAIN</span><span>}</span>/app </pre></td></tr></tbody></table>`

Notice the `.env` file understands UNIX expansion (e.g. `${DOMAIN}`).

[`dotenv`](https://pypi.org/project/python-dotenv/) loads the environment variables from `.env` into the environment:

`<table><tbody><tr><td><pre>1 2 </pre></td><td><pre><span>from</span> <span>dotenv</span> <span>import</span> <span>load_dotenv</span> <span>load_dotenv</span><span>()</span> </pre></td></tr></tbody></table>`

Now the environment variables `DOMAIN`, `ADMIN_EMAIL` and `ROOT_URL` are accessible to the Python script and may be retrieved via `os.environ.get()` as shown above.

## Use case: setting execution mode

Here is a classic use case for environment variables. Suppose you don’t want to add an explicit `-d` / `--debug` flag for your app. Then you could just export an environment variable to do the trick:

The app would behave differently depending on the value of `MY_APP_DEBUG`.

Taking this idea one step further, you could use an environment variable `MY_APP_MODE` to choose between `development`, `staging` and `production` modes.

## Use case: securing access tokens

Many applications require access tokens: they can be API tokens, database passwords and so on. Storing such sensitive information inside the code base is just an accident waiting to happen, no matter how _sure_ you are that you’re _never_ going to commit that special extra line to version control.

Here’s where environment variables come in handy. You could add your secret tokens to the `.env` file and load it with `dotenv` as we’ve seen above. Of course, you’d need to make sure that your `.gitignore` or `.hgignore` contains the `.env` file.

In short, instead of:

`<table><tbody><tr><td><pre>1 2 3 4 </pre></td><td><pre><span># NOTE TO SELF: DO ***NOT*** COMMIT THIS TO VERSION CONTROL! </span><span>SECRET_TOKEN</span> <span>=</span> <span>'56a682c4d000c676f543124b332a2921'</span> <span># ... </span><span>do_stuff_with</span><span>(</span><span>SECRET_TOKEN</span><span>)</span> </pre></td></tr></tbody></table>`

prefer adding your `SECRET_TOKEN` to `.env`, adding `.env` to your version control’s ignore file, and finally:

`<table><tbody><tr><td><pre>1 2 3 4 </pre></td><td><pre><span>dotenv</span><span>.</span><span>load_dotenv</span><span>()</span> <span># ... </span><span>SECRET_TOKEN</span> <span>=</span> <span>os</span><span>.</span><span>environ</span><span>.</span><span>get</span><span>(</span><span>'SECRET_TOKEN'</span><span>)</span> <span>do_stuff_with</span><span>(</span><span>SECRET_TOKEN</span><span>)</span> </pre></td></tr></tbody></table>`

## Use case: injecting configuration into a black box

This final use case is something you’re not going to come across very often in internet discussions. It’s something I call a “black box”, meaning code that you have no control over: you didn’t write it, you cannot change it but you have to run it. Along these lines, remember how I wrote in a [previous post](https://alexandra-zaharia.github.io/posts/standalone-python-script-to-run-other-python-scripts/) about creating a Python script that runs user code from other Python scripts. That’s the kind of use case I am referring to.

OK, you may ask, _but why???_ Why would you want to run code that you have no control over? Well, suppose you’re writing a testing framework that other people may use to write tests for… well, testing stuff. The tests are not relevant, only the part about _having to run them_ is. There are two aspects at play here:

-   the framework is a **library** that users import from in order to write their tests;
-   the framework is also a **framework**, meaning a master runner script that runs the user scripts.

For the users’ sake, their only task should be to read and understand the framework’s well-documented API. They should _not_ have to fiddle around with passing configuration options into their code. The configuration options for running their scripts through the framework may be sent through the command line and/or through configuration files.

What a user script typically does is to import abstractions from the framework and to use them for creating and executing tests. For example:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 </pre></td><td><pre><span># user_script.py </span><span>from</span> <span>fancy_framework</span> <span>import</span> <span>Test</span><span>,</span> <span>PhaseResult</span>  <span>def</span> <span>a_test_phase</span><span>(</span><span>api</span><span>):</span>     <span>do_stuff</span><span>()</span>  <span># assume this exists </span> <span>def</span> <span>another_test_phase</span><span>(</span><span>api</span><span>):</span>     <span>if</span> <span>not</span> <span>check_stuff</span><span>():</span>  <span># assume this exists </span>        <span>return</span> <span>PhaseResult</span><span>.</span><span>FAIL</span>  <span>my_test</span> <span>=</span> <span>Test</span><span>(</span><span>a_test_phase</span><span>,</span> <span>another_test_phase</span><span>,</span> <span>name</span><span>=</span><span>'My Test'</span><span>)</span> <span>my_test</span><span>.</span><span>execute</span><span>()</span> </pre></td></tr></tbody></table>`

Let us suppose that if the user script is ran with verbosity off (default), it only shows the test result:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 </pre></td><td><pre>$ fancy_framework user_script.py  ====================== Running test My Test (attempt #1) =======================  Finished running test My Test ......................................... [ FAIL ] ________________________________________________________________________________  $ </pre></td></tr></tbody></table>`

When the script is ran with the `--verbose` flag, it displays phase results as well:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 </pre></td><td><pre>$ fancy_framework --verbose user_script.py  ====================== Running test My Test (attempt #1) =======================  Phase a_test_phase .................................................... [ PASS ] Phase another_test_phase .............................................. [ FAIL ]  Finished running test My Test ......................................... [ FAIL ] ________________________________________________________________________________  $ </pre></td></tr></tbody></table>`

Now remember that what the `fancy_framework` does among other things is to simply run the provided `user_script.py`. How should a `fancy_framework.Test` object know whether verbosity is on when its `execute()` method is called? Here is where environment variables step in to save the day:

-   The `fancy_framework` exports an environment variable `FANCY_FRAMEWORK_VERBOSITY` according to the user’s choice (whether the `--verbose` flag was used).
-   When a `Test` object is initialized, it reads the value of `FANCY_FRAMEWORK_VERBOSITY` from `os.environ` and stores it in an instance variable `self._verbose`.
-   When the `execute()` method of the `Test` instance is called, details are printed to stdout only if `self._verbose` is true.

Here is a simplified version (using the `get_env_setting()` helper we’ve seen above):

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 </pre></td><td><pre><span>class</span> <span>Test</span><span>:</span>     <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>*</span><span>phases</span><span>,</span> <span>name</span><span>=</span><span>None</span><span>):</span>         <span>self</span><span>.</span><span>_phases</span> <span>=</span> <span>create_phases</span><span>(</span><span>phases</span><span>)</span>  <span># assume this exists </span>        <span>self</span><span>.</span><span>_name</span> <span>=</span> <span>name</span>         <span>self</span><span>.</span><span>_verbose</span> <span>=</span> <span>get_env_settings</span><span>(</span><span>'FANCY_FRAMEWORK_VERBOSITY'</span><span>)</span>      <span>def</span> <span>execute</span><span>(</span><span>self</span><span>):</span>         <span>print_running_test</span><span>(</span><span>self</span><span>)</span>  <span># assume this exists </span>         <span>for</span> <span>phase</span> <span>in</span> <span>self</span><span>.</span><span>_phases</span><span>:</span>             <span>phase</span><span>.</span><span>run</span><span>()</span>             <span>if</span> <span>self</span><span>.</span><span>_verbose</span><span>:</span>                 <span>print_phase_outcome</span><span>(</span><span>phase</span><span>)</span>  <span># assume this exists </span>         <span>print_test_outcome</span><span>(</span><span>self</span><span>)</span>  <span># assume this exists </span></pre></td></tr></tbody></table>`

Isn’t that neat? In this use case we’ve seen how environment variables can be used to inject configuration into a black-box system.

Check out [this article](https://alexandra-zaharia.github.io/posts/python-configuration-and-dataclasses/) for a discussion of passing configuration options in Python in such a way as to only use _identifiers_ instead of strings for the configuration keys.
