"""
Capacity limiters are like semaphores except that a single borrower (the current task by default) can only hold a
single token at a time. It is also possible to borrow a token on behalf of any arbitrary object, so long as that
object is hashable.

You can adjust the total number of tokens by setting a different value on the limiter’s total_tokens property
"""

from anyio import CapacityLimiter, create_task_group, sleep, run


async def use_resource(tasknum, limiter):
    async with limiter:
        print('Task number', tasknum, 'is now working with the shared resource')
        await sleep(1)


async def main():
    limiter = CapacityLimiter(3)
    async with create_task_group() as tg:
        for num in range(15):
            tg.start_soon(use_resource, num, limiter)


run(main)
