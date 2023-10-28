---
source: https://docs.python.org/3/library/asyncio.html

created: 2023-10-24T15:06:51 (UTC +02:00)

tags: []

author: 

---

# asyncio — Asynchronous I/O — Python 3.12.0 documentation
---
___

asyncio is a library to write **concurrent** code using the **async/await** syntax.

asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and
web-servers, database connection libraries, distributed task queues, etc.

asyncio is often a perfect fit for IO-bound and high-level **structured** network code.

asyncio provides a set of **high-level** APIs to:

- [run Python coroutines](https://docs.python.org/3/library/asyncio-task.html#coroutine) concurrently and have full
  control over their execution;

- perform [network IO and IPC](https://docs.python.org/3/library/asyncio-stream.html#asyncio-streams);

- control [subprocesses](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio-subprocess);

- distribute tasks via [queues](https://docs.python.org/3/library/asyncio-queue.html#asyncio-queues);

- [synchronize](https://docs.python.org/3/library/asyncio-sync.html#asyncio-sync) concurrent code;

Additionally, there are **low-level** APIs for _library and framework developers_ to:

- create and manage [event loops](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-event-loop), which
  provide asynchronous APIs
  for [`networking`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server"),
  running [`subprocesses`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec"),
  handling [`OS signals`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_signal_handler "asyncio.loop.add_signal_handler"),
  etc;

- implement efficient protocols
  using [transports](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-transports-protocols);

- [bridge](https://docs.python.org/3/library/asyncio-future.html#asyncio-futures) callback-based libraries and code with
  async/await syntax.

You can experiment with an `asyncio` concurrent context in the REPL:

\>>>

```
$ python -m asyncio
asyncio REPL ...
Use "await" directly instead of "asyncio.run()".
Type "help", "copyright", "credits" or "license" for more information.
>>> import asyncio
>>> await asyncio.sleep(10, result='hello')
'hello'

```

[Availability](https://docs.python.org/3/library/intro.html#availability): not Emscripten, not WASI.

This module does not work or is not available on WebAssembly platforms `wasm32-emscripten` and `wasm32-wasi`.
See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.

Reference

Note

The source code for asyncio can be found in [Lib/asyncio/](https://github.com/python/cpython/tree/3.12/Lib/asyncio/).
