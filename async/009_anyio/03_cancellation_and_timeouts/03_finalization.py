# Sometimes you may want to perform cleanup operations in response to the failure of the operation:
from anyio import sleep, CancelScope


async def external_task():
    print('Started sleeping in the external task')
    await sleep(1)
    print('This line should never be seen')


async def do_something():
    try:
        await external_task()
    except BaseException:
        # (perform cleanup)
        raise


"""
In some specific cases, you might only want to catch the cancellation exception. This is tricky because each async 
framework has its own exception class for that and AnyIO cannot control which exception is raised in the task when 
it’s cancelled. To work around that, AnyIO provides a way to retrieve the exception class specific to the currently 
running async framework, using:func:~get_cancelled_exc_class
"""

from anyio import get_cancelled_exc_class


async def do_something2():
    try:
        await external_task()
    except get_cancelled_exc_class():
        # (perform cleanup)
        # Always reraise the cancellation exception if you catch it. Failing to do so may cause undefined behavior in
        # your application.
        raise


"""
If you need to use await during finalization, you need to enclose it in a shielded cancel scope, or the operation 
will be cancelled immediately since it’s in an already cancelled scope:
"""


async def some_cleanup_function():
    ...


async def do_something3():
    try:
        await external_task()
    except get_cancelled_exc_class():
        with CancelScope(shield=True):
            await some_cleanup_function()

        raise
