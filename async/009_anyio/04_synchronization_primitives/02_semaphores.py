"""
Semaphores are used for limiting access to a shared resource. A semaphore starts with a maximum value, which is decremented each time the semaphore is acquired by a task and incremented when it is released. If the value drops to zero, any attempt to acquire the semaphore will block until another task frees it.

"""

from anyio import Semaphore, create_task_group, sleep, run


async def use_resource(tasknum, semaphore):
    async with semaphore:
        print('Task number', tasknum, 'is now working with the shared resource')
        await sleep(1)
        # await semaphore.acquire()


async def main():
    semaphore = Semaphore(3)
    async with create_task_group() as tg:
        for num in range(10):
            tg.start_soon(use_resource, num, semaphore, name="test")

    f = 1

run(main)