"""
Approach taken by Trio, an alternative async Python framework.
"""

import trio

"""
In trio nurseries are context managers that expose an interface similar to asyncio.create_task.

Trio ensures that the async with block will not exit until both tasks have completed. Arbitrary computation, including await statements, can be done before, in-between, and after task creation. To aid with this, nurseries also offer a blocking start call, which allows waiting for a task to initialize but not finish. For example, we may want to wait for a consumer task to establish connection to a message broker before proceeding with a corresponding producer task. Arbitrary nesting is allowed—tasks can open their own nurseries internally, which creates a hierarchical structure with clearly defined parent-child relationships. To retrieve return values from tasks, it is common to use a shared object, such as an async-ready queue or a plain dictionary.

 In many cases, however, tasks primarily need to pass information between one another, which is commonly achieved by passing a shared queue reference, as seen in the example.
"""
async def child1():
    print("child1 start")
    await trio.sleep(1)
    print("child1 done")

async def child2():
    print("child2 start")
    await trio.sleep(2)
    print("child2 done")


async def parent():
    print("parent start")
    # Trio ensures that the async with block will not exit until both tasks have completed.
    async with trio.open_nursery() as nursery:
        nursery.start_soon(child1)
        nursery.start_soon(child2)
        print("parent wait for childs")

    print("parent done")


trio.run(parent)

