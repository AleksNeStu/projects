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

from common.utils import timer_dc, w_err


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

# run(main_start_init)





# 3) Handling multiple errors in a task group
"""
It is possible for more than one task to raise an exception in a task group. This can happen when a task reacts to cancellation by entering either an exception handler block or a finally: block and raises an exception there. This raises the question: which exception is propagated from the task group context manager? The answer is “both”. In practice this means that a special exception, ExceptionGroup (or BaseExceptionGroup) is raised which contains both exception objects.

To catch such exceptions potentially nested in groups, special measures are required. On Python 3.11 and later, you can use the except* syntax to catch multiple exceptions:
"""
from anyio import create_task_group

async def t1():
    await sleep(32)
    raise ValueError("ValueError t1")

async def t2():
    await sleep(22)
    raise KeyError("KeyError t2")

async def t3():
    try:
        await sleep(1)
        raise ValueError("ValueError t3")
    except ValueError:
        raise NotImplementedError("NotImplementedError t3 - 1")
    finally:
        raise NotImplementedError("NotImplementedError t3 - 2")



async def main_ex2():

    try:
        async with create_task_group() as tg:
            for t in [t1, t2, t3]:
                tg.start_soon(t)

    # On Python 3.11 and later, you can use the except* syntax to catch multiple exceptions:
    except* ValueError as excgroup:
        excgroup: ExceptionGroup
        for exc in excgroup.exceptions:
            print(exc)  # handle each ValueError

    except* NotImplementedError as excgroup:
        excgroup: ExceptionGroup
        for exc in excgroup.exceptions:
            print(exc)  # handle each ValueError

# run(main_ex2)

# OLD Python version example
from anyio import create_task_group
from exceptiongroup import catch

def handle_valueerror(excgroup: ExceptionGroup) -> None:
    for exc in excgroup.exceptions:
        print(exc)  # handle each ValueError


def handle_keyerror(excgroup: ExceptionGroup) -> None:
    for exc in excgroup.exceptions:
        print(exc)  # handle each ValueError


async def main_ex_old():
    with catch({
        ValueError: handle_valueerror,
        KeyError: handle_keyerror
    }):
        async with create_task_group() as tg:
            tg.start_soon(t1)
            tg.start_soon(t2)


# f you need to set local variables in the handlers, declare them as nonlocal:

def handle_valueerror(exc):
    nonlocal somevariable
    somevariable = 'whatever'

# run(main_ex_old)


# Context propagation
"""
Whenever a new task is spawned, context will be copied to the new task. It is important to note which context will be copied to the newly spawned task. It is not the context of the task group’s host task that will be copied, but the context of the task that calls TaskGroup.start() or TaskGroup.start_soon().
"""

# Differences with asyncio.TaskGroup
"""
The asyncio.TaskGroup class, added in Python 3.11, is very similar in design to the AnyIO TaskGroup class. The asyncio counterpart has some important differences in its semantics, however:

The task group itself is instantiated directly, rather than using a factory function

Tasks are spawned solely through create_task(); there is no start() or start_soon() method

The create_task() method returns a task object which can be awaited on (or cancelled)

Tasks spawned via create_task() can only be cancelled individually (there is no cancel() method or similar in the task group)

When a task spawned via create_task() is cancelled before its coroutine has started running, it will not get a chance to handle the cancellation exception

asyncio.TaskGroup does not allow starting new tasks after an exception in one of the tasks has triggered a shutdown of the task group
"""
