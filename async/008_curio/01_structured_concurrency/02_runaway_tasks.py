"""
Coroutines differ from threads in that they implement cooperative multitasking—they must yield control or suspend explicitly (e.g. via a yield or await statement). This means that the programmer is always aware of a potential context switch and is able to arrange a graceful and safe suspension.


Despite the convenience of coroutine-based concurrency, Python's asyncio module has long lacked an intuitive and convenient way to manage groups of concurrently running tasks. The current API revolves around create_task, which returns a task handle to the user. The user is then responsible for keeping references to running tasks, collecting return values, and handling safe cancellation in case of errors. This is notoriously difficult and prone to errors. The lack of correct task management leads to runaway tasks, which never get awaited by the parent or checked for exceptions. As a result, the program can easily end up in an invalid state while failing to emit any kind of error or warning.
"""
import asyncio
from asyncio import create_task


async def child1():
    print("child1 start")
    await asyncio.sleep(1)
    print("child1 done")

async def child2():
    print("child2 start")
    await asyncio.sleep(2)
    print("child2 done")


async def fn():
    # The lack of correct task management leads to runaway tasks, which never get awaited by the parent or checked for exceptions.
    create_task(child1())
    create_task(child2())
    # Arbitrary computation here. return await task_a


asyncio.run(fn())

"""
The parent task spawns two child tasks, A and B, and lets them run in the background. Eventually, it awaits the completion of A. Once A is done, it either produces a return value or propagates an exception into the call stack. However, B is never awaited, which is not strictly wrong, but it exposes us to the following scenarios:

The task dies without our knowledge. Seemingly unrelated code may deadlock or start misbehaving, as it assumes that the task is running in the background.
We expect the task to have ended, but a bug in its termination logic makes it run silently in the background, causing unexpected behavior elsewhere.
Both situations are nightmares to debug. Once the example function exits, B becomes orphaned—we lose our reference to the task and are no longer able to manage its lifetime.
"""