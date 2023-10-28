"""
Calling asynchronous code from a worker thread
If you need to call a coroutine function from a worker thread, you can do th
Note The worker thread must have been spawned using run_sync() for this to work.

"""
from anyio import from_thread, sleep, to_thread, run


def blocking_function():
    from_thread.run(sleep, 5)


async def main():
    await to_thread.run_sync(blocking_function)

run(main)