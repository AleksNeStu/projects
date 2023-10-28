---
source: https://trio.readthedocs.io/en/stable/index.html

created: 2023-10-18T11:47:54 (UTC +02:00)

tags: []

author: 

---

# Trio: a friendly Python library for async concurrency and I/O — Trio 0.22.2 documentation
---
The Trio project’s goal is to produce a
production-quality, [permissively licensed](https://github.com/python-trio/trio/blob/master/LICENSE), async/await-native
I/O library for Python. Like all async libraries, its main purpose is to help you write programs that do **multiple
things at the same time** with **parallelized I/O**. A web spider that wants to fetch lots of pages in parallel, a web
server that needs to juggle lots of downloads and websocket connections at the same time, a process supervisor
monitoring multiple subprocesses… that sort of thing. Compared to other libraries, Trio attempts to distinguish itself
with an obsessive focus on **usability** and **correctness**. Concurrency is complicated; we try to make it _easy_ to
get things _right_.

Trio was built from the ground up to take advantage of
the [latest Python features](https://www.python.org/dev/peps/pep-0492/), and draws inspiration
from [many sources](https://github.com/python-trio/trio/wiki/Reading-list), in particular Dave
Beazley’s [Curio](https://curio.readthedocs.io/). The resulting design is radically simpler than older competitors
like [asyncio](https://docs.python.org/3/library/asyncio.html) and [Twisted](https://twistedmatrix.com/), yet just as
capable. Trio is the Python I/O library I always wanted; I find it makes building I/O-oriented programs easier, less
error-prone, and just plain more fun. Perhaps you’ll find the same.

This project is young and still somewhat experimental: the overall design is solid and the existing features are fully
tested and documented, but you may encounter missing functionality or rough edges. We _do_ encourage you do use it, but
you should [read and subscribe to issue #1](https://github.com/python-trio/trio/issues/1) to get warning and a chance to
give feedback about any compatibility-breaking changes.

Vital statistics:

- Supported environments: We test on

    - Python: 3.7+ (CPython and PyPy)

    - Windows, macOS, Linux (glibc and musl), FreeBSD

  Other environments might also work; give it a try and see.

- Install: `python3 -m pip install -U trio` (or on Windows, maybe `py -3 -m pip install -U trio`). No compiler needed.

- Tutorial and reference manual: [https://trio.readthedocs.io](https://trio.readthedocs.io/)

- Bug tracker and source code: [https://github.com/python-trio/trio](https://github.com/python-trio/trio)

- Real-time chat: [https://gitter.im/python-trio/general](https://gitter.im/python-trio/general)

- Discussion forum: [https://trio.discourse.group](https://trio.discourse.group/)

- License: MIT or Apache 2, your choice

- Contributor
  guide: [https://trio.readthedocs.io/en/latest/contributing.html](https://trio.readthedocs.io/en/latest/contributing.html)

- Code of conduct: Contributors are requested to follow
  our [code of conduct](https://trio.readthedocs.io/en/latest/code-of-conduct.html) in all project spaces.

Trio's friendly, yet comprehensive, manual:

- [Tutorial](https://trio.readthedocs.io/en/stable/tutorial.html)
    - [Before you begin](https://trio.readthedocs.io/en/stable/tutorial.html#before-you-begin)
    - [If you get lost or confused…](https://trio.readthedocs.io/en/stable/tutorial.html#if-you-get-lost-or-confused)
    - [Async functions](https://trio.readthedocs.io/en/stable/tutorial.html#async-functions)
    - [A kinder, gentler GIL](https://trio.readthedocs.io/en/stable/tutorial.html#a-kinder-gentler-gil)
    - [Networking with Trio](https://trio.readthedocs.io/en/stable/tutorial.html#networking-with-trio)
    - [When things go wrong: timeouts, cancellation and exceptions in concurrent tasks](https://trio.readthedocs.io/en/stable/tutorial.html#when-things-go-wrong-timeouts-cancellation-and-exceptions-in-concurrent-tasks)
- [Awesome Trio Libraries](https://trio.readthedocs.io/en/stable/awesome-trio-libraries.html)
    - [Getting Started](https://trio.readthedocs.io/en/stable/awesome-trio-libraries.html#getting-started)
    - [Web and HTML](https://trio.readthedocs.io/en/stable/awesome-trio-libraries.html#web-and-html)
    - [Database](https://trio.readthedocs.io/en/stable/awesome-trio-libraries.html#database)
    - [IOT](https://trio.readthedocs.io/en/stable/awesome-trio-libraries.html#iot)
    - [Building Command Line Apps](https://trio.readthedocs.io/en/stable/awesome-trio-libraries.html#building-command-line-apps)
    - [Building GUI Apps](https://trio.readthedocs.io/en/stable/awesome-trio-libraries.html#building-gui-apps)
    - [Multi-Core/Multiprocessing](https://trio.readthedocs.io/en/stable/awesome-trio-libraries.html#multi-core-multiprocessing)
    - [Stream Processing](https://trio.readthedocs.io/en/stable/awesome-trio-libraries.html#stream-processing)
    - [RPC](https://trio.readthedocs.io/en/stable/awesome-trio-libraries.html#rpc)
    - [Testing](https://trio.readthedocs.io/en/stable/awesome-trio-libraries.html#testing)
    - [Tools and Utilities](https://trio.readthedocs.io/en/stable/awesome-trio-libraries.html#tools-and-utilities)
    - [Trio/Asyncio Interoperability](https://trio.readthedocs.io/en/stable/awesome-trio-libraries.html#trio-asyncio-interoperability)
- [Trio’s core functionality](https://trio.readthedocs.io/en/stable/reference-core.html)
    - [Entering Trio](https://trio.readthedocs.io/en/stable/reference-core.html#entering-trio)
    - [General principles](https://trio.readthedocs.io/en/stable/reference-core.html#general-principles)
    - [Time and clocks](https://trio.readthedocs.io/en/stable/reference-core.html#time-and-clocks)
    - [Cancellation and timeouts](https://trio.readthedocs.io/en/stable/reference-core.html#cancellation-and-timeouts)
    - [Tasks let you do multiple things at once](https://trio.readthedocs.io/en/stable/reference-core.html#tasks-let-you-do-multiple-things-at-once)
    - [Task-local storage](https://trio.readthedocs.io/en/stable/reference-core.html#task-local-storage)
    - [Synchronizing and communicating between tasks](https://trio.readthedocs.io/en/stable/reference-core.html#synchronizing-and-communicating-between-tasks)
    - [Notes on async generators](https://trio.readthedocs.io/en/stable/reference-core.html#notes-on-async-generators)
    - [Threads (if you must)](https://trio.readthedocs.io/en/stable/reference-core.html#threads-if-you-must)
    - [Exceptions and warnings](https://trio.readthedocs.io/en/stable/reference-core.html#exceptions-and-warnings)
- [I/O in Trio](https://trio.readthedocs.io/en/stable/reference-io.html)
    - [The abstract Stream API](https://trio.readthedocs.io/en/stable/reference-io.html#the-abstract-stream-api)
    - [Low-level networking with `trio.socket`](https://trio.readthedocs.io/en/stable/reference-io.html#low-level-networking-with-trio-socket)
    - [Asynchronous filesystem I/O](https://trio.readthedocs.io/en/stable/reference-io.html#asynchronous-filesystem-i-o)
    - [Spawning subprocesses](https://trio.readthedocs.io/en/stable/reference-io.html#spawning-subprocesses)
    - [Signals](https://trio.readthedocs.io/en/stable/reference-io.html#signals)
- [Testing made easier with `trio.testing`](https://trio.readthedocs.io/en/stable/reference-testing.html)
    - [Test harness integration](https://trio.readthedocs.io/en/stable/reference-testing.html#test-harness-integration)
    - [Time and timeouts](https://trio.readthedocs.io/en/stable/reference-testing.html#time-and-timeouts)
    - [Inter-task ordering](https://trio.readthedocs.io/en/stable/reference-testing.html#inter-task-ordering)
    - [Streams](https://trio.readthedocs.io/en/stable/reference-testing.html#streams)
    - [Virtual networking for testing](https://trio.readthedocs.io/en/stable/reference-testing.html#virtual-networking-for-testing)
    - [Testing checkpoints](https://trio.readthedocs.io/en/stable/reference-testing.html#testing-checkpoints)
- [Introspecting and extending Trio with `trio.lowlevel`](https://trio.readthedocs.io/en/stable/reference-lowlevel.html)
    - [Debugging and instrumentation](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#debugging-and-instrumentation)
    - [Low-level process spawning](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#low-level-process-spawning)
    - [Low-level I/O primitives](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#low-level-i-o-primitives)
    - [Global state: system tasks and run-local variables](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#global-state-system-tasks-and-run-local-variables)
    - [Trio tokens](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#trio-tokens)
    - [Spawning threads](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#spawning-threads)
    - [Safer KeyboardInterrupt handling](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#safer-keyboardinterrupt-handling)
    - [Sleeping and waking](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#sleeping-and-waking)
    - [Task API](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#task-api)
    - [Using “guest mode” to run Trio on top of other event loops](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#using-guest-mode-to-run-trio-on-top-of-other-event-loops)
    - [Handing off live coroutine objects between coroutine runners](https://trio.readthedocs.io/en/stable/reference-lowlevel.html#handing-off-live-coroutine-objects-between-coroutine-runners)
- [Design and internals](https://trio.readthedocs.io/en/stable/design.html)
    - [High-level design principles](https://trio.readthedocs.io/en/stable/design.html#high-level-design-principles)
    - [User-level API principles](https://trio.readthedocs.io/en/stable/design.html#user-level-api-principles)
    - [Specific style guidelines](https://trio.readthedocs.io/en/stable/design.html#specific-style-guidelines)
    - [A brief tour of Trio’s internals](https://trio.readthedocs.io/en/stable/design.html#a-brief-tour-of-trio-s-internals)
- [Release history](https://trio.readthedocs.io/en/stable/history.html)
    - [Trio 0.22.2 (2023-07-13)](https://trio.readthedocs.io/en/stable/history.html#trio-0-22-2-2023-07-13)
    - [Trio 0.22.1 (2023-07-02)](https://trio.readthedocs.io/en/stable/history.html#trio-0-22-1-2023-07-02)
    - [Trio 0.22.0 (2022-09-28)](https://trio.readthedocs.io/en/stable/history.html#trio-0-22-0-2022-09-28)
    - [Trio 0.21.0 (2022-06-07)](https://trio.readthedocs.io/en/stable/history.html#trio-0-21-0-2022-06-07)
    - [Trio 0.20.0 (2022-02-21)](https://trio.readthedocs.io/en/stable/history.html#trio-0-20-0-2022-02-21)
    - [Trio 0.19.0 (2021-06-15)](https://trio.readthedocs.io/en/stable/history.html#trio-0-19-0-2021-06-15)
    - [Trio 0.18.0 (2021-01-11)](https://trio.readthedocs.io/en/stable/history.html#trio-0-18-0-2021-01-11)
    - [Trio 0.17.0 (2020-09-15)](https://trio.readthedocs.io/en/stable/history.html#trio-0-17-0-2020-09-15)
    - [Trio 0.16.0 (2020-06-10)](https://trio.readthedocs.io/en/stable/history.html#trio-0-16-0-2020-06-10)
    - [Trio 0.15.1 (2020-05-22)](https://trio.readthedocs.io/en/stable/history.html#trio-0-15-1-2020-05-22)
    - [Trio 0.15.0 (2020-05-19)](https://trio.readthedocs.io/en/stable/history.html#trio-0-15-0-2020-05-19)
    - [Trio 0.14.0 (2020-04-27)](https://trio.readthedocs.io/en/stable/history.html#trio-0-14-0-2020-04-27)
    - [Trio 0.13.0 (2019-11-02)](https://trio.readthedocs.io/en/stable/history.html#trio-0-13-0-2019-11-02)
    - [Trio 0.12.1 (2019-08-01)](https://trio.readthedocs.io/en/stable/history.html#trio-0-12-1-2019-08-01)
    - [Trio 0.12.0 (2019-07-31)](https://trio.readthedocs.io/en/stable/history.html#trio-0-12-0-2019-07-31)
    - [Trio 0.11.0 (2019-02-09)](https://trio.readthedocs.io/en/stable/history.html#trio-0-11-0-2019-02-09)
    - [Trio 0.10.0 (2019-01-07)](https://trio.readthedocs.io/en/stable/history.html#trio-0-10-0-2019-01-07)
    - [Trio 0.9.0 (2018-10-12)](https://trio.readthedocs.io/en/stable/history.html#trio-0-9-0-2018-10-12)
    - [Trio 0.8.0 (2018-10-01)](https://trio.readthedocs.io/en/stable/history.html#trio-0-8-0-2018-10-01)
    - [Trio 0.7.0 (2018-09-03)](https://trio.readthedocs.io/en/stable/history.html#trio-0-7-0-2018-09-03)
    - [Trio 0.6.0 (2018-08-13)](https://trio.readthedocs.io/en/stable/history.html#trio-0-6-0-2018-08-13)
    - [Trio 0.5.0 (2018-07-20)](https://trio.readthedocs.io/en/stable/history.html#trio-0-5-0-2018-07-20)
    - [Trio 0.4.0 (2018-04-10)](https://trio.readthedocs.io/en/stable/history.html#trio-0-4-0-2018-04-10)
    - [Trio 0.3.0 (2017-12-28)](https://trio.readthedocs.io/en/stable/history.html#trio-0-3-0-2017-12-28)
    - [Trio 0.2.0 (2017-12-06)](https://trio.readthedocs.io/en/stable/history.html#trio-0-2-0-2017-12-06)
    - [Trio 0.1.0 (2017-03-10)](https://trio.readthedocs.io/en/stable/history.html#trio-0-1-0-2017-03-10)
- [Contributing to Trio and related projects](https://trio.readthedocs.io/en/stable/contributing.html)
    - [Getting started](https://trio.readthedocs.io/en/stable/contributing.html#getting-started)
    - [Providing support](https://trio.readthedocs.io/en/stable/contributing.html#providing-support)
    - [Preparing pull requests](https://trio.readthedocs.io/en/stable/contributing.html#preparing-pull-requests)
    - [Joining the team](https://trio.readthedocs.io/en/stable/contributing.html#joining-the-team)
    - [Managing issues](https://trio.readthedocs.io/en/stable/contributing.html#managing-issues)
    - [Governance](https://trio.readthedocs.io/en/stable/contributing.html#governance)
- [Preparing a release](https://trio.readthedocs.io/en/stable/releasing.html)
- [Code of Conduct](https://trio.readthedocs.io/en/stable/code-of-conduct.html)
    - [When Something Happens](https://trio.readthedocs.io/en/stable/code-of-conduct.html#when-something-happens)
    - [Our Pledge](https://trio.readthedocs.io/en/stable/code-of-conduct.html#our-pledge)
    - [Our Standards](https://trio.readthedocs.io/en/stable/code-of-conduct.html#our-standards)
    - [Scope](https://trio.readthedocs.io/en/stable/code-of-conduct.html#scope)
    - [Maintainer Enforcement Process](https://trio.readthedocs.io/en/stable/code-of-conduct.html#maintainer-enforcement-process)
    - [Enforcement Examples](https://trio.readthedocs.io/en/stable/code-of-conduct.html#enforcement-examples)
    - [Attribution](https://trio.readthedocs.io/en/stable/code-of-conduct.html#attribution)

## Indices and tables[¶](https://trio.readthedocs.io/en/stable/index.html#indices-and-tables "Permalink to this heading")

- [Index](https://trio.readthedocs.io/en/stable/genindex.html)

- [Module Index](https://trio.readthedocs.io/en/stable/py-modindex.html)

- [Search Page](https://trio.readthedocs.io/en/stable/search.html)

- [Glossary](https://trio.readthedocs.io/en/stable/glossary.html#glossary)
