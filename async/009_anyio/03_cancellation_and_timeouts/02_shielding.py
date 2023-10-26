"""
There are cases where you want to shield your task from cancellation, at least temporarily. The most important such use case is performing shutdown procedures on asynchronous resources.

To accomplish this, open a new cancel scope with the shield=True argument:


"""


from anyio import CancelScope, create_task_group, sleep, run


async def external_task():
    print('Started sleeping in the external task')
    await sleep(1)
    print('This line should never be seen')


async def main():
    async with create_task_group() as tg:
        with CancelScope(shield=True) as scope:
            tg.start_soon(external_task)
            # The shielded block will be exempt from cancellation except when the shielded block itself is being cancelled. Shielding a cancel scope is often best combined with move_on_after() or fail_after(), both of which also accept shield=True.
            tg.cancel_scope.cancel()  # no effect
            # scope.cancel() - effect
            print('Started sleeping in the host task')
            await sleep(1)
            print('Finished sleeping in the host task')

run(main)
