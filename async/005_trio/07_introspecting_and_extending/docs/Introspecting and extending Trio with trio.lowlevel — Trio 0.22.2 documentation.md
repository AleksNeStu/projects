---
source: https://trio.readthedocs.io/en/stable/reference-lowlevel.html

created: 2023-10-24T12:14:18 (UTC +02:00)

tags: []

author: 

---

# Introspecting and extending Trio with trio.lowlevel — Trio 0.22.2 documentation
---
[`trio.lowlevel`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#module-trio.lowlevel "trio.lowlevel")
contains low-level APIs for introspecting and extending Trio. If you’re writing ordinary, everyday code, then you can
ignore this module completely. But sometimes you need something a bit lower level. Here are some examples of situations
where you should reach
for [`trio.lowlevel`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#module-trio.lowlevel "trio.lowlevel"):

- You want to implement a
  new [synchronization primitive](https://trio.readthedocs.io/en/stable/reference-core.html#synchronization) that Trio
  doesn’t (yet) provide, like a reader-writer lock.

- You want to extract low-level metrics to monitor the health of your application.

- You want to use a low-level operating system interface that Trio doesn’t (yet) provide its own wrappers for, like
  watching a filesystem directory for changes.

- You want to implement an interface for calling between Trio and another event loop within the same process.

- You’re writing a debugger and want to visualize Trio’s task tree.

- You need to interoperate with a C library whose API exposes raw file descriptors.

You don’t need to be scared
of [`trio.lowlevel`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#module-trio.lowlevel "trio.lowlevel"),
as long as you take proper precautions. These are real public APIs, with strictly defined and carefully documented
semantics. They’re the same tools we use to implement all the nice high-level APIs in
the [`trio`](https://trio.readthedocs.io/en/stable/reference-core.html#module-trio "trio") namespace. But, be careful.
Some of those strict semantics have [nasty big pointy teeth](https://en.wikipedia.org/wiki/Rabbit_of_Caerbannog). If you
make a mistake, Trio may not be able to handle it gracefully; conventions and guarantees that are followed strictly in
the rest of Trio do not always apply. When you use this module, it’s your job to think about how you’re going to handle
the tricky cases so you can expose a friendly Trio-style API to your users.

## Debugging and instrumentation[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#debugging-and-instrumentation "Permalink to this heading")

Trio tries hard to provide useful hooks for debugging and instrumentation. Some are documented above (the nursery
introspection
attributes, [`trio.Lock.statistics()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.Lock.statistics "trio.Lock.statistics"),
etc.). Here are some more.

### Global statistics[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#global-statistics "Permalink to this heading")

trio.lowlevel.current\_statistics()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.current_statistics "Permalink to this definition")

Returns an object containing run-loop-level debugging information.

Currently the following fields are defined:

- `tasks_living` (int): The number of tasks that have been spawned and not yet exited.

- `tasks_runnable` (int): The number of tasks that are currently queued on the run queue (as opposed to blocked waiting
  for something to happen).

- `seconds_to_next_deadline` (float): The time until the next pending cancel scope deadline. May be negative if the
  deadline has expired but we haven’t yet processed cancellations. May
  be [`inf`](https://docs.python.org/3/library/math.html#math.inf "(in Python v3.11)") if there are no pending
  deadlines.

- `run_sync_soon_queue_size` (int): The number of unprocessed callbacks queued
  via [`trio.lowlevel.TrioToken.run_sync_soon()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.TrioToken.run_sync_soon "trio.lowlevel.TrioToken.run_sync_soon").

- `io_statistics` (object): Some statistics from Trio’s I/O backend. This always has an attribute `backend` which is a
  string naming which operating-system-specific I/O backend is in use; the other attributes vary between backends.

### The current clock[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#the-current-clock "Permalink to this heading")

trio.lowlevel.current\_clock()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.current_clock "Permalink to this definition")

Returns the
current [`Clock`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.abc.Clock "trio.abc.Clock").

### Instrument API[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#instrument-api "Permalink to this heading")

The instrument API provides a standard way to add custom instrumentation to the run loop. Want to make a histogram of
scheduling latencies, log a stack trace of any task that blocks the run loop for >50 ms, or measure what percentage of
your process’s running time is spent waiting for I/O? This is the place.

The general idea is that at any given
moment, [`trio.run()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run") maintains a set of
“instruments”, which are objects that implement
the [`trio.abc.Instrument`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument "trio.abc.Instrument")
interface. When an interesting event happens, it loops over these instruments and notifies them by calling an
appropriate method. The tutorial
has [a simple example of using this for tracing](https://trio.readthedocs.io/en/stable/tutorial.html#tutorial-instrument-example).

Since this hooks into Trio at a rather low level, you do have to be careful. The callbacks are run synchronously, and in
many cases if they error out then there isn’t any plausible way to propagate this exception (for instance, we might be
deep in the guts of the exception propagation machinery…). Therefore
our [current strategy](https://github.com/python-trio/trio/issues/47) for handling exceptions raised by instruments is
to (a) log an exception to the `"trio.abc.Instrument"` logger, which by default prints a stack trace to standard error
and (b) disable the offending instrument.

You can register an initial list of instruments by passing them
to [`trio.run()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run"). [`add_instrument()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.add_instrument "trio.lowlevel.add_instrument")
and [`remove_instrument()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.remove_instrument "trio.lowlevel.remove_instrument")
let you add and remove instruments at runtime.

trio.lowlevel.add\_instrument(
_instrument: [Instrument](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument "trio.abc.Instrument")_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.add_instrument "Permalink to this definition")

Start instrumenting the current run loop with the given instrument.

Parameters:

**instrument** ([
_trio.abc.Instrument_](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument "trio.abc.Instrument")) –
The instrument to activate.

If `instrument` is already active, does nothing.

trio.lowlevel.remove\_instrument(
_instrument: [Instrument](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument "trio.abc.Instrument")_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.remove_instrument "Permalink to this definition")

Stop instrumenting the current run loop with the given instrument.

Parameters:

**instrument** ([
_trio.abc.Instrument_](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument "trio.abc.Instrument")) –
The instrument to de-activate.

Raises:

[**KeyError**](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.11)") – if the instrument is
not currently active. This could occur either because you never added it, or because you added it and then it raised an
unhandled exception and was automatically deactivated.

And here’s the interface to implement if you want to build your
own [`Instrument`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument "trio.abc.Instrument"):

_class_
trio.abc.Instrument[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument "Permalink to this definition")

The interface for run loop instrumentation.

Instruments don’t have to inherit from this abstract base class, and all of these methods are optional. This class
serves mostly as documentation.

after\_io\_wait(
_timeout_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument.after_io_wait "Permalink to this definition")

Called after handling pending I/O.

Parameters:

**timeout** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – The number of
seconds we were willing to wait. This much time may or may not have elapsed, depending on whether any I/O was ready.

after\_run()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument.after_run "Permalink to this definition")

Called just before [`trio.run()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run")
returns.

after\_task\_step(
_task_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument.after_task_step "Permalink to this definition")

Called when we return to the main run loop after a task has yielded.

Parameters:

**task** ([
_trio.lowlevel.Task_](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")) –
The task that just ran.

before\_io\_wait(
_timeout_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument.before_io_wait "Permalink to this definition")

Called before blocking to wait for I/O readiness.

Parameters:

**timeout** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – The number of
seconds we are willing to wait.

before\_run()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument.before_run "Permalink to this definition")

Called at the beginning
of [`trio.run()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run").

before\_task\_step(
_task_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument.before_task_step "Permalink to this definition")

Called immediately before we resume running the given task.

Parameters:

**task** ([
_trio.lowlevel.Task_](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")) –
The task that is about to run.

task\_exited(
_task_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument.task_exited "Permalink to this definition")

Called when the given task exits.

Parameters:

**task** ([
_trio.lowlevel.Task_](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")) –
The finished task.

task\_scheduled(
_task_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument.task_scheduled "Permalink to this definition")

Called when the given task becomes runnable.

It may still be some time before it actually runs, if there are other runnable tasks ahead of it.

Parameters:

**task** ([
_trio.lowlevel.Task_](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")) –
The task that became runnable.

task\_spawned(
_task_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.abc.Instrument.task_spawned "Permalink to this definition")

Called when the given task is created.

Parameters:

**task** ([
_trio.lowlevel.Task_](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")) –
The new task.

The tutorial has
a [fully-worked example](https://trio.readthedocs.io/en/stable/tutorial.html#tutorial-instrument-example) of defining a
custom instrument to log Trio’s internal scheduling decisions.

## Low-level process spawning[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#low-level-process-spawning "Permalink to this heading")

_await_ trio.lowlevel.open\_process(_command_, _\*_, _stdin\=None_, _stdout\=None_, _stderr\=None_,
_\*\*options_) → [Process](https://trio.readthedocs.io/en/stable/reference-io.html#trio.Process "trio.Process")[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.open_process "Permalink to this definition")

Execute a child program in a new process.

After construction, you can interact with the child process by writing data to
its [`stdin`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.Process.stdin "trio.Process.stdin") stream (
a [`SendStream`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.abc.SendStream "trio.abc.SendStream")),
reading data from
its [`stdout`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.Process.stdout "trio.Process.stdout")
and/or [`stderr`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.Process.stderr "trio.Process.stderr")
streams (
both [`ReceiveStream`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.abc.ReceiveStream "trio.abc.ReceiveStream")
s), sending it signals
using [`terminate`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.Process.terminate "trio.Process.terminate"), [`kill`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.Process.kill "trio.Process.kill"),
or [`send_signal`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.Process.send_signal "trio.Process.send_signal"),
and waiting for it to exit
using [`wait`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.Process.wait "trio.Process.wait").
See [`trio.Process`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.Process "trio.Process") for details.

Each standard stream is only available if you specify that a pipe should be created for it. For example, if you
pass `stdin=subprocess.PIPE`, you can write to
the [`stdin`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.Process.stdin "trio.Process.stdin") stream,
else [`stdin`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.Process.stdin "trio.Process.stdin") will
be `None`.

Unlike [`trio.run_process`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.run_process "trio.run_process"),
this function doesn’t do any kind of automatic management of the child process. It’s up to you to implement whatever
semantics you want.

Parameters:

- **command** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)") _or_ [
  _str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – The command to run. Typically this
  is a sequence of strings such as `['ls', '-l', 'directory with spaces']`, where the first element names the executable
  to invoke and the other elements specify its arguments. With `shell=True` in the `**options`, or on Windows, `command`
  may alternatively be a string, which will be parsed following
  platform-dependent [quoting rules](https://trio.readthedocs.io/en/stable/reference-io.html#subprocess-quoting).

- **stdin** – Specifies what the child process’s standard input stream should connect to: output written by the
  parent (`subprocess.PIPE`), nothing (`subprocess.DEVNULL`), or an open file (pass a file descriptor or something
  whose `fileno` method returns one). If `stdin` is unspecified, the child process will have the same standard input
  stream as its parent.

- **stdout** – Like `stdin`, but for the child process’s standard output stream.

- **stderr** – Like `stdin`, but for the child process’s standard error stream. An additional value `subprocess.STDOUT`
  is supported, which causes the child’s standard output and standard error messages to be intermixed on a single
  standard output stream, attached to whatever the `stdout` option says to attach it to.

- **\*\*options** –
  Other [general subprocess options](https://trio.readthedocs.io/en/stable/reference-io.html#subprocess-options) are
  also accepted.

Returns:

A new [`trio.Process`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.Process "trio.Process") object.

Raises:

[**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "(in Python v3.11)") – if the process spawning
fails, for example because the specified command could not be found.

## Low-level I/O primitives[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#low-level-i-o-primitives "Permalink to this heading")

Different environments expose different low-level APIs for performing async
I/O. [`trio.lowlevel`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#module-trio.lowlevel "trio.lowlevel")
exposes these APIs in a relatively direct way, so as to allow maximum power and flexibility for higher level code.
However, this means that the exact API provided may vary depending on what system Trio is running on.

### Universally available API[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#universally-available-api "Permalink to this heading")

All environments provide the following functions:

_await_ trio.lowlevel.wait\_readable(
_obj_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_readable "Permalink to this definition")

Block until the kernel reports that the given object is readable.

On Unix systems, `obj` must either be an integer file descriptor, or else an object with a `.fileno()` method which
returns an integer file descriptor. Any kind of file descriptor can be passed, though the exact semantics will depend on
your kernel. For example, this probably won’t do anything useful for on-disk files.

On Windows systems, `obj` must either be an integer `SOCKET` handle, or else an object with a `.fileno()` method which
returns an integer `SOCKET` handle. File descriptors aren’t supported, and neither are handles that refer to anything
besides a `SOCKET`.

Raises:

- [**trio.BusyResourceError
  **](https://trio.readthedocs.io/en/stable/reference-core.html#trio.BusyResourceError "trio.BusyResourceError") – if
  another task is already waiting for the given socket to become readable.

- [**trio.ClosedResourceError
  **](https://trio.readthedocs.io/en/stable/reference-core.html#trio.ClosedResourceError "trio.ClosedResourceError") –
  if another task
  calls [`notify_closing()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.notify_closing "trio.lowlevel.notify_closing")
  while this function is still working.

_await_ trio.lowlevel.wait\_writable(
_obj_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_writable "Permalink to this definition")

Block until the kernel reports that the given object is writable.

See [`wait_readable`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_readable "trio.lowlevel.wait_readable")
for the definition of `obj`.

Raises:

- [**trio.BusyResourceError
  **](https://trio.readthedocs.io/en/stable/reference-core.html#trio.BusyResourceError "trio.BusyResourceError") – if
  another task is already waiting for the given socket to become writable.

- [**trio.ClosedResourceError
  **](https://trio.readthedocs.io/en/stable/reference-core.html#trio.ClosedResourceError "trio.ClosedResourceError") –
  if another task
  calls [`notify_closing()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.notify_closing "trio.lowlevel.notify_closing")
  while this function is still working.

trio.lowlevel.notify\_closing(
_obj_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.notify_closing "Permalink to this definition")

Call this before closing a file descriptor (on Unix) or socket (on Windows). This will cause
any [`wait_readable`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_readable "trio.lowlevel.wait_readable")
or [`wait_writable`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_writable "trio.lowlevel.wait_writable")
calls on the given object to immediately wake up and
raise [`ClosedResourceError`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.ClosedResourceError "trio.ClosedResourceError").

This doesn’t actually close the object – you still have to do that yourself afterwards. Also, you want to be careful to
make sure no new tasks start waiting on the object in between when you call this and when it’s actually closed. So to
close something properly, you usually want to do these steps in order:

1. Explicitly mark the object as closed, so that any new attempts to use it will abort before they start.

2.

Call [`notify_closing`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.notify_closing "trio.lowlevel.notify_closing")
to wake up any already-existing users.

3. Actually close the object.

It’s also possible to do them in a different order if that’s more convenient, _but only if_ you make sure not to have
any checkpoints in between the steps. This way they all happen in a single atomic step, so other tasks won’t be able to
tell what order they happened in anyway.

### Unix-specific API[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#unix-specific-api "Permalink to this heading")

[`FdStream`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.FdStream "trio.lowlevel.FdStream")
supports wrapping Unix files (such as a pipe or TTY) as a stream.

If you have two different file descriptors for sending and receiving, and want to bundle them together into a single
bidirectional [`Stream`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.abc.Stream "trio.abc.Stream"),
then
use [`trio.StapledStream`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.StapledStream "trio.StapledStream"):

```
bidirectional_stream = trio.StapledStream(
    trio.lowlevel.FdStream(write_fd),
    trio.lowlevel.FdStream(read_fd)
)

```

_class_ trio.lowlevel.FdStream(
_fd: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.FdStream "Permalink to this definition")

Bases: [`Stream`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.abc.Stream "trio.abc.Stream")

Represents a stream given the file descriptor to a pipe, TTY, etc.

_fd_ must refer to a file that is open for reading and/or writing and supports non-blocking I/O (pipes and TTYs will
work, on-disk files probably not). The returned stream takes ownership of the fd, so closing the stream will close the
fd too. As with [`os.fdopen`](https://docs.python.org/3/library/os.html#os.fdopen "(in Python v3.11)"), you should not
directly use an fd after you have wrapped it in a stream using this function.

To be used as a Trio stream, an open file must be placed in non-blocking mode. Unfortunately, this impacts all I/O that
goes through the underlying open file, including I/O that uses a different file descriptor than the one that was passed
to Trio. If other threads or processes are using file descriptors that are related
through [`os.dup`](https://docs.python.org/3/library/os.html#os.dup "(in Python v3.11)") or inheritance
across [`os.fork`](https://docs.python.org/3/library/os.html#os.fork "(in Python v3.11)") to the one that Trio is using,
they are unlikely to be prepared to have non-blocking I/O semantics suddenly thrust upon them. For example, you can
use `FdStream(os.dup(sys.stdin.fileno()))` to obtain a stream for reading from standard input, but it is only safe to do
so with heavy caveats: your stdin must not be shared by any other processes, and you must not make any calls to
synchronous methods of [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "(in Python v3.11)") until the
stream returned
by [`FdStream`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.FdStream "trio.lowlevel.FdStream")
is closed. See [issue #174](https://github.com/python-trio/trio/issues/174) for a discussion of the challenges involved
in relaxing this restriction.

Parameters:

**fd** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – The fd to be wrapped.

Returns:

A
new [`FdStream`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.FdStream "trio.lowlevel.FdStream")
object.

### Kqueue-specific API[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#kqueue-specific-api "Permalink to this heading")

TODO: these are implemented, but are currently more of a sketch than anything real.
See [#26](https://github.com/python-trio/trio/issues/26).

trio.lowlevel.current\_kqueue()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.current_kqueue "Permalink to this definition")

_await_ trio.lowlevel.wait\_kevent(_ident_, _filter_,
_abort\_func_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_kevent "Permalink to this definition")

_with_ trio.lowlevel.monitor\_kevent(_ident_, _filter_)_as
queue_[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.monitor_kevent "Permalink to this definition")

### Windows-specific API[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#windows-specific-api "Permalink to this heading")

_await_ trio.lowlevel.WaitForSingleObject(
_handle_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.WaitForSingleObject "Permalink to this definition")

Async and cancellable variant
of [WaitForSingleObject](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687032(v=vs.85).aspx). Windows only.

Parameters:

**handle** – A Win32 object handle, as a Python integer.

Raises:

[**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "(in Python v3.11)") – If the handle is invalid,
e.g. when it is already closed.

TODO: these are implemented, but are currently more of a sketch than anything real.
See [#26](https://github.com/python-trio/trio/issues/26) and [#52](https://github.com/python-trio/trio/issues/52).

trio.lowlevel.register\_with\_iocp(
_handle_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.register_with_iocp "Permalink to this definition")

_await_ trio.lowlevel.wait\_overlapped(_handle_,
_lpOverlapped_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_overlapped "Permalink to this definition")

trio.lowlevel.current\_iocp()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.current_iocp "Permalink to this definition")

_with_ trio.lowlevel.monitor\_completion\_key()_as
queue_[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.monitor_completion_key "Permalink to this definition")

## Global state: system tasks and run-local variables[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#global-state-system-tasks-and-run-local-variables "Permalink to this heading")

_class_ trio.lowlevel.RunVar(_name_,
_default=<object object>_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.RunVar "Permalink to this definition")

The run-local variant of a context variable.

[`RunVar`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.RunVar "trio.lowlevel.RunVar")
objects are similar to context variable objects, except that they are shared across a single call
to [`trio.run()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run") rather than a single
task.

trio.lowlevel.spawn\_system\_task(_async\_fn_, _\*args_, _name\=None_,
_context\=None_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.spawn_system_task "Permalink to this definition")

Spawn a “system” task.

System tasks have a few differences from regular tasks:

- They don’t need an explicit nursery; instead they go into the internal “system nursery”.

- If a system task raises an exception, then it’s converted into
  a [`TrioInternalError`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.TrioInternalError "trio.TrioInternalError")
  and _all_ tasks are cancelled. If you write a system task, you should be careful to make sure it doesn’t crash.

- System tasks are automatically cancelled when the main task exits.

- By default, system tasks
  have [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)")
  protection _enabled_. If you want your task to be interruptible by control-C, then you need to
  use [`disable_ki_protection()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.disable_ki_protection "trio.lowlevel.disable_ki_protection")
  explicitly (and come up with some plan for what to do with
  a [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)"),
  given that system tasks aren’t allowed to raise exceptions).

- System tasks do not inherit context variables from their creator.

Towards the end of a call
to [`trio.run()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run"), after the main task
and all system tasks have exited, the system nursery becomes closed. At this point, new calls
to [`spawn_system_task()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.spawn_system_task "trio.lowlevel.spawn_system_task")
will raise `RuntimeError("Nursery is closed to new arrivals")` instead of creating a system task. It’s possible to
encounter this state either in a `finally` block in an async generator, or in a callback passed
to [`TrioToken.run_sync_soon()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.TrioToken.run_sync_soon "trio.lowlevel.TrioToken.run_sync_soon")
at the right moment.

Parameters:

- **async\_fn** – An async callable.

- **args** – Positional arguments for `async_fn`. If you want to pass keyword arguments,
  use [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "(in Python v3.11)").

- **name** – The name for this task. Only used for debugging/introspection (e.g. `repr(task_obj)`). If this isn’t a
  string, [`spawn_system_task()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.spawn_system_task "trio.lowlevel.spawn_system_task")
  will try to make it one. A common use case is if you’re wrapping a function before spawning a new task, you might pass
  the original function as the `name=` to make debugging easier.

- **context** – An optional `contextvars.Context` object with context variables to use for this task. You would normally
  get a copy of the current context with `context = contextvars.copy_context()` and then you would pass that `context`
  object here.

Returns:

the newly spawned task

Return type:

[Task](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")

## Trio tokens[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio-tokens "Permalink to this heading")

_class_
trio.lowlevel.TrioToken[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.TrioToken "Permalink to this definition")

An opaque object representing a single call
to [`trio.run()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run").

It has no public constructor; instead,
see [`current_trio_token()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.current_trio_token "trio.lowlevel.current_trio_token").

This object has two uses:

1. It lets you re-enter the Trio run loop from external threads or signal handlers. This is the low-level primitive
   that [`trio.to_thread()`](https://trio.readthedocs.io/en/stable/reference-core.html#module-trio.to_thread "trio.to_thread")
   and [`trio.from_thread`](https://trio.readthedocs.io/en/stable/reference-core.html#module-trio.from_thread "trio.from_thread")
   use to communicate with worker threads,
   that [`trio.open_signal_receiver`](https://trio.readthedocs.io/en/stable/reference-io.html#trio.open_signal_receiver "trio.open_signal_receiver")
   uses to receive notifications about signals, and so forth.

2. Each call to [`trio.run()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run") has
   exactly one
   associated [`TrioToken`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.TrioToken "trio.lowlevel.TrioToken")
   object, so you can use it to identify a particular call.

run\_sync\_soon(_sync\_fn_, _\*args_,
_idempotent\=False_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.TrioToken.run_sync_soon "Permalink to this definition")

Schedule a call to `sync_fn(*args)` to occur in the context of a Trio task.

This is safe to call from the main thread, from other threads, and from signal handlers. This is the fundamental
primitive used to re-enter the Trio run loop from outside of it.

The call will happen “soon”, but there’s no guarantee about exactly when, and no mechanism provided for finding out when
it’s happened. If you need this, you’ll have to build your own.

The call is effectively run as part of a system task (
see [`spawn_system_task()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.spawn_system_task "trio.lowlevel.spawn_system_task")).
In particular this means that:

- [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)")
  protection is _enabled_ by default; if you want `sync_fn` to be interruptible by control-C, then you need to
  use [`disable_ki_protection()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.disable_ki_protection "trio.lowlevel.disable_ki_protection")
  explicitly.

- If `sync_fn` raises an exception, then it’s converted into
  a [`TrioInternalError`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.TrioInternalError "trio.TrioInternalError")
  and _all_ tasks are cancelled. You should be careful that `sync_fn` doesn’t crash.

All calls with `idempotent=False` are processed in strict first-in first-out order.

If `idempotent=True`, then `sync_fn` and `args` must be hashable, and Trio will make a best-effort attempt to discard
any call submission which is equal to an already-pending call. Trio will process these in first-in first-out order.

Any ordering guarantees apply separately to `idempotent=False` and `idempotent=True` calls; there’s no rule for how
calls in the different categories are ordered with respect to each other.

Raises:

[**trio.RunFinishedError
**](https://trio.readthedocs.io/en/stable/reference-core.html#trio.RunFinishedError "trio.RunFinishedError") – if the
associated call to [`trio.run()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run") has
already exited. (Any call that _doesn’t_ raise this error is guaranteed to be fully processed
before [`trio.run()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run") exits.)

trio.lowlevel.current\_trio\_token()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.current_trio_token "Permalink to this definition")

Retrieve
the [`TrioToken`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.TrioToken "trio.lowlevel.TrioToken")
for the current call to [`trio.run()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run").

## Spawning threads[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#spawning-threads "Permalink to this heading")

trio.lowlevel.start\_thread\_soon(_fn_, _deliver_,
_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)") \=
None_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.start_thread_soon "Permalink to this definition")

Runs `deliver(outcome.capture(fn))` in a worker thread.

Generally `fn` does some blocking work, and `deliver` delivers the result back to whoever is interested.

This is a low-level, no-frills interface, very similar to
using [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "(in Python v3.11)") to
spawn a thread directly. The main difference is that this function tries to re-use threads when possible, so it can be a
bit faster
than [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "(in Python v3.11)").

Worker threads have
the [`daemon`](https://docs.python.org/3/library/threading.html#threading.Thread.daemon "(in Python v3.11)") flag set,
which means that if your main thread exits, worker threads will automatically be killed. If you want to make sure that
your `fn` runs to completion, then you should make sure that the main thread remains alive until `deliver` is called.

It is safe to call this function simultaneously from multiple threads.

Parameters:

- **fn** (_sync function_) – Performs arbitrary blocking work.

- **deliver** (_sync function_) – Takes
  the [`outcome.Outcome`](https://outcome.readthedocs.io/en/latest/api.html#outcome.Outcome "(in outcome v1.2.0+dev)")
  of `fn`, and delivers it. _Must not block._

Because worker threads are cached and reused for multiple calls, neither function should mutate thread-level state,
like [`threading.local`](https://docs.python.org/3/library/threading.html#threading.local "(in Python v3.11)") objects –
or if they do, they should be careful to revert their changes before returning.

Note

The split between `fn` and `deliver` serves two purposes. First, it’s convenient, since most callers need something like
this anyway.

Second, it avoids a small race condition that could cause too many threads to be spawned. Consider a program that wants
to run several jobs sequentially on a thread, so the main thread submits a job, waits for it to finish, submits another
job, etc. In theory, this program should only need one worker thread. But what could happen is:

1. Worker thread: First job finishes, and calls `deliver`.

2. Main thread: receives notification that the job finished, and calls `start_thread_soon`.

3. Main thread: sees that no worker threads are marked idle, so spawns a second worker thread.

4. Original worker thread: marks itself as idle.

To avoid this, threads mark themselves as idle _before_ calling `deliver`.

Is this potential extra thread a major problem? Maybe not, but it’s easy enough to avoid, and we figure that if the user
is trying to limit how many threads they’re using then it’s polite to respect that.

## Safer KeyboardInterrupt handling[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#safer-keyboardinterrupt-handling "Permalink to this heading")

Trio’s handling of control-C is designed to balance usability and safety. On the one hand, there are sensitive regions (
like the core scheduling loop) where it’s simply impossible to handle
arbitrary [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)")
exceptions while maintaining our core correctness invariants. On the other, if the user accidentally writes an infinite
loop, we do want to be able to break out of that. Our solution is to install a default signal handler which checks
whether it’s safe to
raise [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)") at
the place where the signal is received. If so, then we do; otherwise, we schedule
a [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)") to be
delivered to the main task at the next available opportunity (similar to
how [`Cancelled`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.Cancelled "trio.Cancelled") is
delivered).

So that’s great, but – how do we know whether we’re in one of the sensitive parts of the program or not?

This is determined on a function-by-function basis. By default:

- The top-level function in regular user tasks is unprotected.

- The top-level function in system tasks is protected.

- If a function doesn’t specify otherwise, then it inherits the protection state of its caller.

This means you only need to override the defaults at places where you transition from protected code to unprotected code
or vice-versa.

These transitions are accomplished using two function decorators:

@trio.lowlevel.disable\_ki\_protection[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.disable_ki_protection "Permalink to this definition")

Decorator that marks the given regular function, generator function, async function, or async generator function as
unprotected
against [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)"),
i.e., the code inside this function _can_ be rudely interrupted
by [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)") at any
moment.

If you have multiple decorators on the same function, then this should be at the bottom of the stack (closest to the
actual function).

An example of where you’d use this is in implementing something
like [`trio.from_thread.run()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.from_thread.run "trio.from_thread.run"),
which
uses [`TrioToken.run_sync_soon()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.TrioToken.run_sync_soon "trio.lowlevel.TrioToken.run_sync_soon")
to get into the Trio
thread. [`run_sync_soon()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.TrioToken.run_sync_soon "trio.lowlevel.TrioToken.run_sync_soon")
callbacks are run
with [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)")
protection enabled,
and [`trio.from_thread.run()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.from_thread.run "trio.from_thread.run")
takes advantage of this to safely set up the machinery for sending a response back to the original thread, but then
uses [`disable_ki_protection()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.disable_ki_protection "trio.lowlevel.disable_ki_protection")
when entering the user-provided function.

@trio.lowlevel.enable\_ki\_protection[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.enable_ki_protection "Permalink to this definition")

Decorator that marks the given regular function, generator function, async function, or async generator function as
protected
against [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)"),
i.e., the code inside this function _won’t_ be rudely interrupted
by [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)"). (
Though if it contains any [checkpoints](https://trio.readthedocs.io/en/stable/reference-core.html#checkpoints), then it
can still
receive [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)")
at those. This is considered a polite interruption.)

Warning

Be very careful to only use this decorator on functions that you know will either exit in bounded time, or else pass
through a checkpoint regularly. (Of course all of your functions should have this property, but if you mess it up here
then you won’t even be able to use control-C to escape!)

If you have multiple decorators on the same function, then this should be at the bottom of the stack (closest to the
actual function).

An example of where you’d use this is on the `__exit__` implementation for something like
a [`Lock`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.Lock "trio.Lock"), where a
poorly-timed [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)")
could leave the lock in an inconsistent state and cause a deadlock.

trio.lowlevel.currently\_ki\_protected()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.currently_ki_protected "Permalink to this definition")

Check whether the calling code
has [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)")
protection enabled.

It’s surprisingly easy to think that
one’s [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)")
protection is enabled when it isn’t, or vice-versa. This function tells you what Trio thinks of the matter, which makes
it useful for `assert`s and unit tests.

Returns:

True if protection is enabled, and False otherwise.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")

## Sleeping and waking[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#sleeping-and-waking "Permalink to this heading")

### Wait queue abstraction[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#wait-queue-abstraction "Permalink to this heading")

_class_
trio.lowlevel.ParkingLot[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot "Permalink to this definition")

A fair wait queue with cancellation and requeueing.

This class encapsulates the tricky parts of implementing a wait queue. It’s useful for implementing higher-level
synchronization primitives like queues and locks.

In addition to the methods below, you can use `len(parking_lot)` to get the number of parked tasks,
and `if parking_lot: ...` to check whether there are any parked tasks.

_await_
park()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot.park "Permalink to this definition")

Park the current task until woken by a call
to [`unpark()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot.unpark "trio.lowlevel.ParkingLot.unpark")
or [`unpark_all()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot.unpark_all "trio.lowlevel.ParkingLot.unpark_all").

repark(_new\_lot_, _\*_,
_count\=1_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot.repark "Permalink to this definition")

Move parked tasks from
one [`ParkingLot`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot "trio.lowlevel.ParkingLot")
object to another.

This dequeues `count` tasks from one lot, and requeues them on another, preserving order. For example:

```
async def parker(lot):
    print("sleeping")
    await lot.park()
    print("woken")

async def main():
    lot1 = trio.lowlevel.ParkingLot()
    lot2 = trio.lowlevel.ParkingLot()
    async with trio.open_nursery() as nursery:
        nursery.start_soon(parker, lot1)
        await trio.testing.wait_all_tasks_blocked()
        assert len(lot1) == 1
        assert len(lot2) == 0
        lot1.repark(lot2)
        assert len(lot1) == 0
        assert len(lot2) == 1
        # This wakes up the task that was originally parked in lot1
        lot2.unpark()

```

If there are fewer than `count` tasks parked, then reparks as many tasks as are available and then returns successfully.

Parameters:

- **new\_lot** ([
  _ParkingLot_](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot "trio.lowlevel.ParkingLot")) –
  the parking lot to move tasks to.

- **count** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – the number of tasks to
  move.

repark\_all(
_new\_lot_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot.repark_all "Permalink to this definition")

Move all parked tasks from
one [`ParkingLot`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot "trio.lowlevel.ParkingLot")
object to another.

See [`repark()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot.repark "trio.lowlevel.ParkingLot.repark")
for details.

statistics()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot.statistics "Permalink to this definition")

Return an object containing debugging information.

Currently the following fields are defined:

- `tasks_waiting`: The number of tasks blocked on this
  lot’s [`park()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot.park "trio.lowlevel.ParkingLot.park")
  method.

unpark(_\*_,
_count\=1_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot.unpark "Permalink to this definition")

Unpark one or more tasks.

This wakes up `count` tasks that are blocked
in [`park()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot.park "trio.lowlevel.ParkingLot.park").
If there are fewer than `count` tasks parked, then wakes as many tasks are available and then returns successfully.

Parameters:

**count** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – the number of tasks to
unpark.

unpark\_all()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot.unpark_all "Permalink to this definition")

Unpark all parked tasks.

### Low-level checkpoint functions[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#low-level-checkpoint-functions "Permalink to this heading")

_await_
trio.lowlevel.checkpoint()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.checkpoint "Permalink to this definition")

A pure [checkpoint](https://trio.readthedocs.io/en/stable/reference-core.html#checkpoints).

This checks for cancellation and allows other tasks to be scheduled, without otherwise blocking.

Note that the scheduler has the option of ignoring this and continuing to run the current task if it decides this is
appropriate (e.g. for increased efficiency).

Equivalent to `await trio.sleep(0)` (which is implemented by
calling [`checkpoint()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.checkpoint "trio.lowlevel.checkpoint").)

The next two functions are used _together_ to make up a checkpoint:

_await_
trio.lowlevel.checkpoint\_if\_cancelled()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.checkpoint_if_cancelled "Permalink to this definition")

Issue a [checkpoint](https://trio.readthedocs.io/en/stable/reference-core.html#checkpoints) if the calling context has
been cancelled.

Equivalent to (but potentially more efficient than):

```
if trio.current_effective_deadline() == -inf:
    await trio.lowlevel.checkpoint()

```

This is either a no-op, or else it allow other tasks to be scheduled and then
raises [`trio.Cancelled`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.Cancelled "trio.Cancelled").

Typically used together
with [`cancel_shielded_checkpoint()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.cancel_shielded_checkpoint "trio.lowlevel.cancel_shielded_checkpoint").

_await_
trio.lowlevel.cancel\_shielded\_checkpoint()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.cancel_shielded_checkpoint "Permalink to this definition")

Introduce a schedule point, but not a cancel point.

This is _not_ a [checkpoint](https://trio.readthedocs.io/en/stable/reference-core.html#checkpoints), but it is half of a
checkpoint, and when combined
with [`checkpoint_if_cancelled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.checkpoint_if_cancelled "trio.lowlevel.checkpoint_if_cancelled")
it can make a full checkpoint.

Equivalent to (but potentially more efficient than):

```
with trio.CancelScope(shield=True):
    await trio.lowlevel.checkpoint()

```

These are commonly used in cases where you have an operation that might-or-might-not block, and you want to implement
Trio’s standard checkpoint semantics. Example:

```
async def operation_that_maybe_blocks():
    await checkpoint_if_cancelled()
    try:
        ret = attempt_operation()
    except BlockingIOError:
        # need to block and then retry, which we do below
        pass
    else:
        # operation succeeded, finish the checkpoint then return
        await cancel_shielded_checkpoint()
        return ret
    while True:
        await wait_for_operation_to_be_ready()
        try:
            return attempt_operation()
        except BlockingIOError:
            pass

```

This logic is a bit convoluted, but accomplishes all of the following:

- Every successful execution path passes through a checkpoint (assuming that `wait_for_operation_to_be_ready` is an
  unconditional checkpoint)

- Our [cancellation semantics](https://trio.readthedocs.io/en/stable/reference-core.html#cancellable-primitives) say
  that [`Cancelled`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.Cancelled "trio.Cancelled") should
  only be raised if the operation didn’t happen.
  Using [`cancel_shielded_checkpoint()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.cancel_shielded_checkpoint "trio.lowlevel.cancel_shielded_checkpoint")
  on the early-exit branch accomplishes this.

- On the path where we do end up blocking, we don’t pass through any schedule points before that, which avoids some
  unnecessary work.

- Avoids implicitly chaining
  the [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "(in Python v3.11)") with
  any errors raised by `attempt_operation` or `wait_for_operation_to_be_ready`, by keeping the `while True:` loop
  outside of the `except BlockingIOError:` block.

These functions can also be useful in other situations. For example,
when [`trio.to_thread.run_sync()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.to_thread.run_sync "trio.to_thread.run_sync")
schedules some work to run in a worker thread, it blocks until the work is finished (so it’s a schedule point), but by
default it doesn’t allow cancellation. So to make sure that the call always acts as a checkpoint, it
calls [`checkpoint_if_cancelled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.checkpoint_if_cancelled "trio.lowlevel.checkpoint_if_cancelled")
before starting the thread.

### Low-level blocking[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#low-level-blocking "Permalink to this heading")

_await_ trio.lowlevel.wait\_task\_rescheduled(
_abort\_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.11)")\[\[[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.11)")\[\[\], [NoReturn](https://docs.python.org/3/library/typing.html#typing.NoReturn "(in Python v3.11)")\]\], [Abort](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Abort "trio.lowlevel.Abort")\]_) → [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_task_rescheduled "Permalink to this definition")

Put the current task to sleep, with cancellation support.

This is the lowest-level API for blocking in Trio. Every time
a [`Task`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")
blocks, it does so by calling this function (usually indirectly via some higher-level API).

This is a tricky interface with no guard rails. If you can
use [`ParkingLot`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot "trio.lowlevel.ParkingLot")
or the built-in I/O wait functions instead, then you should.

Generally the way it works is that before calling this function, you make arrangements for “someone” to
call [`reschedule()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.reschedule "trio.lowlevel.reschedule")
on the current task at some later point.

Then you
call [`wait_task_rescheduled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_task_rescheduled "trio.lowlevel.wait_task_rescheduled"),
passing in `abort_func`, an “abort callback”.

(Terminology: in Trio, “aborting” is the process of attempting to interrupt a blocked task to deliver a cancellation.)

There are two possibilities for what happens next:

1. “Someone”
   calls [`reschedule()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.reschedule "trio.lowlevel.reschedule")
   on the current task,
   and [`wait_task_rescheduled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_task_rescheduled "trio.lowlevel.wait_task_rescheduled")
   returns or raises whatever value or error was passed
   to [`reschedule()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.reschedule "trio.lowlevel.reschedule").

2. The call’s context transitions to a cancelled state (e.g. due to a timeout expiring). When this happens,
   the `abort_func` is called. Its interface looks like:

   ```
   def abort_func(raise_cancel):
       ...
       return trio.lowlevel.Abort.SUCCEEDED  # or FAILED
   
   ```

   It should attempt to clean up any state associated with this call, and in particular, arrange
   that [`reschedule()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.reschedule "trio.lowlevel.reschedule")
   will _not_ be called later. If (and only if!) it is successful, then it should
   return [`Abort.SUCCEEDED`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Abort.SUCCEEDED "trio.lowlevel.Abort.SUCCEEDED"),
   in which case the task will automatically be rescheduled with an
   appropriate [`Cancelled`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.Cancelled "trio.Cancelled")
   error.

   Otherwise, it should
   return [`Abort.FAILED`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Abort.FAILED "trio.lowlevel.Abort.FAILED").
   This means that the task can’t be cancelled at this time, and still has to make sure that “someone” eventually
   calls [`reschedule()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.reschedule "trio.lowlevel.reschedule").

   At that point there are again two possibilities. You can simply ignore the cancellation altogether: wait for the
   operation to complete and then reschedule and continue as normal. (For example, this is
   what [`trio.to_thread.run_sync()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.to_thread.run_sync "trio.to_thread.run_sync")
   does if cancellation is disabled.) The other possibility is that the `abort_func` does succeed in cancelling the
   operation, but for some reason isn’t able to report that right away. (Example: on Windows, it’s possible to request
   that an async (“overlapped”) I/O operation be cancelled, but this request is _also_ asynchronous – you don’t find out
   until later whether the operation was actually cancelled or not.) To report a delayed cancellation, then you should
   reschedule the task yourself, and call the `raise_cancel` callback passed to `abort_func` to raise
   a [`Cancelled`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.Cancelled "trio.Cancelled") (or
   possibly [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)"))
   exception into this task. Either of the approaches sketched below can work:

   ```
   # Option 1:
   # Catch the exception from raise_cancel and inject it into the task.
   # (This is what Trio does automatically for you if you return
   # Abort.SUCCEEDED.)
   trio.lowlevel.reschedule(task, outcome.capture(raise_cancel))
   
   # Option 2:
   # wait to be woken by "someone", and then decide whether to raise
   # the error from inside the task.
   outer_raise_cancel = None
   def abort(inner_raise_cancel):
       nonlocal outer_raise_cancel
       outer_raise_cancel = inner_raise_cancel
       TRY_TO_CANCEL_OPERATION()
       return trio.lowlevel.Abort.FAILED
   await wait_task_rescheduled(abort)
   if OPERATION_WAS_SUCCESSFULLY_CANCELLED:
       # raises the error
       outer_raise_cancel()
   
   ```

   In any case it’s guaranteed that we only call the `abort_func` at most once per call
   to [`wait_task_rescheduled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_task_rescheduled "trio.lowlevel.wait_task_rescheduled").

Sometimes, it’s useful to be able to share some mutable sleep-related data between the sleeping task, the abort
function, and the waking task. You can use the sleeping
task’s [`custom_sleep_data`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task.custom_sleep_data "trio.lowlevel.Task.custom_sleep_data")
attribute to store this data, and Trio won’t touch it, except to make sure that it gets cleared when the task is
rescheduled.

Warning

If your `abort_func` raises an error, or returns any value other
than [`Abort.SUCCEEDED`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Abort.SUCCEEDED "trio.lowlevel.Abort.SUCCEEDED")
or [`Abort.FAILED`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Abort.FAILED "trio.lowlevel.Abort.FAILED"),
then Trio will crash violently. Be careful! Similarly, it is entirely possible to deadlock a Trio program by failing to
reschedule a blocked task, or cause havoc by
calling [`reschedule()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.reschedule "trio.lowlevel.reschedule")
too many times. Remember what we said up above about how you should use a higher-level API if at all possible?

_class_ trio.lowlevel.Abort(_value_, _names\=None_, _\*_, _module\=None_, _qualname\=None_, _type\=None_, _start\=1_,
_boundary\=None_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Abort "Permalink to this definition")

[`enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.11)") used as the return value from
abort functions.

See [`wait_task_rescheduled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_task_rescheduled "trio.lowlevel.wait_task_rescheduled")
for details.

SUCCEEDED[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Abort.SUCCEEDED "Permalink to this definition")

FAILED[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Abort.FAILED "Permalink to this definition")

trio.lowlevel.reschedule(_task_,
_next\_send=<object object>_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.reschedule "Permalink to this definition")

Reschedule the given task with the
given [`outcome.Outcome`](https://outcome.readthedocs.io/en/latest/api.html#outcome.Outcome "(in outcome v1.2.0+dev)").

See [`wait_task_rescheduled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_task_rescheduled "trio.lowlevel.wait_task_rescheduled")
for the gory details.

There must be exactly one call
to [`reschedule()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.reschedule "trio.lowlevel.reschedule")
for every call
to [`wait_task_rescheduled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_task_rescheduled "trio.lowlevel.wait_task_rescheduled"). (
And when counting, keep in mind that
returning [`Abort.SUCCEEDED`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Abort.SUCCEEDED "trio.lowlevel.Abort.SUCCEEDED")
from an abort callback is equivalent to
calling [`reschedule()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.reschedule "trio.lowlevel.reschedule")
once.)

Parameters:

- **task** ([
  _trio.lowlevel.Task_](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")) –
  the task to be rescheduled. Must be blocked in a call
  to [`wait_task_rescheduled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_task_rescheduled "trio.lowlevel.wait_task_rescheduled").

- **next\_send** ([
  _outcome.Outcome_](https://outcome.readthedocs.io/en/latest/api.html#outcome.Outcome "(in outcome v1.2.0+dev)")) – the
  value (or error) to return (or raise)
  from [`wait_task_rescheduled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_task_rescheduled "trio.lowlevel.wait_task_rescheduled").

Here’s an example lock class implemented
using [`wait_task_rescheduled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_task_rescheduled "trio.lowlevel.wait_task_rescheduled")
directly. This implementation has a number of flaws, including lack of fairness, O(n) cancellation, missing error
checking, failure to insert a checkpoint on the non-blocking path, etc. If you really want to implement your own lock,
then you should study the implementation
of [`trio.Lock`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.Lock "trio.Lock") and
use [`ParkingLot`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.ParkingLot "trio.lowlevel.ParkingLot"),
which handles some of these issues for you. But this does serve to illustrate the basic structure of
the [`wait_task_rescheduled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_task_rescheduled "trio.lowlevel.wait_task_rescheduled")
API:

```
class NotVeryGoodLock:
    def __init__(self):
        self._blocked_tasks = collections.deque()
        self._held = False

    async def acquire(self):
        # We might have to try several times to acquire the lock.
        while self._held:
            # Someone else has the lock, so we have to wait.
            task = trio.lowlevel.current_task()
            self._blocked_tasks.append(task)
            def abort_fn(_):
                self._blocked_tasks.remove(task)
                return trio.lowlevel.Abort.SUCCEEDED
            await trio.lowlevel.wait_task_rescheduled(abort_fn)
            # At this point the lock was released -- but someone else
            # might have swooped in and taken it again before we
            # woke up. So we loop around to check the 'while' condition
            # again.
        # if we reach this point, it means that the 'while' condition
        # has just failed, so we know no-one is holding the lock, and
        # we can take it.
        self._held = True

    def release(self):
        self._held = False
        if self._blocked_tasks:
            woken_task = self._blocked_tasks.popleft()
            trio.lowlevel.reschedule(woken_task)

```

## Task API[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#task-api "Permalink to this heading")

trio.lowlevel.current\_root\_task()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.current_root_task "Permalink to this definition")

Returns the current
root [`Task`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task").

This is the task that is the ultimate parent of all other tasks.

trio.lowlevel.current\_task()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.current_task "Permalink to this definition")

Return
the [`Task`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")
object representing the current task.

Returns:

the [`Task`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task") that
called [`current_task()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.current_task "trio.lowlevel.current_task").

Return type:

[Task](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")

_class_
trio.lowlevel.Task[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "Permalink to this definition")

A [`Task`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task") object
represents a concurrent “thread” of execution. It has no public constructor; Trio internally creates
a [`Task`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task") object
for each call to `nursery.start(...)` or `nursery.start_soon(...)`.

Its public members are mostly useful for introspection and debugging:

name[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task.name "Permalink to this definition")

String containing
this [`Task`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")'s
name. Usually the name of the function
this [`Task`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task") is
running, but can be overridden by passing `name=` to `start` or `start_soon`.

coro[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task.coro "Permalink to this definition")

This task’s coroutine object.

_for ... in_
iter\_await\_frames()[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task.iter_await_frames "Permalink to this definition")

Iterates recursively over the coroutine-like objects this task is waiting on, yielding the frame and line number at each
frame.

This is similar
to [`traceback.walk_stack`](https://docs.python.org/3/library/traceback.html#traceback.walk_stack "(in Python v3.11)")
in a synchronous context. Note
that [`traceback.walk_stack`](https://docs.python.org/3/library/traceback.html#traceback.walk_stack "(in Python v3.11)")
returns frames from the bottom of the call stack to the top, while this function starts
from [`Task.coro`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task.coro "trio.lowlevel.Task.coro")
and works it way down.

Example usage: extracting a stack trace:

```
import traceback

def print_stack_for_task(task):
    ss = traceback.StackSummary.extract(task.iter_await_frames())
    print("".join(ss.format()))

```

context[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task.context "Permalink to this definition")

This
task’s [`contextvars.Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "(in Python v3.11)")
object.

parent\_nursery[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task.parent_nursery "Permalink to this definition")

The nursery this task is inside (or None if this is the “init” task).

Example use case: drawing a visualization of the task tree in a debugger.

eventual\_parent\_nursery[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task.eventual_parent_nursery "Permalink to this definition")

The nursery this task will be inside after it calls `task_status.started()`.

If this task has already called `started()`, or if it was not spawned
using [`nursery.start()`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.Nursery.start "trio.Nursery.start"),
then
its [`eventual_parent_nursery`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task.eventual_parent_nursery "trio.lowlevel.Task.eventual_parent_nursery")
is `None`.

child\_nurseries[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task.child_nurseries "Permalink to this definition")

The nurseries this task contains.

This is a list, with outer nurseries before inner nurseries.

custom\_sleep\_data[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task.custom_sleep_data "Permalink to this definition")

Trio doesn’t assign this variable any meaning, except that it sets it to `None` whenever a task is rescheduled. It can
be used to share data between the different tasks involved in putting a task to sleep and then waking it up again. (
See [`wait_task_rescheduled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_task_rescheduled "trio.lowlevel.wait_task_rescheduled")
for details.)

## Using “guest mode” to run Trio on top of other event loops[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#using-guest-mode-to-run-trio-on-top-of-other-event-loops "Permalink to this heading")

### What is “guest mode”?[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#what-is-guest-mode "Permalink to this heading")

An event loop acts as a central coordinator to manage all the IO happening in your program. Normally, that means that
your application has to pick one event loop, and use it for everything. But what if you like Trio, but also need to use
a framework like [Qt](https://en.wikipedia.org/wiki/Qt_(software)) or [PyGame](https://www.pygame.org/) that has its own
event loop? Then you need some way to run both event loops at once.

It is possible to combine event loops, but the standard approaches all have significant downsides:

- **Polling:** this is where you use a [busy-loop](https://en.wikipedia.org/wiki/Busy_waiting) to manually check for IO
  on both event loops many times per second. This adds latency, and wastes CPU time and electricity.

- **Pluggable IO backends:** this is where you reimplement one of the event loop APIs on top of the other, so you
  effectively end up with just one event loop. This requires a significant amount of work for each pair of event loops
  you want to integrate, and different backends inevitably end up with inconsistent behavior, forcing users to program
  against the least-common-denominator. And if the two event loops expose different feature sets, it may not even be
  possible to implement one in terms of the other.

- **Running the two event loops in separate threads:** This works, but most event loop APIs aren’t thread-safe, so in
  this approach you need to keep careful track of which code runs on which event loop, and remember to use explicit
  inter-thread messaging whenever you interact with the other loop – or else risk obscure race conditions and data
  corruption.

That’s why Trio offers a fourth option: **guest mode**. Guest mode lets you
execute [`trio.run`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run") on top of some other
“host” event loop, like Qt. Its advantages are:

- Efficiency: guest mode is event-driven instead of using a busy-loop, so it has low latency and doesn’t waste
  electricity.

- No need to think about threads: your Trio code runs in the same thread as the host event loop, so you can freely call
  sync Trio APIs from the host, and call sync host APIs from Trio. For example, if you’re making a GUI app with Qt as
  the host loop, then making a [cancel button](https://doc.qt.io/qt-5/qpushbutton.html) and connecting it to
  a [`trio.CancelScope`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.CancelScope "trio.CancelScope")
  is as easy as writing:

  ```
  # Trio code can create Qt objects without any special ceremony...
  my_cancel_button = QPushButton("Cancel")
  # ...and Qt can call back to Trio just as easily
  my_cancel_button.clicked.connect(my_cancel_scope.cancel)
  
  ```

  (For async APIs, it’s not that simple, but you can use sync APIs to build explicit bridges between the two worlds,
  e.g. by passing async functions and their results back and forth through queues.)

- Consistent behavior: guest mode uses the same code as regular Trio: the same scheduler, same IO code, same everything.
  So you get the full feature set and everything acts the way you expect.

- Simple integration and broad compatibility: pretty much every event loop offers some threadsafe “schedule a callback”
  operation, and that’s all you need to use it as a host loop.

### Really? How is that possible?[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#really-how-is-that-possible "Permalink to this heading")

Note

You can use guest mode without reading this section. It’s included for those who enjoy understanding how things work.

All event loops have the same basic structure. They loop through two operations, over and over:

1. Wait for the operating system to notify them that something interesting has happened, like data arriving on a socket
   or a timeout passing. They do this by invoking a platform-specific `sleep_until_something_happens()` system
   call – `select`, `epoll`, `kqueue`, `GetQueuedCompletionEvents`, etc.

2. Run all the user tasks that care about whatever happened, then go back to step 1.

The problem here is step 1. Two different event loops on the same thread can take turns running user tasks in step 2,
but when they’re idle and nothing is happening, they can’t both invoke their own `sleep_until_something_happens()`
function at the same time.

The “polling” and “pluggable backend” strategies solve this by hacking the loops so both step 1s can run at the same
time in the same thread. Keeping everything in one thread is great for step 2, but the step 1 hacks create problems.

The “separate threads” strategy solves this by moving both steps into separate threads. This makes step 1 work, but the
downside is that now the user tasks in step 2 are running separate threads as well, so users are forced to deal with
inter-thread coordination.

The idea behind guest mode is to combine the best parts of each approach: we move Trio’s step 1 into a separate worker
thread, while keeping Trio’s step 2 in the main host thread. This way, when the application is idle, both event loops do
their `sleep_until_something_happens()` at the same time in their own threads. But when the app wakes up and your code
is actually running, it all happens in a single thread. The threading trickiness is all handled transparently inside
Trio.

Concretely, we unroll Trio’s internal event loop into a chain of callbacks, and as each callback finishes, it schedules
the next callback onto the host loop or a worker thread as appropriate. So the only thing the host loop has to provide
is a way to schedule a callback onto the main thread from a worker thread.

Coordinating between Trio and the host loop does add some overhead. The main cost is switching in and out of the
background thread, since this requires cross-thread messaging. This is cheap (on the order of a few microseconds,
assuming your host loop is implemented efficiently), but it’s not free.

But, there’s a nice optimization we can make: we only _need_ the thread when our `sleep_until_something_happens()` call
actually sleeps, that is, when the Trio part of your program is idle and has nothing to do. So before we switch into the
worker thread, we double-check whether we’re idle, and if not, then we skip the worker thread and jump directly to step

2. This means that your app only pays the extra thread-switching penalty at moments when it would otherwise be sleeping,
   so it should have minimal effect on your app’s overall performance.

The total overhead will depend on your host loop, your platform, your application, etc. But we expect that in most
cases, apps running in guest mode should only be 5-10% slower than the same code
using [`trio.run`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run"). If you find that’s
not true for your app, then please let us know and we’ll see if we can fix it!

### Implementing guest mode for your favorite event loop[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#implementing-guest-mode-for-your-favorite-event-loop "Permalink to this heading")

Let’s walk through what you need to do to integrate Trio’s guest mode with your favorite event loop. Treat this section
like a checklist.

**Getting started:** The first step is to get something basic working. Here’s a minimal example of running Trio on top
of asyncio, that you can use as a model:

```
import asyncio, trio

# A tiny Trio program
async def trio_main():
    for _ in range(5):
        print("Hello from Trio!")
        # This is inside Trio, so we have to use Trio APIs
        await trio.sleep(1)
    return "trio done!"

# The code to run it as a guest inside asyncio
async def asyncio_main():
    asyncio_loop = asyncio.get_running_loop()

    def run_sync_soon_threadsafe(fn):
        asyncio_loop.call_soon_threadsafe(fn)

    def done_callback(trio_main_outcome):
        print(f"Trio program ended with: {trio_main_outcome}")

    # This is where the magic happens:
    trio.lowlevel.start_guest_run(
        trio_main,
        run_sync_soon_threadsafe=run_sync_soon_threadsafe,
        done_callback=done_callback,
    )

    # Let the host loop run for a while to give trio_main time to
    # finish. (WARNING: This is a hack. See below for better
    # approaches.)
    #
    # This function is in asyncio, so we have to use asyncio APIs.
    await asyncio.sleep(10)

asyncio.run(asyncio_main())

```

You can see we’re using asyncio-specific APIs to start up a loop, and then we
call [`trio.lowlevel.start_guest_run`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.start_guest_run "trio.lowlevel.start_guest_run").
This function is very similar
to [`trio.run`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run"), and takes all the same
arguments. But it has two differences:

First, instead of blocking until `trio_main` has finished, it schedules `trio_main` to start running on top of the host
loop, and then returns immediately. So `trio_main` is running in the background – that’s why we have to sleep and give
it time to finish.

And second, it requires two extra keyword arguments: `run_sync_soon_threadsafe`, and `done_callback`.

For `run_sync_soon_threadsafe`, we need a function that takes a synchronous callback, and schedules it to run on your
host loop. And this function needs to be “threadsafe” in the sense that you can safely call it from any thread. So you
need to figure out how to write a function that does that using your host loop’s API. For asyncio, this is easy
because [`call_soon_threadsafe`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "(in Python v3.11)")
does exactly what we need; for your loop, it might be more or less complicated.

For `done_callback`, you pass in a function that Trio will automatically invoke when the Trio run finishes, so you know
it’s done and what happened. For this basic starting version, we just print the result; in the next section we’ll
discuss better alternatives.

At this stage you should be able to run a simple Trio program inside your host loop. Now we’ll turn that prototype into
something solid.

**Loop lifetimes:** One of the trickiest things in most event loops is shutting down correctly. And having two event
loops makes this even harder!

If you can, we recommend following this pattern:

- Start up your host loop

- Immediately
  call [`start_guest_run`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.start_guest_run "trio.lowlevel.start_guest_run")
  to start Trio

- When Trio finishes and your `done_callback` is invoked, shut down the host loop

- Make sure that nothing else shuts down your host loop

This way, your two event loops have the same lifetime, and your program automatically exits when your Trio function
finishes.

Here’s how we’d extend our asyncio example to implement this pattern:

```
# Improved version, that shuts down properly after Trio finishes
async def asyncio_main():
    asyncio_loop = asyncio.get_running_loop()

    def run_sync_soon_threadsafe(fn):
        asyncio_loop.call_soon_threadsafe(fn)

    # Revised 'done' callback: set a Future
    done_fut = asyncio_loop.create_future()
    def done_callback(trio_main_outcome):
        done_fut.set_result(trio_main_outcome)

    trio.lowlevel.start_guest_run(
        trio_main,
        run_sync_soon_threadsafe=run_sync_soon_threadsafe,
        done_callback=done_callback,
    )

    # Wait for the guest run to finish
    trio_main_outcome = await done_fut
    # Pass through the return value or exception from the guest run
    return trio_main_outcome.unwrap()

```

And then you can encapsulate all this machinery in a utility function that exposes
a [`trio.run`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run")\-like API, but runs both
loops together:

```
def trio_run_with_asyncio(trio_main, *args, **trio_run_kwargs):
    async def asyncio_main():
        # same as above
        ...

    return asyncio.run(asyncio_main())

```

Technically, it is possible to use other patterns. But there are some important limitations you have to respect:

- **You must let the Trio program run to completion.** Many event loops let you stop the event loop at any point, and
  any pending callbacks/tasks/etc. just… don’t run. Trio follows a more structured system, where you can cancel things,
  but the code always runs to completion, so `finally` blocks run, resources are cleaned up, etc. If you stop your host
  loop early, before the `done_callback` is invoked, then that cuts off the Trio run in the middle without a chance to
  clean up. This can leave your code in an inconsistent state, and will definitely leave Trio’s internals in an
  inconsistent state, which will cause errors if you try to use Trio again in that thread.

  Some programs need to be able to quit at any time, for example in response to a GUI window being closed or a user
  selecting a “Quit” from a menu. In these cases, we recommend wrapping your whole program in
  a [`trio.CancelScope`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.CancelScope "trio.CancelScope"),
  and cancelling it when you want to quit.

- Each host loop can only have
  one [`start_guest_run`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.start_guest_run "trio.lowlevel.start_guest_run")
  at a time. If you try to start a second one, you’ll get an error. If you need to run multiple Trio functions at the
  same time, then start up a single Trio run, open a nursery, and then start your functions as child tasks in that
  nursery.

- Unless you or your host loop register a handler
  for [`signal.SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "(in Python v3.11)") before starting
  Trio (this is not common), then Trio will take over delivery
  of [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)")s.
  And since Trio can’t tell which host code is safe to interrupt, it will only
  deliver [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)")
  into the Trio part of your code. This is fine if your program is set up to exit when the Trio part exits, because
  the [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)")
  will propagate out of Trio and then trigger the shutdown of your host loop, which is just what you want.

Given these constraints, we think the simplest approach is to always start and stop the two loops together.

**Signal management:** [“Signals”](https://en.wikipedia.org/wiki/Signal_(IPC)) are a low-level inter-process
communication primitive. When you hit control-C to kill a program, that uses a signal. Signal handling in Python
has [a lot of moving parts](https://vorpus.org/blog/control-c-handling-in-python-and-trio/). One of those parts
is [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "(in Python v3.11)"),
which event loops use to make sure that they wake up when a signal arrives so they can respond to it. (If you’ve ever
had an event loop ignore you when you hit control-C, it was probably because they weren’t
using [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "(in Python v3.11)")
correctly.)

But, only one event loop can
use [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "(in Python v3.11)") at
a time. And in guest mode that can cause problems: Trio and the host loop might start fighting over who’s
using [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "(in Python v3.11)").

Some event loops, like asyncio, won’t work correctly unless they win this fight. Fortunately, Trio is a little less
picky: as long as _someone_ makes sure that the program wakes up when a signal arrives, it should work correctly. So if
your host loop
wants [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "(in Python v3.11)"),
then you should disable
Trio’s [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "(in Python v3.11)")
support, and then both loops will work correctly.

On the other hand, if your host loop doesn’t
use [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "(in Python v3.11)"),
then the only way to make everything work correctly is to _enable_
Trio’s [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "(in Python v3.11)")
support.

By default, Trio assumes that your host loop doesn’t
use [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "(in Python v3.11)"). It
does try to detect when this creates a conflict with the host loop, and print a warning – but unfortunately, by the time
it detects it, the damage has already been done. So if you’re getting this warning, then you should disable
Trio’s [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "(in Python v3.11)")
support by passing `host_uses_signal_set_wakeup_fd=True`
to [`start_guest_run`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.start_guest_run "trio.lowlevel.start_guest_run").

If you aren’t seeing any warnings with your initial prototype, you’re _probably_ fine. But the only way to be certain is
to check your host loop’s source. For example, asyncio may or may not
use [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "(in Python v3.11)")
depending on the Python version and operating system.

**A small optimization:** Finally, consider a small optimization. Some event loops offer two versions of their “call
this function soon” API: one that can be used from any thread, and one that can only be used from the event loop thread,
with the latter being cheaper. For example, asyncio has
both [`call_soon_threadsafe`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "(in Python v3.11)")
and [`call_soon`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "(in Python v3.11)").

If you have a loop like this, then you can also pass a `run_sync_soon_not_threadsafe=...` kwarg
to [`start_guest_run`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.start_guest_run "trio.lowlevel.start_guest_run"),
and Trio will automatically use it when appropriate.

If your loop doesn’t have a split like this, then don’t worry about it; `run_sync_soon_not_threadsafe=` is optional. (If
it’s not passed, then Trio will just use your threadsafe version in all cases.)

**That’s it!** If you’ve followed all these steps, you should now have a cleanly-integrated hybrid event loop. Go make
some cool GUIs/games/whatever!

### Limitations[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#limitations "Permalink to this heading")

In general, almost all Trio features should work in guest mode. The exception is features which rely on Trio having a
complete picture of everything that your program is doing, since obviously, it can’t control the host loop or see what
it’s doing.

Custom clocks can be used in guest mode, but they only affect Trio timeouts, not host loop timeouts. And
the [autojump clock](https://trio.readthedocs.io/en/stable/reference-testing.html#testing-time) and
related [`trio.testing.wait_all_tasks_blocked`](https://trio.readthedocs.io/en/stable/reference-testing.html#trio.testing.wait_all_tasks_blocked "trio.testing.wait_all_tasks_blocked")
can technically be used in guest mode, but they’ll only take Trio tasks into account when decided whether to jump the
clock or whether all tasks are blocked.

### Reference[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#reference "Permalink to this heading")

trio.lowlevel.start\_guest\_run(_async\_fn_, _\*args_, _run\_sync\_soon\_threadsafe_, _done\_callback_,
_run\_sync\_soon\_not\_threadsafe\=None_,
_host\_uses\_signal\_set\_wakeup\_fd: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)") \=
False_, _clock\=None_, _instruments\=()_,
_restrict\_keyboard\_interrupt\_to\_checkpoints: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)") \=
False_, _strict\_exception\_groups: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)") \=
False_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.start_guest_run "Permalink to this definition")

Start a “guest” run of Trio on top of some other “host” event loop.

Each host loop can only have one guest run at a time.

You should always let the Trio run finish before stopping the host loop; if not, it may leave Trio’s internal data
structures in an inconsistent state. You might be able to get away with it if you immediately exit the program, but it’s
safest not to go there in the first place.

Generally, the best way to do this is wrap this in a function that starts the host loop and then immediately starts the
guest run, and then shuts down the host when the guest run completes.

Parameters:

- **run\_sync\_soon\_threadsafe** –

  An arbitrary callable, which will be passed a function as its sole argument:

  ```
  def my_run_sync_soon_threadsafe(fn):
      ...
  
  ```

  This callable should schedule `fn()` to be run by the host on its next pass through its loop. **Must support being
  called from arbitrary threads.**

- **done\_callback** –

  An arbitrary callable:

  ```
  def my_done_callback(run_outcome):
      ...
  
  ```

  When the Trio run has finished, Trio will invoke this callback to let you know. The argument is
  an [`outcome.Outcome`](https://outcome.readthedocs.io/en/latest/api.html#outcome.Outcome "(in outcome v1.2.0+dev)"),
  reporting what would have been returned or raised
  by [`trio.run`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run"). This function can do
  anything you want, but commonly you’ll want it to shut down the host loop, unwrap the outcome, etc.

- **run\_sync\_soon\_not\_threadsafe** – Like `run_sync_soon_threadsafe`, but will only be called from inside the host
  loop’s main thread. Optional, but if your host loop allows you to implement this more efficiently
  than `run_sync_soon_threadsafe` then passing it will make things a bit faster.

- **host\_uses\_signal\_set\_wakeup\_fd** ([
  _bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) –
  Pass [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.11)") if your host loop
  uses [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "(in Python v3.11)"),
  and [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.11)") otherwise. For more details,
  see [Implementing guest mode for your favorite event loop](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#guest-run-implementation).

For the meaning of other arguments,
see [`trio.run`](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run "trio.run").

## Handing off live coroutine objects between coroutine runners[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#handing-off-live-coroutine-objects-between-coroutine-runners "Permalink to this heading")

Internally, Python’s async/await syntax is built around the idea of “coroutine objects” and “coroutine runners”. A
coroutine object represents the state of an async callstack. But by itself, this is just a static object that sits
there. If you want it to do anything, you need a coroutine runner to push it forward. Every Trio task has an associated
coroutine object (
see [`Task.coro`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task.coro "trio.lowlevel.Task.coro")),
and the Trio scheduler acts as their coroutine runner.

But of course, Trio isn’t the only coroutine runner in
Python – [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "(in Python v3.11)") has one, other
event loops have them, you can even define your own.

And in some very, very unusual circumstances, it even makes sense to transfer a single coroutine object back and forth
between different coroutine runners. That’s what this section is about. This is an _extremely_ exotic use case, and
assumes a lot of expertise in how Python async/await works internally. For motivating examples,
see [trio-asyncio issue #42](https://github.com/python-trio/trio-asyncio/issues/42),
and [trio issue #649](https://github.com/python-trio/trio/issues/649). For more details on how coroutines work, we
recommend André Caron’s [A tale of event loops](https://github.com/AndreLouisCaron/a-tale-of-event-loops), or going
straight to [PEP 492](https://www.python.org/dev/peps/pep-0492/) for the full details.

_await_ trio.lowlevel.permanently\_detach\_coroutine\_object(
_final\_outcome_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.permanently_detach_coroutine_object "Permalink to this definition")

Permanently detach the current task from the Trio scheduler.

Normally, a Trio task doesn’t exit until its coroutine object exits. When you call this function, Trio acts like the
coroutine object just exited and the task terminates with the given outcome. This is useful if you want to permanently
switch the coroutine object over to a different coroutine runner.

When the calling coroutine enters this function it’s running under Trio, and when the function returns it’s running
under the foreign coroutine runner.

You should make sure that the coroutine object has released any Trio-specific resources it has acquired (e.g.
nurseries).

Parameters:

**final\_outcome** ([
_outcome.Outcome_](https://outcome.readthedocs.io/en/latest/api.html#outcome.Outcome "(in outcome v1.2.0+dev)")) – Trio
acts as if the current task exited with the given return value or exception.

Returns or raises whatever value or exception the new coroutine runner uses to resume the coroutine.

_await_ trio.lowlevel.temporarily\_detach\_coroutine\_object(
_abort\_func_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.temporarily_detach_coroutine_object "Permalink to this definition")

Temporarily detach the current coroutine object from the Trio scheduler.

When the calling coroutine enters this function it’s running under Trio, and when the function returns it’s running
under the foreign coroutine runner.

The Trio [`Task`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")
will continue to exist, but will be suspended until you
use [`reattach_detached_coroutine_object()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.reattach_detached_coroutine_object "trio.lowlevel.reattach_detached_coroutine_object")
to resume it. In the mean time, you can use another coroutine runner to schedule the coroutine object. In fact, you have
to – the function doesn’t return until the coroutine is advanced from outside.

Note that you’ll need to save the
current [`Task`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")
object to later resume; you can retrieve it
with [`current_task()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.current_task "trio.lowlevel.current_task").
You can also use
this [`Task`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")
object to retrieve the coroutine object –
see [`Task.coro`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task.coro "trio.lowlevel.Task.coro").

Parameters:

**abort\_func** – Same as
for [`wait_task_rescheduled()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.wait_task_rescheduled "trio.lowlevel.wait_task_rescheduled"),
except that it must
return [`Abort.FAILED`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Abort.FAILED "trio.lowlevel.Abort.FAILED"). (
If it
returned [`Abort.SUCCEEDED`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Abort.SUCCEEDED "trio.lowlevel.Abort.SUCCEEDED"),
then Trio would attempt to reschedule the detached task directly without going
through [`reattach_detached_coroutine_object()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.reattach_detached_coroutine_object "trio.lowlevel.reattach_detached_coroutine_object"),
which would be bad.) Your `abort_func` should still arrange for whatever the coroutine object is doing to be cancelled,
and then reattach to Trio and call the `raise_cancel` callback, if possible.

Returns or raises whatever value or exception the new coroutine runner uses to resume the coroutine.

_await_ trio.lowlevel.reattach\_detached\_coroutine\_object(_task_,
_yield\_value_)[¶](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.reattach_detached_coroutine_object "Permalink to this definition")

Reattach a coroutine object that was detached
using [`temporarily_detach_coroutine_object()`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.temporarily_detach_coroutine_object "trio.lowlevel.temporarily_detach_coroutine_object").

When the calling coroutine enters this function it’s running under the foreign coroutine runner, and when the function
returns it’s running under Trio.

This must be called from inside the coroutine being resumed, and yields whatever value you pass in. (Presumably you’ll
pass a value that will cause the current coroutine runner to stop scheduling this task.) Then the coroutine is resumed
by the Trio scheduler at the next opportunity.

Parameters:

- **task** ([
  _Task_](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio.lowlevel.Task "trio.lowlevel.Task")) – The
  Trio task object that the current coroutine was detached from.

- **yield\_value** ([_object_](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – The
  object to yield to the current coroutine runner.
