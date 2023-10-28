"""
Practical asynchronous applications occasionally need to run network, file or computationally expensive operations. Such operations would normally block the asynchronous event loop, leading to performance issues. The solution is to run such code in worker threads. Using worker threads lets the event loop continue running other tasks while the worker thread runs the blocking call.

Running a function in a worker thread
To run a (synchronous) callable in a worker thread:
"""

import time

from anyio import to_thread, run


async def main():
    await to_thread.run_sync(time.sleep, 5)

run(main)
