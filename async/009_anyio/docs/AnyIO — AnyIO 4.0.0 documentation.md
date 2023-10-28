---
source: https://anyio.readthedocs.io/en/stable/index.html

created: 2023-10-28T19:53:05 (UTC +02:00)

tags: []

author: 

---

# AnyIO — AnyIO 4.0.0 documentation
---
[![Build Status](https://github.com/agronholm/anyio/actions/workflows/test.yml/badge.svg)](https://github.com/agronholm/anyio/actions/workflows/test.yml) [![Code Coverage](https://coveralls.io/repos/github/agronholm/anyio/badge.svg?branch=master)](https://coveralls.io/github/agronholm/anyio?branch=master) [![Documentation](https://readthedocs.org/projects/anyio/badge/?version=latest)](https://anyio.readthedocs.io/en/latest/?badge=latest) [![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.svg)](https://gitter.im/python-trio/AnyIO)

AnyIO is an asynchronous networking and concurrency library that works on top of
either [asyncio](https://docs.python.org/3/library/asyncio.html) or [trio](https://github.com/python-trio/trio). It
implements trio-like [structured concurrency](https://en.wikipedia.org/wiki/Structured_concurrency) (SC) on top of
asyncio and works in harmony with the native SC of trio itself.

Applications and libraries written against AnyIO’s API will run unmodified on
either [asyncio](https://docs.python.org/3/library/asyncio.html) or [trio](https://github.com/python-trio/trio). AnyIO
can also be adopted into a library or application incrementally – bit by bit, no full refactoring necessary. It will
blend in with the native libraries of your chosen backend.

## Documentation[¶](https://anyio.readthedocs.io/en/stable/index.html#documentation "Link to this heading")

View full documentation at: [https://anyio.readthedocs.io/](https://anyio.readthedocs.io/)

## Features[¶](https://anyio.readthedocs.io/en/stable/index.html#features "Link to this heading")

AnyIO offers the following functionality:

- Task groups ([nurseries](https://trio.readthedocs.io/en/stable/reference-core.html#nurseries-and-spawning) in trio
  terminology)

- High-level networking (TCP, UDP and UNIX sockets)

    - [Happy eyeballs](https://en.wikipedia.org/wiki/Happy_Eyeballs) algorithm for TCP connections (more robust than
      that of asyncio on Python 3.8)

    - async/await style UDP sockets (unlike asyncio where you still have to use Transports and Protocols)

- A versatile API for byte streams and object streams

- Inter-task synchronization and communication (locks, conditions, events, semaphores, object streams)

- Worker threads

- Subprocesses

- Asynchronous file I/O (using worker threads)

- Signal handling

AnyIO also comes with its own [pytest](https://docs.pytest.org/en/latest/) plugin which also supports asynchronous
fixtures. It even works with the popular [Hypothesis](https://hypothesis.works/) library.

## The manual[¶](https://anyio.readthedocs.io/en/stable/index.html#the-manual "Link to this heading")

- [The basics](https://anyio.readthedocs.io/en/stable/basics.html)
    - [Installation](https://anyio.readthedocs.io/en/stable/basics.html#installation)
    - [Running async programs](https://anyio.readthedocs.io/en/stable/basics.html#running-async-programs)
    - [Backend specific options](https://anyio.readthedocs.io/en/stable/basics.html#backend-specific-options)
    - [Using native async libraries](https://anyio.readthedocs.io/en/stable/basics.html#using-native-async-libraries)
- [Creating and managing tasks](https://anyio.readthedocs.io/en/stable/tasks.html)
    - [Starting and initializing tasks](https://anyio.readthedocs.io/en/stable/tasks.html#starting-and-initializing-tasks)
    - [Handling multiple errors in a task group](https://anyio.readthedocs.io/en/stable/tasks.html#handling-multiple-errors-in-a-task-group)
    - [Context propagation](https://anyio.readthedocs.io/en/stable/tasks.html#context-propagation)
    - [Differences with asyncio.TaskGroup](https://anyio.readthedocs.io/en/stable/tasks.html#differences-with-asyncio-taskgroup)
- [Cancellation and timeouts](https://anyio.readthedocs.io/en/stable/cancellation.html)
    - [Timeouts](https://anyio.readthedocs.io/en/stable/cancellation.html#timeouts)
    - [Shielding](https://anyio.readthedocs.io/en/stable/cancellation.html#shielding)
    - [Finalization](https://anyio.readthedocs.io/en/stable/cancellation.html#finalization)
    - [Avoiding cancel scope stack corruption](https://anyio.readthedocs.io/en/stable/cancellation.html#avoiding-cancel-scope-stack-corruption)
- [Using synchronization primitives](https://anyio.readthedocs.io/en/stable/synchronization.html)
    - [Events](https://anyio.readthedocs.io/en/stable/synchronization.html#events)
    - [Semaphores](https://anyio.readthedocs.io/en/stable/synchronization.html#semaphores)
    - [Locks](https://anyio.readthedocs.io/en/stable/synchronization.html#locks)
    - [Conditions](https://anyio.readthedocs.io/en/stable/synchronization.html#conditions)
    - [Capacity limiters](https://anyio.readthedocs.io/en/stable/synchronization.html#capacity-limiters)
- [Streams](https://anyio.readthedocs.io/en/stable/streams.html)
    - [Memory object streams](https://anyio.readthedocs.io/en/stable/streams.html#memory-object-streams)
    - [Stapled streams](https://anyio.readthedocs.io/en/stable/streams.html#stapled-streams)
    - [Buffered byte streams](https://anyio.readthedocs.io/en/stable/streams.html#buffered-byte-streams)
    - [Text streams](https://anyio.readthedocs.io/en/stable/streams.html#text-streams)
    - [File streams](https://anyio.readthedocs.io/en/stable/streams.html#file-streams)
    - [TLS streams](https://anyio.readthedocs.io/en/stable/streams.html#tls-streams)
- [Using typed attributes](https://anyio.readthedocs.io/en/stable/typedattrs.html)
    - [Defining your own typed attributes](https://anyio.readthedocs.io/en/stable/typedattrs.html#defining-your-own-typed-attributes)
- [Using sockets and streams](https://anyio.readthedocs.io/en/stable/networking.html)
    - [Working with TCP sockets](https://anyio.readthedocs.io/en/stable/networking.html#working-with-tcp-sockets)
    - [Working with UNIX sockets](https://anyio.readthedocs.io/en/stable/networking.html#working-with-unix-sockets)
    - [Working with UDP sockets](https://anyio.readthedocs.io/en/stable/networking.html#working-with-udp-sockets)
    - [Working with UNIX datagram sockets](https://anyio.readthedocs.io/en/stable/networking.html#working-with-unix-datagram-sockets)
- [Working with threads](https://anyio.readthedocs.io/en/stable/threads.html)
    - [Running a function in a worker thread](https://anyio.readthedocs.io/en/stable/threads.html#running-a-function-in-a-worker-thread)
    - [Calling asynchronous code from a worker thread](https://anyio.readthedocs.io/en/stable/threads.html#calling-asynchronous-code-from-a-worker-thread)
    - [Calling synchronous code from a worker thread](https://anyio.readthedocs.io/en/stable/threads.html#calling-synchronous-code-from-a-worker-thread)
    - [Calling asynchronous code from an external thread](https://anyio.readthedocs.io/en/stable/threads.html#calling-asynchronous-code-from-an-external-thread)
    - [Spawning tasks from worker threads](https://anyio.readthedocs.io/en/stable/threads.html#spawning-tasks-from-worker-threads)
    - [Using asynchronous context managers from worker threads](https://anyio.readthedocs.io/en/stable/threads.html#using-asynchronous-context-managers-from-worker-threads)
    - [Context propagation](https://anyio.readthedocs.io/en/stable/threads.html#context-propagation)
    - [Adjusting the default maximum worker thread count](https://anyio.readthedocs.io/en/stable/threads.html#adjusting-the-default-maximum-worker-thread-count)
- [Using subprocesses](https://anyio.readthedocs.io/en/stable/subprocesses.html)
    - [Running one-shot commands](https://anyio.readthedocs.io/en/stable/subprocesses.html#running-one-shot-commands)
    - [Working with processes](https://anyio.readthedocs.io/en/stable/subprocesses.html#working-with-processes)
    - [Running functions in worker processes](https://anyio.readthedocs.io/en/stable/subprocesses.html#running-functions-in-worker-processes)
- [Asynchronous file I/O support](https://anyio.readthedocs.io/en/stable/fileio.html)
    - [Asynchronous path operations](https://anyio.readthedocs.io/en/stable/fileio.html#asynchronous-path-operations)
- [Receiving operating system signals](https://anyio.readthedocs.io/en/stable/signals.html)
    - [Handling KeyboardInterrupt and SystemExit](https://anyio.readthedocs.io/en/stable/signals.html#handling-keyboardinterrupt-and-systemexit)
- [Testing with AnyIO](https://anyio.readthedocs.io/en/stable/testing.html)
    - [Creating asynchronous tests](https://anyio.readthedocs.io/en/stable/testing.html#creating-asynchronous-tests)
    - [Specifying the backends to run on](https://anyio.readthedocs.io/en/stable/testing.html#specifying-the-backends-to-run-on)
    - [Asynchronous fixtures](https://anyio.readthedocs.io/en/stable/testing.html#asynchronous-fixtures)
    - [Using async fixtures with higher scopes](https://anyio.readthedocs.io/en/stable/testing.html#using-async-fixtures-with-higher-scopes)
    - [Technical details](https://anyio.readthedocs.io/en/stable/testing.html#technical-details)
- [API reference](https://anyio.readthedocs.io/en/stable/api.html)
    - [Event loop](https://anyio.readthedocs.io/en/stable/api.html#event-loop)
    - [Asynchronous resources](https://anyio.readthedocs.io/en/stable/api.html#asynchronous-resources)
    - [Typed attributes](https://anyio.readthedocs.io/en/stable/api.html#typed-attributes)
    - [Timeouts and cancellation](https://anyio.readthedocs.io/en/stable/api.html#timeouts-and-cancellation)
    - [Task groups](https://anyio.readthedocs.io/en/stable/api.html#task-groups)
    - [Running code in worker threads](https://anyio.readthedocs.io/en/stable/api.html#running-code-in-worker-threads)
    - [Running code in worker processes](https://anyio.readthedocs.io/en/stable/api.html#running-code-in-worker-processes)
    - [Running asynchronous code from other threads](https://anyio.readthedocs.io/en/stable/api.html#running-asynchronous-code-from-other-threads)
    - [Async file I/O](https://anyio.readthedocs.io/en/stable/api.html#async-file-i-o)
    - [Streams and stream wrappers](https://anyio.readthedocs.io/en/stable/api.html#streams-and-stream-wrappers)
    - [Sockets and networking](https://anyio.readthedocs.io/en/stable/api.html#sockets-and-networking)
    - [Subprocesses](https://anyio.readthedocs.io/en/stable/api.html#subprocesses)
    - [Synchronization](https://anyio.readthedocs.io/en/stable/api.html#synchronization)
    - [Operating system signals](https://anyio.readthedocs.io/en/stable/api.html#operating-system-signals)
    - [Low level operations](https://anyio.readthedocs.io/en/stable/api.html#low-level-operations)
    - [Testing and debugging](https://anyio.readthedocs.io/en/stable/api.html#testing-and-debugging)
    - [Exceptions](https://anyio.readthedocs.io/en/stable/api.html#exceptions)
- [Migrating from AnyIO 3 to AnyIO 4](https://anyio.readthedocs.io/en/stable/migration.html)
    - [The non-standard exception group class was removed](https://anyio.readthedocs.io/en/stable/migration.html#the-non-standard-exception-group-class-was-removed)
    - [Task groups now wrap single exceptions in groups](https://anyio.readthedocs.io/en/stable/migration.html#task-groups-now-wrap-single-exceptions-in-groups)
    - [Syntax for type annotated memory object streams has changed](https://anyio.readthedocs.io/en/stable/migration.html#syntax-for-type-annotated-memory-object-streams-has-changed)
    - [Event loop factories instead of event loop policies](https://anyio.readthedocs.io/en/stable/migration.html#event-loop-factories-instead-of-event-loop-policies)
- [Migrating from AnyIO 2 to AnyIO 3](https://anyio.readthedocs.io/en/stable/migration.html#migrating-from-anyio-2-to-anyio-3)
    - [Asynchronous functions converted to synchronous](https://anyio.readthedocs.io/en/stable/migration.html#asynchronous-functions-converted-to-synchronous)
    - [Starting tasks](https://anyio.readthedocs.io/en/stable/migration.html#starting-tasks)
    - [Blocking portal changes](https://anyio.readthedocs.io/en/stable/migration.html#blocking-portal-changes)
    - [Synchronization primitives](https://anyio.readthedocs.io/en/stable/migration.html#synchronization-primitives)
    - [Threading functions moved](https://anyio.readthedocs.io/en/stable/migration.html#threading-functions-moved)
- [Frequently Asked Questions](https://anyio.readthedocs.io/en/stable/faq.html)
    - [Why is Curio not supported as a backend?](https://anyio.readthedocs.io/en/stable/faq.html#why-is-curio-not-supported-as-a-backend)
    - [Why is Twisted not supported as a backend?](https://anyio.readthedocs.io/en/stable/faq.html#why-is-twisted-not-supported-as-a-backend)
- [Getting help](https://anyio.readthedocs.io/en/stable/support.html)
- [Reporting bugs](https://anyio.readthedocs.io/en/stable/support.html#reporting-bugs)
- [Contributing to AnyIO](https://anyio.readthedocs.io/en/stable/contributing.html)
    - [Making a pull request on Github](https://anyio.readthedocs.io/en/stable/contributing.html#making-a-pull-request-on-github)
- [Version history](https://anyio.readthedocs.io/en/stable/versionhistory.html)
