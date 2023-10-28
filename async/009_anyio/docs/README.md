[![Build Status](https://github.com/agronholm/anyio/actions/workflows/test.yml/badge.svg)](https://github.com/agronholm/anyio/actions/workflows/test.yml)

[![Code Coverage](https://coveralls.io/repos/github/agronholm/anyio/badge.svg?branch=master)](https://coveralls.io/github/agronholm/anyio?branch=master)

[![Documentation](https://readthedocs.org/projects/anyio/badge/?version=latest)](https://anyio.readthedocs.io/en/latest/?badge=latest)

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.svg)](https://gitter.im/python-trio/AnyIO)

AnyIO is an asynchronous networking and concurrency library that works
on top of either
[asyncio](https://docs.python.org/3/library/asyncio.html) or
[trio](https://github.com/python-trio/trio). It implements trio-like
[structured
concurrency](https://en.wikipedia.org/wiki/Structured_concurrency) (SC)
on top of asyncio and works in harmony with the native SC of trio
itself.

Applications and libraries written against AnyIO\'s API will run
unmodified on either
[asyncio](https://docs.python.org/3/library/asyncio.html) or
[trio](https://github.com/python-trio/trio). AnyIO can also be adopted
into a library or application incrementally -- bit by bit, no full
refactoring necessary. It will blend in with the native libraries of
your chosen backend.

# Documentation

View full documentation at: <https://anyio.readthedocs.io/>

# Features

AnyIO offers the following functionality:

- Task groups
  ([nurseries](https://trio.readthedocs.io/en/stable/reference-core.html#nurseries-and-spawning)
  in trio terminology)
- High-level networking (TCP, UDP and UNIX sockets)
    - [Happy eyeballs](https://en.wikipedia.org/wiki/Happy_Eyeballs)
      algorithm for TCP connections (more robust than that of asyncio
      on Python 3.8)
    - async/await style UDP sockets (unlike asyncio where you still
      have to use Transports and Protocols)
- A versatile API for byte streams and object streams
- Inter-task synchronization and communication (locks, conditions,
  events, semaphores, object streams)
- Worker threads
- Subprocesses
- Asynchronous file I/O (using worker threads)
- Signal handling

AnyIO also comes with its own
[pytest](https://docs.pytest.org/en/latest/) plugin which also supports
asynchronous fixtures. It even works with the popular
[Hypothesis](https://hypothesis.works/) library.
