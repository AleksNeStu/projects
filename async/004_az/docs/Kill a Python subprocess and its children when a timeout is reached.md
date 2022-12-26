---
source: https://alexandra-zaharia.github.io/posts/kill-subprocess-and-its-children-on-timeout-python/ \
created: 2022-12-26T21:35:00 (UTC +01:00) \
tags: [] \
author: Alexandra Zaharia
---
# Kill a Python subprocess and its children when a timeout is reached | Alexandra Zaharia
---
Suppose a Python script needs to launch an external command. This can be done using the [`subprocess`](https://docs.python.org/3/library/subprocess.html) module in one of two ways:

-   either use the “convenience” function `subprocess.run()`
-   or use the more flexible `Popen` interface

## Stopping a subprocess on timeout

The “convenience” function `subprocess.run()` allows to do quite a number of useful things, such as capturing output, checking the external command’s return code or setting a timeout, among others.

If we are simply interested in stopping the execution of the external command after a given timeout has been reached, it is sufficient to `subprocess.run()` the command and catch the `TimeoutExpired` exception if it is raised:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 </pre></td><td><pre><span>import</span> <span>subprocess</span>  <span>cmd</span> <span>=</span> <span>[</span><span>'/path/to/cmd'</span><span>,</span> <span>'arg1'</span><span>,</span> <span>'arg2'</span><span>]</span>  <span># the external command to run </span><span>timeout_s</span> <span>=</span> <span>10</span>  <span># how many seconds to wait  </span> <span>try</span><span>:</span>     <span>p</span> <span>=</span> <span>subprocess</span><span>.</span><span>run</span><span>(</span><span>cmd</span><span>,</span> <span>timeout</span><span>=</span><span>timeout_s</span><span>)</span> <span>except</span> <span>subprocess</span><span>.</span><span>TimeoutExpired</span><span>:</span>     <span>print</span><span>(</span><span>f</span><span>'Timeout for </span><span>{</span><span>cmd</span><span>}</span><span> (</span><span>{</span><span>timeout_s</span><span>}</span><span>s) expired'</span><span>)</span> </pre></td></tr></tbody></table>`

## Stopping a subprocess and its children on timeout

The situation gets more complicated when the external command may launch one or several child processes. In order to be able to stop the child processes as well as the parent, it is necessary to use the `Popen` constructor.

> **Note:** The following only applies to UNIX-like operating systems. (Read: it won’t work on Windows.)

The reason for using the `Popen` constructor for this scenario is that it can be instructed to launch a new _session_ for the external command. Then, the whole _process group_ belonging to the external command can be terminated on timeout. A **process group** is simply a group of processes that can be controlled at once (via [signals](https://en.wikipedia.org/wiki/Signal_(IPC))), while a **session** is a collection of process groups. Here are the official [definitions](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html), taken from the [POSIX.1-2008 standard](https://pubs.opengroup.org/onlinepubs/9699919799/):

> **3.296 Process Group** - A collection of processes that permits the signaling of related processes. Each process in the system is a member of a process group that is identified by a process group ID. A newly created process joins the process group of its creator.

> **3.343 Session** - A collection of process groups established for job control purposes. Each process group is a member of a session. A process is considered to be a member of the session of which its process group is a member. A newly created process joins the session of its creator. A process can alter its session membership; see `setsid()`. There can be multiple process groups in the same session.

### The reason for using a session instead of a process group

Reading the above definitions, one may wonder why should we bother with creating a new session instead of simply using a new process group for the external command. That’s an excellent question! It is technically possible, but not advisable. In order to create a process group, we’d need to call `os.setpgrp()` (which uses the [`setpgrp()`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/setpgrp.html) system call). However, there are two problems with this approach:

-   `setpgrp()` is marked as obsolete and may be removed in future versions (check the `man` page);
-   the only way to call `os.setpgrp()` from within the `Popen` constructor is to pass it to the `preexec_fn` parameter, which is _not_ thread-safe.

The Python documentation for [`Popen()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen) states the following:

> **Warning:** The `preexec_fn` parameter is not safe to use in the presence of threads in your application. The child process could deadlock before `exec` is called. If you must use it, keep it trivial! Minimize the number of libraries you call into.

In the note following the warning, it is mentioned that:

> The `start_new_session` parameter can take the place of a previously common use of `preexec_fn` to call `os.setsid()` in the child.

The workaround, therefore, is to simply create a new session by setting the `start_new_session` argument of the `Popen` constructor to `True`. According to the Python documentation, it is the equivalent of using `preexec_fn=os.setsid` (based on the [`setsid()`](https://pubs.opengroup.org/onlinepubs/009604599/functions/setsid.html) system call), but without the un-thread-safe warning.

### Implementation

With all the above explanations, the implementation is straight-forward:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 </pre></td><td><pre><span>import</span> <span>os</span> <span>import</span> <span>signal</span> <span>import</span> <span>subprocess</span> <span>import</span> <span>sys</span>  <span>cmd</span> <span>=</span> <span>[</span><span>'/path/to/cmd'</span><span>,</span> <span>'arg1'</span><span>,</span> <span>'arg2'</span><span>]</span>  <span># the external command to run </span><span>timeout_s</span> <span>=</span> <span>10</span>  <span># how many seconds to wait  </span> <span>try</span><span>:</span>     <span>p</span> <span>=</span> <span>subprocess</span><span>.</span><span>Popen</span><span>(</span><span>cmd</span><span>,</span> <span>start_new_session</span><span>=</span><span>True</span><span>)</span>     <span>p</span><span>.</span><span>wait</span><span>(</span><span>timeout</span><span>=</span><span>timeout_s</span><span>)</span> <span>except</span> <span>subprocess</span><span>.</span><span>TimeoutExpired</span><span>:</span>     <span>print</span><span>(</span><span>f</span><span>'Timeout for </span><span>{</span><span>cmd</span><span>}</span><span> (</span><span>{</span><span>timeout_s</span><span>}</span><span>s) expired'</span><span>,</span> <span>file</span><span>=</span><span>sys</span><span>.</span><span>stderr</span><span>)</span>     <span>print</span><span>(</span><span>'Terminating the whole process group...'</span><span>,</span> <span>file</span><span>=</span><span>sys</span><span>.</span><span>stderr</span><span>)</span>     <span>os</span><span>.</span><span>killpg</span><span>(</span><span>os</span><span>.</span><span>getpgid</span><span>(</span><span>p</span><span>.</span><span>pid</span><span>),</span> <span>signal</span><span>.</span><span>SIGTERM</span><span>)</span> </pre></td></tr></tbody></table>`

The `Popen` interface is different than that of the convenience `subprocess.run()` function. The timeout needs to be specified in `Popen.wait()`. If you want to capture `stdout` and `stderr`, you need to pass them to the `Popen` constructor as `subprocess.PIPE` and then use `Popen.communicate()`. Regardless of the differences, whatever can be done with `subprocess.run()` can also be achieved with the `Popen` constructor.

When the timeout set in `Popen.wait()` has elapsed, a `TimeoutExpired` exception is raised. Then, in line 15, we send a SIGTERM to the whole process group (`os.killpg()`) of the external command (`os.getpgid(p.pid)`).

That’s it. Happy infanticide! (Err… I was referring to child processes ![:grin:](https://github.githubassets.com/images/icons/emoji/unicode/1f601.png ":grin:"))

## Further reading

-   [`subprocess`](https://docs.python.org/3/library/subprocess.html) (Python documentation)
-   [`signal`](https://docs.python.org/3/library/signal.html) (Python documentation)
-   [Signals](https://en.wikipedia.org/wiki/Signal_(IPC)) (Wikipedia)
-   [POSIX.1-2008 standard](https://pubs.opengroup.org/onlinepubs/9699919799/)
-   [POSIX.1-2008 definitions](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html)
