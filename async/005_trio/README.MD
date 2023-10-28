Trio’s nurseries: to delimit the lifetime of concurrent tasks, ensure that they never leak, and never swallow errors
silently.

In Trio, it is not possible to spawn tasks without first giving them a place to live: a nursery. Nurseries are
context managers that expose an interface similar to asyncio.create_task.

Tasks are always owned and managed by the nursery which spawned them, and the nursery context will never exit until
all its tasks have completed by producing a return value or raising an exception.

When a task fails, the nursery ensures that all concurrently running tasks are properly canceled, giving every task the
ability to gracefully clean up.

After all tasks are done, the exception is propagated back through the call stack.