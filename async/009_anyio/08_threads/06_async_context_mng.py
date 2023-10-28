"""
Using asynchronous context managers from worker threads
You can use wrap_async_context_manager() to wrap an asynchronous context managers as a synchronous one:
"""
from anyio.from_thread import start_blocking_portal


class AsyncContextManager:
    async def __aenter__(self):
        print('entering')

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('exiting with', exc_type)


async_cm = AsyncContextManager()
with start_blocking_portal() as portal, portal.wrap_async_context_manager(async_cm):
    print('inside the context manager block')

# Note You cannot use wrapped async context managers in synchronous callbacks inside the event loop thread.
