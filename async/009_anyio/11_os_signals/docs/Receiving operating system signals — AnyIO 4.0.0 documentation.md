---
source: https://anyio.readthedocs.io/en/stable/signals.html

created: 2023-10-28T19:36:54 (UTC +02:00)

tags: []

author: 

---

# Receiving operating system signals — AnyIO 4.0.0 documentation
---
You may occasionally find it useful to receive signals sent to your application in a meaningful way. For example, when
you receive a `signal.SIGTERM` signal, your application is expected to shut down gracefully. Likewise, `SIGHUP` is often
used as a means to ask the application to reload its configuration.

AnyIO provides a simple mechanism for you to receive the signals you’re interested in:

```
import signal

from anyio import open_signal_receiver, run


async def main():
    with open_signal_receiver(signal.SIGTERM, signal.SIGHUP) as signals:
        async for signum in signals:
            if signum == signal.SIGTERM:
                return
            elif signum == signal.SIGHUP:
                print('Reloading configuration')

run(main)

```

Note

Signal handlers can only be installed in the main thread, so they will not work when the event loop is being run
through [`BlockingPortal`](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.BlockingPortal "anyio.from_thread.BlockingPortal"),
for instance.

Note

Windows does not natively support signals so do not rely on this in a cross platform application.

## Handling KeyboardInterrupt and SystemExit[¶](https://anyio.readthedocs.io/en/stable/signals.html#handling-keyboardinterrupt-and-systemexit "Link to this heading")

By default, different backends handle the Ctrl+C (or Ctrl+Break on Windows) key combination and external
termination ([`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.11)")
and [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "(in Python v3.11)"), respectively)
differently: Trio raises the relevant exception inside the application while asyncio shuts down all the tasks and exits.
If you need to do your own cleanup in these situations, you will need to install a signal handler:

```
import signal

from anyio import open_signal_receiver, create_task_group, run
from anyio.abc import CancelScope


async def signal_handler(scope: CancelScope):
    with open_signal_receiver(signal.SIGINT, signal.SIGTERM) as signals:
        async for signum in signals:
            if signum == signal.SIGINT:
                print('Ctrl+C pressed!')
            else:
                print('Terminated!')

            scope.cancel()
            return


async def main():
    async with create_task_group() as tg:
        tg.start_soon(signal_handler, tg.cancel_scope)
        ...  # proceed with starting the actual application logic

run(main)

```

Note

Windows does not support
the [`SIGTERM`](https://docs.python.org/3/library/signal.html#signal.SIGTERM "(in Python v3.11)") signal so if you need
a mechanism for graceful shutdown on Windows, you will have to find another way.
