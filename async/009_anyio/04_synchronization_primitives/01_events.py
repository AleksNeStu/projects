"""
Synchronization primitives are objects that are used by tasks to communicate and coordinate with each other. They are useful for things like distributing workload, notifying other tasks and guarding access to shared resources.

Note AnyIO primitives are not thread-safe, therefore they should not be used directly from worker threads. Use run_sync() for that.

Events are used to notify tasks that something they’ve been waiting to happen has happened. An event object can have multiple listeners and they are all notified when the event is triggered.

"""
from anyio import Event, create_task_group, run, sleep

from common.utils import timer_dc


@timer_dc
async def notify(event):
    await sleep(1.5)
    event.set()

async def ger_notification(event):
    await event.wait()
    print('Received notification!')

async def main():
    event = Event()
    async with create_task_group() as tg:
        tg.start_soon(notify, event)
        tg.start_soon(ger_notification, event)


run(main)


"""
Note Unlike standard library Events, AnyIO events cannot be reused, and must be replaced instead. This practice prevents a class of race conditions, and matches the semantics of the Trio library.
"""