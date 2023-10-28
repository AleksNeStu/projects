"""
Calling synchronous code from a worker thread
Occasionally you may need to call synchronous code in the event loop thread from a worker thread. Common cases
include setting asynchronous events or sending data to a memory object stream. Because these methods aren’t thread
safe, you need to arrange them to be called inside the event loop thread using run_sync():
"""
import time

from anyio import Event, from_thread, to_thread, run


def worker(event):
    time.sleep(1)
    from_thread.run_sync(event.set)


async def main():
    event = Event()
    await to_thread.run_sync(worker, event)
    await event.wait()


run(main)
