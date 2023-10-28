import asyncio

import anyio
import trio

from common.utils import timer_dc, w_err

"""
Similarly, the nursery pattern creates semantic improvement via explicit lifetime representation of async tasks. This 
relatively new concept is often referred to as structured concurrenc

"""

"""
Now, let us return to the world of Python, where the majority of async libraries—and therefore applications using 
them—only aim for asyncio compatibility. One may rightfully question the practicality of Trio’s nurseries in such an 
ecosystem, apart from a theoretical proof of concept. Fortunately, the amazing AnyIO project implements structured 
concurrency on top of asyncio, making it available for widespread use.

"""


@timer_dc
async def child1_as(delay: int):
    print("child1 start")
    await asyncio.sleep(delay)
    print("child1 done")


@timer_dc
async def child2_as(delay: int):
    print("child2 start")
    await asyncio.sleep(delay)
    print("child2 done")


async def parent_as():
    print("parent start")
    async with asyncio.TaskGroup() as tg:
        # When the context manager exits, it waits for all tasks in the group to complete. While waiting,
        # we can still add new tasks to TaskGroup.
        tg.create_task(child1_as())
        tg.create_task(child2_as())
        # Note that assuming that a task in the group throws an exception other than asyncio.CancelledError while
        # waiting, all other tasks in the group will be canceled.
        #
        # Also, all exceptions were thrown except for asyncio.CanceledError will be combined and thrown in the
        # ExceptionGroup.

    print("parent done")


@timer_dc
async def timeout1():
    "Run timeout. asyncio.timeout is also created using the asynchronous context manager. It limits the execution
    time of concurrent code in a context."
    with w_err({TimeoutError: None}):
        await asyncio.wait_for(child1_as(delay=2), timeout=1)


# asyncio.run(timeout1())
"""
child1 start
Async func `child1_as` elapsed time: 1.000689 s
Func: `timeout1`, exception: `TimeoutError()` was caught, not raised
Async func `timeout1` elapsed time: 1.021242 s
"""

"""
But when it is necessary to set a uniform timeout for multiple concurrent calls, things will become problematic. 
Let’s assume we have two concurrent tasks and want them to run to completion in 8 seconds. Let’s try to assign an 
average timeout of 4 seconds to each task, with code like the following:

You can see that although we set an average timeout for each concurrent method, such a setting may cause 
uncontrollable situations since each call to the IO-bound task is not guaranteed to return simultaneously, 
and we still got a TimeoutError.

At this point, we use the asyncio.timeout block to ensure that we set an overall timeout for all concurrent tasks:
"""


@timer_dc
async def timeout2():
    with w_err({TimeoutError: None}):
        print("parent start")
        # At this point, we use the asyncio.timeout block to ensure that we set an overall timeout for all concurrent
        # tasks:
        async with asyncio.timeout(delay=1):
            async with asyncio.TaskGroup() as tg:
                tg.create_task(child1_as(delay=1))
                tg.create_task(child2_as(delay=2))
        print("parent done")


# asyncio.run(timeout2())
"""
parent start
child1 start
child2 start
Async func `child1_as` elapsed time: 1.000847 s
Async func `child2_as` elapsed time: 1.000869 s
Func: `timeout2`, exception: `TimeoutError()` was caught, not raised
Async func `timeout2` elapsed time: 1.019755 s
"""

# Structured Concurrency
"""
What is Structured Concurrency
TaskGroup and asyncio.timeout above uses the async with feature. Just like with struct block can manage the life 
cycle of resources uniformly like this

"""


# TaskGroup and asyncio.timeout above uses the async with feature. Just like with struct block can manage the life
# cycle of resources uniformly like this:

def main1():
    with open("hello.txt", "w") as f:
        f.write("hello world.")


# But calling concurrent tasks inside with block does not work because the concurrent task will continue executing in
# the background while the with block has already exited, which will lead to improper closure of the resource:

async def file_coro(f):
    await asyncio.sleep(5)
    f.write("hello world.")


async def main2():
    with open("hello.txt", "w") as f:
        # This will result in nothing being written to the file
        asyncio.create_task(file_coro(f))
        # Do some other things.


# Therefore, we introduced the async with feature here. As with, async with and TaskGroup Is used to manage the life
# cycle of concurrent code uniformly, thus making the code clear and saving development time. We call this feature
# our main character today:


# asyncio.gather
"""
Some readers say that asyncio.gather could be responsible for joining all the background tasks. But asyncio.gather it 
has its problems:

It cannot centrally manage backend tasks in a unified way. Often creating backend tasks in one place and calling 
asyncio.gather in another.
The argument aws received by asyncio.gather is a fixed list, which means that we have set the number of background 
tasks when asyncio.gather is called, and they cannot be added randomly on the way to waiting.
When a task is waiting in asyncio.gather throws an exception, it cannot cancel other tasks that are executing, 
which may cause some tasks to run indefinitely in the background and the program to die falsely.
Therefore, the Structured Concurrency feature introduced in Python 3.11 is an excellent solution to our concurrency 
problems. It allows the related asynchronous code to all finish executing in the same place, and at the same time, 
it will enable tg instances to be passed as arguments to background tasks, so that new background tasks created in 
the background tasks will not jump out of the current life cycle management of the asynchronous context.


"""


async def child1(delay: int):
    print("child1 start")
    await trio.sleep(delay)
    print("child1 done")


async def child2(delay: int):
    print("child2 start")
    await trio.sleep(delay)
    print("child2 done")


# 1) Nurseries in Trio
async def main_trio():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(child1, 1)
        nursery.start_soon(child2, 2)
    print("All tasks done.")


# trio.run(main_trio)

# 2) create_task_group in Anyio
"""
But with the advent of the official Python asyncio package, more and more third-party packages are using asyncio to 
implement concurrent programming. At this point, using Trio will inevitably run into compatibility problems.

At this point, Anyio, which claims to be compatible with both asyncio and Trio, emerged. It can also implement 
Structured Concurrency through the create_task_group API
"""


async def some_task(num: int = 0):
    print(f"Task {num} running")
    await anyio.sleep(num)
    print(f"Task {num} finished")


async def main_anyio():
    # NOTE: TrioDeprecationWarning: trio.MultiError is deprecated since Trio 0.22.0; use BaseExceptionGroup (on Python
    # 3.11 and later) or exceptiongroup.BaseExceptionGroup (earlier versions) instead (
    # https://github.com/python-trio/trio/issues/2211)
    #   class ExceptionGroup(BaseExceptionGroup, trio.MultiError):
    async with anyio.create_task_group() as tg:
        tg.start_soon(child1, 1)
        # tg.start_soon(child1_as, 1)
        for num in range(5):
            tg.start_soon(some_task, num)
    print("All tasks finished!")


anyio.run(main_anyio, backend="trio")
