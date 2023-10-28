"""
A condition is basically a combination of an event and a lock. It first acquires a lock and then waits for a
notification from the event. Once the condition receives a notification, it releases the lock. The notifying task can
also choose to wake up more than one listener at once, or even all of them.

Like Lock, Condition also requires that the task which locked it also the one to release it.
"""
from anyio import Condition, create_task_group, sleep, run


async def listen(tasknum, condition):
    async with condition:
        await condition.wait()
        print('Woke up task number', tasknum)


async def main():
    condition = Condition()
    async with create_task_group() as tg:
        for tasknum in range(6):
            tg.start_soon(listen, tasknum, condition)

        await sleep(2)
        async with condition:
            condition.notify(1)

        await sleep(2)
        async with condition:
            condition.notify(2)

        await sleep(2)
        async with condition:
            condition.notify_all()


run(main)
