"""
Spawning tasks from worker threads
When you need to spawn a task to be run in the background, you can do so using start_task_soon():
"""
from concurrent.futures import as_completed

from anyio import sleep
from anyio.from_thread import start_blocking_portal


async def long_running_task(index):
    await sleep(1)
    print(f'Task {index} running...')
    await sleep(index)
    return f'Task {index} return value'


with start_blocking_portal() as portal:
    futures = [portal.start_task_soon(long_running_task, i) for i in range(1, 5)]
    for future in as_completed(futures):
        print(future.result())

"""
Cancelling tasks spawned this way can be done by cancelling the returned Future.

Blocking portals also have a method similar to TaskGroup.start(): start_task() which, like its counterpart, 
waits for the callable to signal readiness by calling task_status.started():
"""
from anyio import sleep, TASK_STATUS_IGNORED
from anyio.from_thread import start_blocking_portal


async def service_task(*, task_status=TASK_STATUS_IGNORED):
    task_status.started('STARTED')
    await sleep(1)
    return 'DONE'


with start_blocking_portal() as portal:
    future, start_value = portal.start_task(service_task)
    print('Task has started with value', start_value)

    return_value = future.result()
    print('Task has finished with return value', return_value)
