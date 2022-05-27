import asyncio

from unsync import unsync
from codetiming import Timer
import time

# unsync
# Unsynchronize asyncio by using an ambient event loop, or executing in separate threads or processes.
#
# Quick Overview
# Functions marked with the @unsync decorator will behave in one of the following ways:
#
# async functions will run in the unsync.loop event loop executed from unsync.thread
# Regular functions will execute in unsync.thread_executor, a ThreadPoolExecutor
# Useful for IO bounded work that does not support asyncio
# Regular functions marked with @unsync(cpu_bound=True) will execute in unsync.process_executor, a ProcessPoolExecutor
# Useful for CPU bounded work
# All @unsync functions will return an Unfuture object. This new future type combines the behavior of asyncio.Future and concurrent.Future with the following changes:
#
# Unfuture.set_result is threadsafe unlike asyncio.Future
# Unfuture instances can be awaited, even if made from concurrent.Future
# Unfuture.result() is a blocking operation except in unsync.loop/unsync.thread where it behaves like asyncio.Future.result and will throw an exception if the future is not done

# Executing an async function outside of an existing event loop is troublesome
# * asyncio.Future is not thread safe
# * concurrent.Future's cannot be directly awaited
# * Future.result() is a blocking operation even within an event loop
# * asyncio.Future.result() will throw an exception if the future is not done
# * async Functions always execute in the asyncio loop (not thread or process backed)
# * Cancellation and timeouts are tricky in threads and processes
# * Executing an async function outside of an existing event loop is troublesome
# * Testing is hard

# 1) Example with asyncio (loop):
async def sync_async():
    await asyncio.sleep(1)
    return 'I hate event loops'


async def main():
    future1 = asyncio.create_task(sync_async())
    future2 = asyncio.create_task(sync_async())

    await future1, future2

    print(future1.result() + future2.result())

with Timer(text=f"asyncio (loop): {{:.4f}}"):
    asyncio.run(main())
# Takes 1 second to run

# 2) Example with unsync (loop):
@unsync
async def unsync_async():
    await asyncio.sleep(1)
    return 'I like decorators'

with Timer(text=f"unsync (loop): {{:.4f}}"):
    unfuture1 = unsync_async()
    unfuture2 = unsync_async()
    print(unfuture1.result() + unfuture2.result())
    # Takes 1 second to run

# 3) Example with unsync (thread_executor):
@unsync
def non_async_function(seconds):
    time.sleep(seconds)
    return 'Run concurrently!'

with Timer(text=f"unsync (thread_executor): {{:.4f}}"):
    tasks = [non_async_function(0.1) for _ in range(10)]
    print([task.result() for task in tasks])

# 4) Example with unsync (process_executor):
@unsync
def non_async_function(seconds):
    time.sleep(seconds)
    return 'Run concurrently!'

with Timer(text=f"unsync (thread_executor): {{:.4f}}"):
    tasks = [non_async_function(0.1) for _ in range(10)]
    print([task.result() for task in tasks])


# 5) Unfuture.then
@unsync
async def initiate(request):
    await asyncio.sleep(0.1)
    return request + 1

@unsync
async def process(task):
    await asyncio.sleep(0.1)
    return task * 2

with Timer(text=f"Unfuture.then: {{:.4f}}"):
    res = initiate(3).then(process)
    print(res.result())


# 6) Mixin
import unsync
import uvloop

@unsync
async def main():
        # Main entry-point.
        return

uvloop.install() # Equivalent to asyncio.set_event_loop_policy(EventLoopPolicy())
main()