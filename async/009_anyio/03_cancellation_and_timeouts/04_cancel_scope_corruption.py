"""
Avoiding cancel scope stack corruption
When using cancel scopes, it is important that they are entered and exited in LIFO (last in, first out) order within
each task. This is usually not an issue since cancel scopes are normally used as context managers. However,
in certain situations, cancel scope stack corruption might still occur:

Manually calling CancelScope.__enter__() and CancelScope.__exit__(), usually from another context manager class,
in the wrong order

Using cancel scopes with [Async]ExitStack in a manner that couldn’t be achieved by nesting them as context managers

Using the low level coroutine protocol to execute parts of the coroutine function in different cancel scopes

Yielding in an async generator while enclosed in a cancel scope

Remember that task groups contain their own cancel scopes so the same list of risky situations applies to them too.

As an example, the following code is highly dubious:
"""
from anyio import create_task_group


async def foo():
    ...


# Bad!
async def some_generator():
    async with create_task_group() as tg:
        tg.start_soon(foo)
        yield


"""
The problem with this code is that it violates structural concurrency: what happens if the spawned task raises an 
exception? The host task would be cancelled as a result, but the host task might be long gone by the time that 
happens. Even if it weren’t, any enclosing try...except in the generator would not be triggered. Unfortunately there 
is currently no way to automatically detect this condition in AnyIO, so in practice you may simply experience some 
weird behavior in your application as a consequence of running code like above.

Depending on how they are used, this pattern is, however, usually safe to use in asynchronous context managers, 
so long as you make sure that the same host task keeps running throughout the entire enclosed code block:
"""

from contextlib import asynccontextmanager


# Okay in most cases!
@asynccontextmanager
async def some_context_manager():
    async with create_task_group() as tg:
        tg.start_soon(foo)
        yield


"""
Prior to AnyIO 3.6, this usage pattern was also invalid in pytest’s asynchronous generator fixtures. Starting from 
3.6, however, each async generator fixture is run from start to end in the same task, making it possible to have task 
groups or cancel scopes safely straddle the yield.

When you’re implementing the async context manager protocol manually and your async context manager needs to use 
other context managers, you may find it necessary to call their __aenter__() and __aexit__() directly. In such cases, 
it is absolutely vital to ensure that their __aexit__() methods are called in the exact reverse order of the 
__aenter__() calls. To this end, you may find the AsyncExitStack class very useful:
"""

from contextlib import AsyncExitStack

from anyio import create_task_group


class MyAsyncContextManager:
    async def __aenter__(self):
        self._exitstack = AsyncExitStack()
        await self._exitstack.__aenter__()
        self._task_group = await self._exitstack.enter_async_context(
            create_task_group()
        )

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self._exitstack.__aexit__(exc_type, exc_val, exc_tb)
