"""
The ability to cancel tasks is the foremost advantage of the asynchronous programming model. Threads, on the other
hand, cannot be forcibly killed and shutting them down will require perfect cooperation from the code running in them.

Cancellation in AnyIO follows the model established by the Trio framework. This means that cancellation of tasks is
done via so called cancel scopes. Cancel scopes are used as context managers and can be nested. Cancelling a cancel
scope cancels all cancel scopes nested within it. If a task is waiting on something, it is cancelled immediately. If
the task is just starting, it will run until it first tries to run an operation requiring waiting, such as sleep().

A task group contains its own cancel scope. The entire task group can be cancelled by cancelling this scope.
"""
from common.utils import w_err

"""
Networked operations can often take a long time, and you usually want to set up some kind of a timeout to ensure that 
your application doesn’t stall forever. There are two principal ways to do this: move_on_after() and fail_after(). 
Both are used as synchronous context managers. The difference between these two is that the former simply exits the 
context block prematurely on a timeout, while the other raises a TimeoutError.

Both methods create a new cancel scope, and you can check the deadline by accessing the deadline attribute. Note, 
however, that an outer cancel scope may have an earlier deadline than your current cancel scope. To check the actual 
deadline, you can use the current_effective_deadline() function.
"""

from anyio import create_task_group, move_on_after, sleep, run, fail_after


# 1) move_on_after()
async def main1():
    async with create_task_group() as tg:
        with move_on_after(1) as scope:
            print('Starting sleep')
            await sleep(2)
            print('This should never be printed')

        # The cancelled_caught property will be True if timeout was reached
        print('Exited cancel scope, cancelled =', scope.cancel_called)


run(main1)

# fail_after()
"""
Note It’s recommended not to directly cancel a scope from fail_after(), as that may currently result in TimeoutError 
being erroneously raised if exiting the scope is delayed long enough for the deadline to be exceeded.
"""


async def main2():
    with w_err({TimeoutError: None}):
        async with create_task_group() as tg:
            with fail_after(1) as scope:
                print('Starting sleep')
                await sleep(2)
                print('This should never be printed')

            # The cancelled_caught property will be True if timeout was reached
            print('Exited cancel scope, cancelled =', scope.cancel_called)


run(main2)
