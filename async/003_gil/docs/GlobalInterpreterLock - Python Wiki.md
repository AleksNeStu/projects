---
source: https://wiki.python.org/moin/GlobalInterpreterLock \
created: 2022-12-26T16:54:14 (UTC +01:00) \
tags: [] \
author: 
---

# GlobalInterpreterLock - Python Wiki
---
In CPython, the **global interpreter lock**, or **GIL**, is a mutex that protects access to Python objects, preventing
multiple threads from executing Python bytecodes at once. The GIL prevents race conditions and ensures thread safety. A
nice explanation
of [how the Python GIL helps in these areas can be found here](https://python.land/python-concurrency/the-python-gil).
In short, this mutex is necessary mainly because CPython's memory management is not thread-safe.

In hindsight, the GIL is not ideal, since it prevents multithreaded CPython programs from taking full advantage of
multiprocessor systems in certain situations. Luckily, many potentially blocking or long-running operations, such as
I/O, image processing, and [NumPy](https://wiki.python.org/moin/NumPy) number crunching, happen _outside_ the GIL.
Therefore it is only in multithreaded programs that spend a lot of time inside the GIL, interpreting CPython bytecode,
that the GIL becomes a bottleneck.

Unfortunately, since the GIL exists, other features have grown to depend on the guarantees that it enforces. This makes
it hard to remove the GIL without breaking many official and unofficial Python packages and modules.

[The GIL can degrade performance](http://www.dabeaz.com/python/GIL.pdf) even when it is not a bottleneck. Summarizing
the linked slides: The system call overhead is significant, especially on multicore hardware. Two threads calling a
function may take twice as much time as a single thread calling the function twice. The GIL can cause I/O-bound threads
to be scheduled ahead of CPU-bound threads, and it prevents signals from being delivered.

CPython extensions must be GIL-aware in order to avoid defeating threads. For an explanation,
see [Global interpreter lock](https://docs.python.org/3/c-api/init.html#thread-state-and-the-global-interpreter-lock).

## Non-CPython implementations

- [Jython](https://wiki.python.org/moin/Jython) and [IronPython](https://wiki.python.org/moin/IronPython) have no GIL
  and can fully exploit multiprocessor systems

- [PyPy](https://wiki.python.org/moin/PyPy) currently has a GIL like CPython

- in Cython the GIL exists, but can be released temporarily using a "with" statement

\[Mention place of GIL in [StacklessPython](https://wiki.python.org/moin/StacklessPython).\]

## Eliminating the GIL

Getting rid of the GIL is an occasional topic on the python-dev mailing list. No one has managed it yet. The following
properties are all highly desirable for any potential GIL replacement; some are hard requirements.

- **Simplicity.** The proposal must be implementable and maintainable in the long run.

- **Concurrency.** The point of eliminating the GIL would be to improve the performance of multithreaded programs. So
  any proposal must show that it actually does so in practice.

- **Speed.** The [BDFL](https://wiki.python.org/moin/BDFL) has said he will reject any proposal in this direction that
  slows down single-threaded programs. (citation needed) Note that this is harder than it looks. The existing reference
  count mechanism is very fast in the non-concurrent case, but means that almost any reference to an object is a
  modification (at least to the refcount); many concurrent GC algorithms assume that modifications are rare.

- **Features.** The proposal must support existing CPython features including \_\_del\_\_ and weak references.

    - \_\_del\_\_ isn't thread-safe, becoming a large problem if any sort of locking becomes commonplace. My CPython
      fork will provide a safer and more reliable replacement. --Rhamphoryncus

        - What's not thread-safe about \_\_del\_\_? --jorendorff

            - The language doesn't say anything about what sort of atomicity any operation has. That dict operations are
              often thread-safe in CPython today is mostly to avoid low-level crashes.

              This is normally solved in threads by using locks, but \_\_del\_\_ may be executed currently holding the
              same lock you want, resulting in a deadlock. To fix this (without adding a memory model to the language)
              requires you run \_\_del\_\_ in a dedicated system thread and require you to use locks (such as those
              provided by a monitor.) (Non-blocking algorithms are possible in assembly, but insanely overcomplicated
              from a Python perspect.) --Rhamphoryncus

- **API compatibility.** The proposal should be source-compatible with the macros used by all existing CPython
  extensions (Py\_INCREF and friends).
  See [Python/C API Reference Manual: Reference Counting](http://docs.python.org/api/countingRefs.html).

- **Prompt destruction** (nice to have?). The existing reference-counting scheme destroys objects as soon as they become
  unreachable, except for objects in reference cycles. Those are collected later by Python's cycle collector. Some
  CPython programs depend on this, e.g. to close files promptly, so it would be nice to keep this feature.

- **Ordered destruction** (nice to have?). Barring cycles, Python currently always destroys an unreachable object _X_
  before destroying any other objects referenced by _X_. This means all the object's attributes are still there when
  \_\_del\_\_ runs. (Many garbage collection schemes don't guarantee this.)

    - I'd say this is necessary for Python. There's very little you can usefully do with a half-destroyed object. That
      which you can do, you could also do without being exposed to half-destroyed objects. --Rhamphoryncus
        - The [language reference](http://docs.python.org/ref/customization.html) doesn't require this. I doubt Jython
          or [IronPython](https://wiki.python.org/moin/IronPython) provides it. --jorendorff

            - They seem deliberately vague. Java distinguishes finalized from non-finalized objects, and a single
              finalizer is ordered with regard to non-finalized objects. The catch is that it's not ordered with regard
              to other finalizers, so you need to program as if they may already be deleted. In practise this means
              avoiding finalizers unless absolutely necessary, and if necessary they must not depend on each other.

              CPython uses low-level finalizers extensively, so it must have stronger guarantees. Because of this, it
              refuses to delete cycles involving \_\_del\_\_. The interesting realization is that, although finalizers
              in java are run even in the face of reference cycles, they cannot be correct unless you eliminate
              finalizer cycles. Finding ways to tell the GC implementation of this key distinction lets you have your
              cake and eat it too. --Rhamphoryncus

                - I don't subscribe to "it must have stronger guarantees". CPython uses C-level finalizers mostly for
                  memory management and occasionally (as with file objects) for some non-order-dependent cleanup.
                  --jorendorff

                    - The implementation doesn't distinguish C-level finalizers from Python-level finalizers (except to
                      refuse to delete cycles involving \_\_del\_\_), which is why it needs stronger guarantees. If you
                      made \_\_del\_\_ use a separate pass then you could loosen it to what Java provides.
                      --Rhamphoryncus

### API compatibility in detail

API compatibility is an especially difficult aspect of the problem. All concurrent memory management schemes we've found
rely on one or more of the following techniques, all of which are incompatible with the existing Python/C API.

- **Tracing.** Most garbage collectors need to be able to start with an object and enumerate all the objects that it
  points to. The builtin CPython pointer-containing types, like PyList and PyDict, all have a tp\_traverse method that
  can do this, but not all extension types have that method.

- **Write barriers.** A write barrier is a small piece of code that executes whenever a pointer variable is modified.
  Alas, no matter how you hack the Py\_INCREF etc. macros, you can't make a write barrier hook out of them. Even if you
  could, many schemes require a different write barrier for stack variables vs. global variables vs. object fields that
  point to other objects; nothing in the Python/C API makes that distinction.

- **Exact stack information.** Exact garbage collection schemes need to be able to mark all objects reachable from local
  C variables. To do this, some schemes need to know where such variables are located on the C stack (and/or registers)
  --something the Python/C API does not require extensions to track.

It is barely credible that CPython might someday make tp\_traverse mandatory for pointer-carrying types; adding support
for write barriers or stack bookkeeping to the Python/C API seems extremely unlikely.

Another issue in this area is that existing C extensions depend on the GIL guarantees. They assume that when extension
code is called, all other threads are locked out. If an extension does need to deal with a threaded environment, it
explicitly opts in (by releasing the GIL). Therefore any would-be GIL replacement must provide GIL-like guarantees by
default. Threading must remain opt-in for extensions.

## Recent discussions

- [message on 2009-10-25 by Antoine Pitrou](http://mail.python.org/pipermail/python-dev/2009-October/093321.html):
  Reworking the GIL (for 3.2)

- [Understanding the Python GIL](http://www.dabeaz.com/GIL/): David Beazley
  at [PyCon](https://wiki.python.org/moin/PyCon) 2010

- [issue #7753](http://bugs.python.org/issue7753): Backport to 2.7 _(rejected)_

- [issue #7946](http://bugs.python.org/issue7946): Convoy effect with I/O bound threads and New GIL

- [issue #8299](http://bugs.python.org/issue8299): Improve GIL in 2.7
