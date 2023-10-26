"""
A task is a unit of execution that lets you do many things concurrently that need waiting on. This works so that while you can have any number of tasks, the asynchronous event loop can only run one of them at a time. When the task encounters an await statement that requires the task to sleep until something happens, the event loop is then free to work on another task. When the thing the first task was waiting is complete, the event loop will resume the execution of that task on the first opportunity it gets.

Task handling in AnyIO loosely follows the Trio model. Tasks can be created (spawned) using task groups. A task group is an asynchronous context manager that makes sure that all its child tasks are finished one way or another after the context block is exited. If a child task, or the code in the enclosed context block raises an exception, all child tasks are cancelled. Otherwise the context manager just waits until all child tasks have exited before proceeding.
"""

from anyio import (
    TASK_STATUS_IGNORED,
    create_task_group,
    connect_tcp,
    create_tcp_listener,
    sleep,
    run,
)
from anyio.abc import TaskStatus

from common.utils import timer_dc


# 1) Task handling in AnyIO loosely follows the Trio model.
async def sometask(num: int) -> None:
    print('Task', num, 'running')
    await sleep(1)
    print('Task', num, 'finished')


async def main_ex() -> None:
    async with create_task_group() as tg:
        for num in range(5):
            tg.start_soon(sometask, num)

    print('All tasks finished!')

#run(main_ex)

# 2) Starting and initializing tasks
"""
Sometimes it is very useful to be able to wait until a task has successfully initialized itself. For example, when starting network services, you can have your task start the listener and then signal the caller that initialization is done. That way, the caller can now start another task that depends on that service being up and running. Also, if the socket bind fails or something else goes wrong during initialization, the exception will be propagated to the caller which can then catch and handle it.

This can be done with TaskGroup.start():
"""




async def handler(stream):
    ...


async def start_some_service(
        port: int, *, task_status: TaskStatus[None] = TASK_STATUS_IGNORED
):
    async with await create_tcp_listener(
            local_host="127.0.0.1", local_port=port
    ) as listener:
        print("init start server")
        # If the spawned task never calls it, then the TaskGroup.start() call will raise a RuntimeError.
        await sleep(3)
        task_status.started()
        print(f"end start server: {handler}")
        await listener.serve(handler)



@timer_dc
async def connect_to_some_service():
    async with await connect_tcp("127.0.0.1", 5000) as stream:
        ...
        await sleep(2)
        print(f"connected to server: {stream}")

@timer_dc
async def main_start_init():
    print("start parent")
    async with create_task_group() as tg:
        # listener (consumer)
        # The target coroutine function must call task_status.started() because the task that is calling with TaskGroup.start() will be blocked until then.
        #
        # Note Unlike start_soon(), start() needs an await.
        await tg.start(start_some_service, 5000)
        tg.start_soon(connect_to_some_service)
        # lsof -i:5000
        # COMMAND    PID USER   FD   TYPE   DEVICE SIZE/OFF NODE NAME
        # python  814588   he    7u  IPv4 11276324      0t0  TCP localhost:commplex-main (LISTEN)

        # caller (producer)

        # lsof -i:5000
        # COMMAND    PID USER   FD   TYPE   DEVICE SIZE/OFF NODE NAME
        # python  814588   he    8u  IPv4 11269882      0t0  TCP localhost:53290->localhost:commplex-main (ESTABLISHED)
        # python  814588   he    9u  IPv4 11269883      0t0  TCP localhost:commplex-main->localhost:53290 (ESTABLISHED)

        # netstat -tapun | grep 5000
        # tcp        0      0 127.0.0.1:5000          0.0.0.0:*               LISTEN      814588/python
        # tcp        0      0 127.0.0.1:53290         127.0.0.1:5000          ESTABLISHED 814588/python
        # tcp        0      0 127.0.0.1:5000          127.0.0.1:53290         ESTABLISHED 814588/python
    print("end parent")

run(main_start_init)