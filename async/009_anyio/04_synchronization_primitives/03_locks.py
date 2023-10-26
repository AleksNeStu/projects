"""
Locks are used to guard shared resources to ensure sole access to a single task at once. They function much like semaphores with a maximum value of 1, except that only the task that acquired the lock is allowed to release it.
"""
from anyio import Lock, create_task_group, sleep, run


async def use_resource(tasknum, lock):
    async with lock:
        print('Task number', tasknum, 'is now working with the shared resource')
        await sleep(1)


async def main():
    lock = Lock()
    async with create_task_group() as tg:
        for num in range(4):
            tg.start_soon(use_resource, num, lock, name=num)

run(main)