**[A]**


**[B]**

**[C]**
> Concurrency
- [asyncio](https://docs.python.org/3/library/asyncio.html) <br>
  asyncio is a library to write concurrent code using the async/await syntax.
asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc. 
   

- [thread](https://docs.python.org/3/library/threading.html) <br>
  threading — Thread-based parallelism <br>
  https://realpython.com/intro-to-python-threading/
  https://www.tutorialspoint.com/python/python_multithreading.htm

  
- [Multiprocessing](https://towardsdatascience.com/how-to-use-the-multiprocessing-package-in-python3-a1c808415ec2)  <br>
  Multiprocessing leverages the entirety of CPU cores (multiple processes), whereas Multithreading maps multiple threads to every process. In multiprocessing, each process is associated with its own memory, which doesn’t lead to data corruption or deadlocks. Threads utilize shared memory, henceforth enforcing the thread locking mechanism. For CPU-related jobs, multiprocessing is preferable, whereas, for I/O-related jobs (IO-bound vs. CPU-bound tasks), multithreading performs better. <br>
https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python <br>
  https://realpython.com/learning-paths/python-concurrency-parallel-programming/   


- [trio](https://github.com/python-trio/trio) <br>
  Trio – a friendly Python library for async concurrency and I/O
  The Trio project aims to produce a production-quality, permissively licensed, async/await-native I/O library for Python. Like all async libraries, its main purpose is to help you write programs that do multiple things at the same time with parallelized I/O. A web spider that wants to fetch lots of pages in parallel, a web server that needs to juggle lots of downloads and websocket connections simultaneously, a process supervisor monitoring multiple subprocesses... that sort of thing. Compared to other libraries, Trio attempts to distinguish itself with an obsessive focus on usability and correctness. Concurrency is complicated; we try to make it easy to get things right.
  

- [trio-asyncio](https://github.com/python-trio/trio-asyncio) <br>
  trio-asyncio is a re-implementation of the asyncio mainloop on top of Trio.
  Trio has native concepts of tasks and task cancellation. Asyncio is based on callbacks and chaining Futures, albeit with nicer syntax, making handling failures and timeouts fundamentally less reliable, especially in larger programs. Thus, you really want to base your async project on Trio.
On the other hand, there are quite a few asyncio-enhanced libraries. You really don't want to re-invent any wheels in your project.
Thus, being able to use asyncio libraries from Trio is useful. trio-asyncio enables you to do that and more.



- [unsync](https://github.com/alex-sherman/unsync) <br>
  Unsynchronize asyncio by using an ambient event loop, or executing in separate threads or processes.
  https://asherman.io/projects/unsync.html


- [uvloop](https://github.com/MagicStack/uvloop) <br>
  uvloop is a fast, drop-in replacement of the built-in asyncio event loop. uvloop is implemented in Cython and uses libuv under the hood.


- [AIOHTTP](https://docs.aiohttp.org/en/stable/) <br>
  Asynchronous HTTP Client/Server for asyncio and Python.
  Supports both Client and HTTP Server.
  Supports both Server WebSockets and Client WebSockets out-of-the-box without the Callback Hell.


- [aiofiles](https://github.com/Tinche/aiofiles) <br>
  aiofiles is an Apache2 licensed library, written in Python, for handling local disk files in asyncio applications.

  Ordinary local file IO is blocking, and cannot easily and portably made asynchronous. This means doing file IO may interfere with asyncio applications, which shouldn't block the executing thread. aiofiles helps with this by introducing asynchronous versions of files that support delegating operations to a separate thread pool.
 Web-server has Middlewares, Signals and plugable routing.

- [greenlets](https://greenlet.readthedocs.io/en/latest/) <br>
  greenlets are lightweight coroutines for in-process sequential concurrent programming.<br>
  greenlets can be used on their own, but they are frequently used with frameworks such as gevent to provide higher-level abstractions and asynchronous I/O.<br>
  greenlets are frequently defined by analogy to threads or Python’s built-in coroutines (generators and async def functions). The rest of this section will explore those analogies. For a more precise introduction, see greenlet Concepts.<br>
  See History And About for how the greenlet library was created, and its relation to other similar concepts<br>
  Are greenlets similar to threads? <br>
  For many purposes, you can usually think of greenlets as cooperatively scheduled threads. The major differences are that since they’re cooperatively scheduled, you are in control of when they execute, and since they are coroutines, many greenlets can exist in a single native thread.
  ```In contrast, greenlets are cooperative and sequential. This means that when one greenlet is running, no other greenlet can be running; the programmer is fully in control of when execution switches between greenlets. This can eliminate race conditions and greatly simplify the programming task. Also, threads require resources from the operating system (the thread stack, and bookkeeping in the kernel). Because greenlets are implemented entirely without involving the operating system, they can require fewer resources; it is often practical to have many more greenlets than it is threads.```

- [Twisted](https://pypi.org/project/Twisted/) + use greenlets!!!
  Code as sync but it's ansync!!!
  An asynchronous networking framework written in Python
  What is this?
  Twisted is an event-based framework for internet applications, supporting Python 3.6+. It includes modules for many different purposes, including the following:
twisted.web: HTTP clients and servers, HTML templating, and a WSGI server
twisted.conch: SSHv2 and Telnet clients and servers and terminal emulators
twisted.words: Clients and servers for IRC, XMPP, and other IM protocols
twisted.mail: IMAPv4, POP3, SMTP clients and servers
twisted.positioning: Tools for communicating with NMEA-compatible GPS receivers
twisted.names: DNS client and tools for making your own DNS servers
twisted.trial: A unit testing framework that integrates well with Twisted-based code.
Twisted supports all major system event loops – select (all platforms), poll (most POSIX platforms), epoll (Linux), kqueue (FreeBSD, macOS), IOCP (Windows), and various GUI event loops (GTK+2/3, Qt, wxWidgets). Third-party reactors can plug into Twisted, and provide support for additional event loops.



> Code style
- [flake8](https://pypi.org/project/flake8/) <br>
  the modular source code checker: pep8 pyflakes and co

**[D]**
> Dependencies
- [The Nine Circles of Python Dependency Hell](https://medium.com/knerd/the-nine-circles-of-python-dependency-hell-481d53e3e025)
- [pip-conflict-checker](https://github.com/ambitioninc/pip-conflict-checker) <br>
  A tool that checks installed packages against all package requirements to ensure that there are no dependency version conflicts.
- [pipdeptree](https://pypi.org/project/pipdeptree/) <br>
Command line utility to show dependency tree of packages
- [pip-tools](https://github.com/jazzband/pip-tools) <br>
  A set of command line tools to help you keep your pip-based packages fresh, even when you've pinned them. You do pin them, right? (In building your Python application and its dependencies for production, you want to make sure that your builds are predictable and deterministic.)
- [poetry](https://pypi.org/project/poetry/) \
  https://python-poetry.org/ \
  Poetry helps you declare, manage and install dependencies of Python projects, ensuring you have the right stack everywhere. <br>
  Packaging systems and dependency management in Python are rather convoluted and hard to understand for newcomers. Even for seasoned developers it might be cumbersome at times to create all files needed in a Python project: setup.py, requirements.txt, setup.cfg, MANIFEST.in and the newly added Pipfile. <br>
  So I wanted a tool that would limit everything to a single configuration file to do: dependency management, packaging and publishing. <br>
  And, finally, there is no reliable tool to properly resolve dependencies in Python, so I started poetry to bring an exhaustive dependency resolver to the Python community. <br>
  poetry is a tool to handle dependency installation as well as building and packaging of Python packages. It only needs one file to do all of that: the new, standardized pyproject.toml.<br>
  In other words, poetry uses pyproject.toml to replace setup.py, requirements.txt, setup.cfg, MANIFEST.in and the newly added Pipfile.<br>
  So I wanted a tool that would limit everything to a single configuration file to do: dependency management, packaging and publishing. <br>
  By default, Poetry create virtual environment in $HOME/.poetry for cahcing/sharing purpose.
  ```poetry config virtualenvs.in-project true``` - always create virtual environment in the root directory of a project.
  ```poetry config --local virtualenvs.in-project true``` - one time
  https://www.yippeecode.com/topics/python-poetry-cheat-sheet/
```
# 1) Set Poetry always create virtual environment in the root directory. 
poetry config virtualenvs.in-project true

# 2) Navigate to the project dir
cd <project_dir>

# 3) Create a Virtual Environment (e.g. python = 3.10 - depends on os setup)
poetry init - pyproject.toml interactively create

poetry env use python
#* Switching between environments
poetry env use system
poetry env use python3.10
poetry env use /full/path/to/python

poetry lock - poetry.lock file, locking the project to those specific versions.

# 4) Activate Vitual Environment
poetry shell

# 5) Show env
which python
poetry env info --path
poetry env list --full-path - Find the list of virtual environments including its full path.

# 6) Remove env
poetry env remove /full/path/to/python
poetry env remove python3.10
poetry env remove 3.10
poetry env remove test-O3eWbxRl-py3.10

# 7) Add
poetry add "Flask==1.1.2"
poetry add "Flask==1.1.2" --dev - Adding package in dev-dependencies.
poetry add "/path/to/locallib" - Add local dependency by specifying the library path.
poetry add pendulum@^2.0.5
poetry add "pendulum>=2.0.5"
poetry add pendulum@latest
poetry add git+https://github.com/sdispater/pendulum.git

--dev (-D): Add package as development dependency.
--path: The path to a dependency.
--optional : Add as an optional dependency.
--dry-run : Outputs the operations but will not execute anything (implicitly enables –verbose).
--lock : Do not perform install (only update the lockfile).


# 8) Delete dependencies
poetry remove Flask

# 9) Update dependencies
poetry update - Update all poetry packages that are defined in pyproject.toml.
poetry update Flask - update individual packages by specifying the name.
poetry show --tree - Show the list of all packages installed with description.
poetry show Flask - Show information about a specific package.

--dry-run : Outputs the operations but will not execute anything (implicitly enables –verbose).
--no-dev : Do not install dev dependencies.
--lock : Do not perform install (only update the lockfile).

# 10) Install dependencies
poetry install - The install command reads the pyproject.toml file from the current project, resolves the dependencies, and installs them. If there is a poetry.lock file in the current directory, it will use the exact versions from there instead of resolving them.

--no-dev: Do not install dev dependencies.
--no-root: Do not install the root package (your project).
--extras (-E): Features to install (multiple values allowed).

# 11) Export
poetry export -f requirements.txt --output requirements.txt

# 12) Build & Publish
poetry build - Easily build and package your projects with a single command.
poetry publish - Make your work known by publishing it to PyPI.
```

- [pdm](https://github.com/pdm-project/pdm) <br>
  A modern Python package manager with PEP 582 support.
  PDM is meant to be a next generation Python package management tool. It was originally built for personal use. If you feel you are going well with Pipenv or Poetry and don't want to introduce another package manager, just stick to it. But if you are missing something that is not present in those tools, you can probably find some goodness in pdm. <br>

> Documentation
- [Sphinx](https://www.sphinx-doc.org/en/master/) <br>
  Sphinx is a tool that makes it easy to create intelligent and beautiful documentation

**[E]**
> Environment
- [virtualenvs](https://docs.python-guide.org/dev/virtualenvs/) <br>
  Pipenv & Virtual Environments
- [pyenv](https://github.com/pyenv/pyenv) <br>
pyenv lets you easily switch between multiple versions of Python.
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) <br>
  pyenv-virtualenv is a pyenv plugin that provides features to manage virtualenvs and conda environments for Python on UNIX-like systems.  
  ```
  // Create virtual environment
  $ pyenv virtualenv 3.7.3 my-env
  // Activate virtual environment
  $ pyenv activate my-env
  // Exit virtual environment
  (my-env)$ pyenv deactivate
  ```
- [pipenv](https://github.com/pypa/pipenv) <br>
  Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. Windows is a first-class citizen, in our world.

- [venv](https://docs.python.org/3/library/venv.html) <br>
  venv - Creation of virtual environments
  ```python -m venv ~/.virtualenvs/my-env```
- [virtualenv](https://github.com/pypa/virtualenv) <br>
  virtualenv is a tool to create isolated Python environments. Since Python 3.3, a subset of it has been integrated into the standard library under the venv module. The venv module does not offer all features of this library, to name just a few more prominent:
- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html) <br>
  virtualenvwrapper is a set of extensions to Ian Bicking’s virtualenv tool

> Data
- [pandas.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) <br>
    ```
    data = {k1: v2, k2: v2, ...}
    df_product = pd.DataFrame.from_dict(data)
    df_product.to_csv('product_info.csv')
```

**[F]**
> Frameworks
- 1
- 2

**[G]**
- [GIL](https://realpython.com/python-gil/)<br>
  The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter. <br>
  This means that only one thread can be in a state of execution at any point in time. The impact of the GIL isn’t visible to developers who execute single-threaded programs, but it can be a performance bottleneck in CPU-bound and multi-threaded code. <br>
  > **alternative** <br>
  Jython and IronPython are different python implementations, both of which run on different virtual machines. Jython runs on the JVM (Java virtual machine) and IronPython runs on the CLR (common language runtime). This means that programs using these implementations can take advantage of the libraries and ecosystem of the virtual machines. For example, using Jython, I can write a plugin for a Java application, and using IronPython I can use the .NET standard library. The downside to using a different implementation to CPython is that CPython is the most used python, and therefore has the best support from libraries and developers. For example, a popular library like NumPy will only work on CPython, as it relies on CPython's C api, which neither Jython or IronPython can provide.
- 
**[H]**

**[I]**
> IDE
- [Anaconda Python IDE](http://damnwidget.github.io/anaconda/) <br>
  Anaconda turns your Sublime Text 3 into a full featured Python development IDE


**[J]**

**[K]**

**[L]**

**[M]**
> Memory (performance testing)
 * Python profiling  has three critical parts including:
 - Definition & explanation;
 - Tools  for a generic app developed using Python language;
 - APM (application performance monitoring) tools

 - [Pympler](https://pythonhosted.org/Pympler/) <br>
   Pympler is a development tool to measure, monitor and analyze the memory behavior of Python objects in a running Python application.<br>
   By pympling a Python application, detailed insight in the size and the lifetime of Python objects can be obtained. Undesirable or unexpected runtime behavior like memory bloat and other “pymples” can easily be identified.<br>
Pympler integrates three previously separate modules into a single, comprehensive profiling tool. The asizeof module provides basic size information for one or several Python objects, module muppy is used for on-line monitoring of a Python application and module Class Tracker provides off-line analysis of the lifetime of selected Python objects. <br>
A web profiling frontend exposes process statistics, garbage visualisation and class tracker statistics. <br>

 - [Timeit](https://www.guru99.com/timeit-python-examples.html) <br>
   Python timeit() is a method in Python library to measure the execution time taken by the given code snippet. The Python library runs the code statement 1 million times and provides the minimum time taken from the given set of code snippets. Python timeit() is a useful method that helps in checking the performance of the code.
 - [time](https://www.programiz.com/python-programming/time) <br>
   The time() function returns the number of seconds passed since epoch.
 - [codetiming](https://pypi.org/project/codetiming/) <br>
   A flexible, customizable timer for your Python code
 - [Intel® VTune™ Profiler](https://www.intel.com/content/www/us/en/develop/documentation/vtune-help/top/analyze-performance/code-profiling-scenarios/python-code-analysis.html) <br>
   Python* Code Analysis<br>
   When you attach the VTune Profiler to the Python process, make sure you initialize the Global Interpreter Lock (GIL) inside your script before you start the analysis. If GIL is not initialized, the VTune Profiler collector initializes it only when a new Python function is called.<br>
   Explore performance analysis options provided by the Intel® VTune™ Profiler for Python* applications to identify the most time-consuming code sections and critical call paths.<br>
   VTune Profiler supports the Hotspots, Threading, and Memory Consumption analysis for Python* applications via the Launch Application and Attach to Process modes. For example, when your application does excessive numerical modeling, you need to know how effectively it uses available CPU resources. A good example of the effective CPU usage is when the calculating process spends most time executing native extension and not interpreting Python glue code.<br>
   To get the maximum performance out of your Python application, consider using native extensions, such as NumPy or writing and compiling performance critical modules of your Python project in native languages, such as C or even assembly. This will help your application take advantage of vectorization and make complete use of powerful CPU resources.<br>
   To analyze the Python code performance with the VTune Profiler and interpret data:<br>
 - [wrk](https://github.com/wg/wrk) <br>
   wrk - a HTTP benchmarking tool
   wrk is a modern HTTP benchmarking tool capable of generating significant load when run on a single multi-core CPU. It combines a multithreaded design with scalable event notification systems such as epoll and kqueue. <br>
An optional LuaJIT script can perform HTTP request generation, response processing, and custom reporting. Details are available in SCRIPTING and several examples are located in scripts/. <br>
 - [cProfile](https://docs.python.org/3/library/profile.html) <br>
   cProfile and profile provide deterministic profiling of Python programs. A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.
   https://stackify.com/why-python-cprofile-is-the-recommended-profiling-interface/
   ```
    Simple cProfile Program Example:
    from simul import benchmark
    import cProfile
    pr = cProfile.Profile()
    pr.enable()
    benchmark()
    pr.disable()
    pr.print_stats()
    ```
 - [profile, cProfile, and pstats – Performance analysis of Python programs](http://pymotw.com/2/profile/) <br>
   The profile and cProfile modules provide APIs for collecting and analyzing statistics about how Python source consumes processor resources.
   The standard report created by the profile functions is not very flexible. If it doesn’t meet your needs, you can produce your own reports by saving the raw profiling data from run() and runctx() and processing it separately with the Stats class from pstats. <br>
   cProfile and profile provide deterministic profiling of Python programs. A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module. <br>
   cProfile is recommended for most users; it’s a C extension with reasonable overhead that makes it suitable for profiling long-running programs. Based on lsprof, contributed by Brett Rosen and Ted Czotter.
New in version 2.5. <br>
profile, a pure Python module whose interface is imitated by cProfile, but which adds significant overhead to profiled programs. If you’re trying to extend the profiler in some way, the task might be easier with this module. Originally designed and written by Jim Roskind. <br>
Changed in version 2.4: Now also reports the time spent in calls to built-in functions and methods.
hotshot was an experimental C module that focused on minimizing the overhead of profiling, at the expense of longer data post-processing times. It is no longer maintained and may be dropped in a future version of Python. <br>

   https://docs.python.org/2.7/library/profile.html#the-stats-class - 
   https://docs.python.org/2.7/library/profile.html

 - [gprof2dot](https://github.com/jrfonseca/gprof2dot) <br>
 This is a Python script to convert the output from many profilers into a dot graph.

 - [memory-profiler]() <br>
   A module for monitoring memory usage of a python program.
   This is a python module for monitoring memory consumption of a process as well as line-by-line analysis of memory consumption for python programs. It is a pure python module which depends on the psutil module.

 - [psutil](https://pypi.org/project/psutil/) <br>
   Cross-platform lib for process and system monitoring in Python.
   psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes. It implements many functionalities offered by classic UNIX command line tools such as ps, top, iotop, lsof, netstat, ifconfig, free and others. psutil currently supports the following platforms:


> Memory (Managment)
- [Memory Management](https://docs.python.org/3/c-api/memory.html) 

**[N]**

**[O]**

**[P]**
> Project
- [Python Project Template](https://github.com/seanfisk/python-project-template) <br>
  This project provides a best-practices template Python project which integrates several different tools. It saves you work by setting up a number of things, including documentation, code checking, and unit test runners.
  https://docs.python-guide.org/writing/structure/
- [Paver](https://pythonhosted.org/Paver/) <br>
  It is designed to help out with all of your other repetitive tasks (run documentation generators, moving files around, downloading things), all with the convenience of Python’s syntax and massive library of code.
- [The Hitchhiker's Guide to Python: Best Practices for Development 1st Edition](https://www.amazon.com/Hitchhikers-Guide-Python-Practices-Development/dp/1491933178/ref=as_li_ss_il?ie=UTF8&linkCode=li2&tag=bookforkind-20&linkId=804806ebdacaf3b56567347f3afbdbca) <br>
  This guide, collaboratively written by over a hundred members of the Python community, describes best practices currently used by package and application developers. Unlike other books for this audience, The Hitchhiker’s Guide is light on reusable code and heavier on design philosophy, directing the reader to excellent sources that already exist.
  
> Packages
- [distutils](https://docs.python.org/3/library/distutils.html#module-distutils) <br>
  The distutils package provides support for building and installing additional modules into a Python installation. The new modules may be either 100%-pure Python, or may be extension modules written in C, or may be collections of Python packages which include modules coded in both Python and C.
- [setuptools](https://setuptools.readthedocs.io/en/latest/) <br>
  Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects.

> Password
- [passlib](https://github.com/glic3rinu/passlib)
  
  Passlib is a password hashing library for Python 2 & 3, which provides cross-platform implementations of over 30 password hashing algorithms, as well as a framework for managing existing password hashes. It's designed to be useful for a wide range of tasks, from verifying a hash found in /etc/shadow, to providing full-strength password hashing for multi-user application.


**[Q]**

**[R]**

**[S]** 
> Slides
- [speakerdeck](https://speakerdeck.com/)

> Study
- [geeksforgeeks.org](https://www.geeksforgeeks.org)
- [ya be dev](https://www.youtube.com/channel/UCNuItlOR3qXZBtMRwb4GoBg)

**[T]**
> Testing
- [pytest](https://pytest.org/en/6.2.x/) <br>
  The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.
- [mock](https://docs.python.org/3/library/unittest.mock.html) <br>
  unittest.mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
- [tox](https://tox.readthedocs.io/en/latest/) <br>
  tox aims to automate and standardize testing in Python. It is part of a larger vision of easing the packaging, testing and release process of Python software.

- shebang <br>
https://www.jetbrains.com/help/pycharm/creating-and-registering-file-types.html#file-types-shebang
https://stackoverflow.com/questions/1523427/what-is-the-common-header-format-of-python-files
https://gist.github.com/NicolasBizzozzero/6d4ca63f8482a1af99b0ed022c13b041
https://stackoverflow.com/questions/16220930/python-what-is-a-header/27462911
https://stackoverflow.com/questions/4872007/where-does-this-come-from-coding-utf-8


**[U]**

**[V]**

**[W]**

**[X]**

**[Y]**

**[Z]**