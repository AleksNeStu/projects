"""Context propagation
When running functions in worker threads, the current context is copied to the worker thread. Therefore any context
variables available on the task will also be available to the code running on the thread. As always with context
variables, any changes made to them will not propagate back to the calling asynchronous task.

When calling asynchronous code from worker threads, context is again copied to the task that calls the target
function in the event loop thread.

Adjusting the default maximum worker thread count
The default AnyIO worker thread limiter has a value of 40, meaning that any calls to to_thread.run_sync() without an
explicit limiter argument will cause a maximum of 40 threads to be spawned. You can adjust this limit like this:
"""
from anyio import to_thread


async def foo():
    # Set the maximum number of worker threads to 60
    to_thread.current_default_thread_limiter().total_tokens = 60
# Note AnyIO’s default thread pool limiter does not affect the default thread pool executor on asyncio.
