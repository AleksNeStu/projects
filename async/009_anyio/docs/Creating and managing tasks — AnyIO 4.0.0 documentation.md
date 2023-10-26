---
source: https://anyio.readthedocs.io/en/stable/tasks.html

created: 2023-10-26T14:54:07 (UTC +02:00)

tags: []

author: 

---
# Creating and managing tasks — AnyIO 4.0.0 documentation
---
A _task_ is a unit of execution that lets you do many things concurrently that need waiting on. This works so that while you can have any number of tasks, the asynchronous event loop can only run one of them at a time. When the task encounters an `await` statement that requires the task to sleep until something happens, the event loop is then free to work on another task. When the thing the first task was waiting is complete, the event loop will resume the execution of that task on the first opportunity it gets.

Task handling in AnyIO loosely follows the [Trio](https://trio.readthedocs.io/en/latest/reference-core.html#tasks-let-you-do-multiple-things-at-once) model. Tasks can be created (_spawned_) using _task groups_. A task group is an asynchronous context manager that makes sure that all its child tasks are finished one way or another after the context block is exited. If a child task, or the code in the enclosed context block raises an exception, all child tasks are cancelled. Otherwise the context manager just waits until all child tasks have exited before proceeding.

Here’s a demonstration:

```
from anyio import sleep, create_task_group, run


async def sometask(num: int) -> None:
    print('Task', num, 'running')
    await sleep(1)
    print('Task', num, 'finished')


async def main() -> None:
    async with create_task_group() as tg:
        for num in range(5):
            tg.start_soon(sometask, num)

    print('All tasks finished!')

run(main)

```

## Starting and initializing tasks[¶](https://anyio.readthedocs.io/en/stable/tasks.html#starting-and-initializing-tasks "Link to this heading")

Sometimes it is very useful to be able to wait until a task has successfully initialized itself. For example, when starting network services, you can have your task start the listener and then signal the caller that initialization is done. That way, the caller can now start another task that depends on that service being up and running. Also, if the socket bind fails or something else goes wrong during initialization, the exception will be propagated to the caller which can then catch and handle it.

This can be done with [`TaskGroup.start()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup.start "anyio.abc.TaskGroup.start"):

```
from anyio import (
    TASK_STATUS_IGNORED,
    create_task_group,
    connect_tcp,
    create_tcp_listener,
    run,
)
from anyio.abc import TaskStatus


async def handler(stream):
    ...


async def start_some_service(
    port: int, *, task_status: TaskStatus[None] = TASK_STATUS_IGNORED
):
    async with await create_tcp_listener(
        local_host="127.0.0.1", local_port=port
    ) as listener:
        task_status.started()
        await listener.serve(handler)


async def main():
    async with create_task_group() as tg:
        await tg.start(start_some_service, 5000)
        async with await connect_tcp("127.0.0.1", 5000) as stream:
            ...


run(main)

```

The target coroutine function **must** call `task_status.started()` because the task that is calling with [`TaskGroup.start()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup.start "anyio.abc.TaskGroup.start") will be blocked until then. If the spawned task never calls it, then the [`TaskGroup.start()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup.start "anyio.abc.TaskGroup.start") call will raise a `RuntimeError`.

## Handling multiple errors in a task group[¶](https://anyio.readthedocs.io/en/stable/tasks.html#handling-multiple-errors-in-a-task-group "Link to this heading")

It is possible for more than one task to raise an exception in a task group. This can happen when a task reacts to cancellation by entering either an exception handler block or a `finally:` block and raises an exception there. This raises the question: which exception is propagated from the task group context manager? The answer is “both”. In practice this means that a special exception, [`ExceptionGroup`](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "(in Python v3.11)") (or [`BaseExceptionGroup`](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup "(in Python v3.11)")) is raised which contains both exception objects.

To catch such exceptions potentially nested in groups, special measures are required. On Python 3.11 and later, you can use the `except*` syntax to catch multiple exceptions:

```
from anyio import create_task_group

try:
    async with create_task_group() as tg:
        tg.start_soon(some_task)
        tg.start_soon(another_task)
except* ValueError as excgroup:
    for exc in excgroup:
        ...  # handle each ValueError
except* KeyError as excgroup:
    for exc in excgroup:
        ...  # handle each KeyError

```

If compatibility with older Python versions is required, you can use the `catch()` function from the [exceptiongroup](https://pypi.org/project/exceptiongroup/) package:

```
from anyio import create_task_group
from exceptiongroup import catch

def handle_valueerror(excgroup: ExceptionGroup) -> None:
    for exc in excgroup.exceptions:
        ...  # handle each ValueError

def handle_keyerror(excgroup: ExceptionGroup) -> None:
    for exc in excgroup.exceptions:
        ...  # handle each KeyError

with catch({
    ValueError: handle_valueerror,
    KeyError: handle_keyerror
}):
    async with create_task_group() as tg:
        tg.start_soon(some_task)
        tg.start_soon(another_task)

```

If you need to set local variables in the handlers, declare them as `nonlocal`:

```
def handle_valueerror(exc):
    nonlocal somevariable
    somevariable = 'whatever'

```

## Context propagation[¶](https://anyio.readthedocs.io/en/stable/tasks.html#context-propagation "Link to this heading")

Whenever a new task is spawned, [context](https://docs.python.org/3/library/contextvars.html) will be copied to the new task. It is important to note _which_ context will be copied to the newly spawned task. It is not the context of the task group’s host task that will be copied, but the context of the task that calls [`TaskGroup.start()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup.start "anyio.abc.TaskGroup.start") or [`TaskGroup.start_soon()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup.start_soon "anyio.abc.TaskGroup.start_soon").

## Differences with asyncio.TaskGroup[¶](https://anyio.readthedocs.io/en/stable/tasks.html#differences-with-asyncio-taskgroup "Link to this heading")

The [`asyncio.TaskGroup`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup "(in Python v3.11)") class, added in Python 3.11, is very similar in design to the AnyIO [`TaskGroup`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup "anyio.abc.TaskGroup") class. The asyncio counterpart has some important differences in its semantics, however:

-   The task group itself is instantiated directly, rather than using a factory function
    
-   Tasks are spawned solely through [`create_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup.create_task "(in Python v3.11)"); there is no `start()` or `start_soon()` method
    
-   The [`create_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup.create_task "(in Python v3.11)") method returns a task object which can be awaited on (or cancelled)
    
-   Tasks spawned via [`create_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup.create_task "(in Python v3.11)") can only be cancelled individually (there is no `cancel()` method or similar in the task group)
    
-   When a task spawned via [`create_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup.create_task "(in Python v3.11)") is cancelled before its coroutine has started running, it will not get a chance to handle the cancellation exception
    
-   [`asyncio.TaskGroup`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup "(in Python v3.11)") does not allow starting new tasks after an exception in one of the tasks has triggered a shutdown of the task group
