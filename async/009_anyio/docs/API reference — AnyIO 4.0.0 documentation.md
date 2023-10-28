---
source: https://anyio.readthedocs.io/en/stable/api.html

created: 2023-10-28T19:52:22 (UTC +02:00)

tags: []

author: 

---

# API reference — AnyIO 4.0.0 documentation
---

## Event loop[¶](https://anyio.readthedocs.io/en/stable/api.html#event-loop "Link to this heading")

anyio.run(_func_, _\*args_, _backend\='asyncio'_,
_backend\_options\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.run "Link to this definition")

Run the given coroutine function in an asynchronous event loop.

The current thread must not be already running an event loop.

Parameters:

- **func
  ** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis "(in Python v3.11)"), [`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "(in Python v3.11)")\[[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)\]\]) –
  a coroutine function

- **args** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – positional
  arguments to `func`

- **backend** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – name of the
  asynchronous event loop implementation – currently either `asyncio` or `trio`

- **backend\_options
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\]\]) –
  keyword arguments to call the backend `run()` implementation with (
  documented [here](https://anyio.readthedocs.io/en/stable/basics.html#backend-options))

Return type:

[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)

Returns:

the return value of the coroutine function

Raises:

- [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.11)") – if an
  asynchronous event loop is already running in this thread

- [**LookupError**](https://docs.python.org/3/library/exceptions.html#LookupError "(in Python v3.11)") – if the named
  backend is not found

anyio.get\_all\_backends()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.get_all_backends "Link to this definition")

Return a tuple of the names of all built-in backends.

Return type:

[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`...`](https://docs.python.org/3/library/constants.html#Ellipsis "(in Python v3.11)")\]

anyio.get\_cancelled\_exc\_class()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.get_cancelled_exc_class "Link to this definition")

Return the current async library’s cancellation exception class.

Return type:

[`type`](https://docs.python.org/3/library/functions.html#type "(in Python v3.11)")\[[`BaseException`](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.11)")\]

_async_ anyio.sleep(_delay_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.sleep "Link to this definition")

Pause the current task for the specified duration.

Parameters:

**delay** ([`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – the duration, in
seconds

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_async_
anyio.sleep\_forever()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.sleep_forever "Link to this definition")

Pause the current task until it’s cancelled.

This is a shortcut for `sleep(math.inf)`. :
rtype: [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

New in version 3.1.

_async_ anyio.sleep\_until(
_deadline_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.sleep_until "Link to this definition")

Pause the current task until the given time.

Parameters:

**deadline** ([`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – the absolute time
to wake up at (according to the internal monotonic clock of the event loop)

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

New in version 3.1.

anyio.current\_time()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.current_time "Link to this definition")

Return the current value of the event loop’s internal clock.

Return type:

[`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")

Returns:

the clock value (seconds)

## Asynchronous resources[¶](https://anyio.readthedocs.io/en/stable/api.html#asynchronous-resources "Link to this heading")

_async_ anyio.aclose\_forcefully(
_resource_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.aclose_forcefully "Link to this definition")

Close an asynchronous resource in a cancelled scope.

Doing this closes the resource without waiting on anything.

Parameters:

**resource
** ([`AsyncResource`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AsyncResource "anyio.abc.AsyncResource")) –
the resource to close

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_
anyio.abc.AsyncResource[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AsyncResource "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

Abstract base class for all closeable asynchronous resources.

Works as an asynchronous context manager which returns the instance itself on enter, and
calls [`aclose()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AsyncResource.aclose "anyio.abc.AsyncResource.aclose")
on exit.

_abstract async_
aclose()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AsyncResource.aclose "Link to this definition")

Close the resource.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

## Typed attributes[¶](https://anyio.readthedocs.io/en/stable/api.html#typed-attributes "Link to this heading")

anyio.typed\_attribute()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.typed_attribute "Link to this definition")

Return a unique object, used to mark typed attributes.

Return type:

[`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")

_class_
anyio.TypedAttributeSet[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeSet "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

Superclass for typed attribute collections.

Checks that every public attribute of every subclass has a type annotation.

_class_
anyio.TypedAttributeProvider[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeProvider "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

Base class for classes that wish to provide typed extra attributes.

Return the value of the given typed extra attribute.

Parameters:

- **attribute** ([`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")) – the
  attribute (member of
  a [`TypedAttributeSet`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeSet "anyio.TypedAttributeSet"))
  to look for

- **default** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – the value that
  should be returned if no value is found for the attribute

Raises:

[**TypedAttributeLookupError
**](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeLookupError "anyio.TypedAttributeLookupError") –
if the search failed and no default value was given

Return type:

[`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned
mapping (but the wrapper may override the callables from the wrapped instance).

## Timeouts and cancellation[¶](https://anyio.readthedocs.io/en/stable/api.html#timeouts-and-cancellation "Link to this heading")

anyio.move\_on\_after(_delay_,
_shield\=False_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.move_on_after "Link to this definition")

Create a cancel scope with a deadline that expires after the given delay.

Parameters:

- **delay
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")\]) –
  maximum allowed time (in seconds) before exiting the context block, or `None` to disable the timeout

- **shield** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – `True` to shield
  the cancel scope from external cancellation

Return type:

[`CancelScope`](https://anyio.readthedocs.io/en/stable/api.html#anyio.CancelScope "anyio.CancelScope")

Returns:

a cancel scope

anyio.fail\_after(_delay_,
_shield\=False_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.fail_after "Link to this definition")

Create a context manager which raises
a [`TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError "(in Python v3.11)") if does not
finish in time.

Parameters:

- **delay
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")\]) –
  maximum allowed time (in seconds) before raising the exception, or `None` to disable the timeout

- **shield** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – `True` to shield
  the cancel scope from external cancellation

Returns:

a context manager that yields a cancel scope

Return type:

[`ContextManager`](https://docs.python.org/3/library/typing.html#typing.ContextManager "(in Python v3.11)")\[[`CancelScope`](https://anyio.readthedocs.io/en/stable/api.html#anyio.CancelScope "anyio.CancelScope")\]

anyio.current\_effective\_deadline()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.current_effective_deadline "Link to this definition")

Return the nearest deadline among all the cancel scopes effective for the current task.

Returns:

a clock value from the event loop’s internal clock (or `float('inf')` if there is no deadline in effect,
or `float('-inf')` if the current scope has been cancelled)

Return type:

[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")

_class_ anyio.CancelScope(_\*_,
_deadline: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)") \= inf_,
_shield: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)") \=
False_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CancelScope "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

Wraps a unit of work that can be made separately cancellable.

Parameters:

- **deadline** – The time (clock value) when this scope is cancelled automatically

- **shield** – `True` to shield the cancel scope from external cancellation

cancel()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CancelScope.cancel "Link to this definition")

Cancel this scope immediately.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_property_
cancel\_called_: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CancelScope.cancel_called "Link to this definition")

`True`
if [`cancel()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.CancelScope.cancel "anyio.CancelScope.cancel") has
been called.

_property_
cancelled\_caught_: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CancelScope.cancelled_caught "Link to this definition")

`True` if this scope suppressed a cancellation exception it itself raised.

This is typically used to check if any work was interrupted, or to see if the scope was cancelled due to its deadline
being reached. The value will, however, only be `True` if the cancellation was triggered by the scope itself (and not an
outer scope).

_property_
deadline_: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CancelScope.deadline "Link to this definition")

The time (clock value) when this scope is cancelled automatically.

Will be `float('inf')` if no timeout has been set.

_property_
shield_: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CancelScope.shield "Link to this definition")

`True` if this scope is shielded from external cancellation.

While a scope is shielded, it will not receive cancellations from outside.

## Task groups[¶](https://anyio.readthedocs.io/en/stable/api.html#task-groups "Link to this heading")

anyio.create\_task\_group()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.create_task_group "Link to this definition")

Create a task group.

Return type:

[`TaskGroup`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup "anyio.abc.TaskGroup")

Returns:

a task group

_class_
anyio.abc.TaskGroup[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

Groups several asynchronous tasks together.

Variables:

**cancel\_scope** ([
_CancelScope_](https://anyio.readthedocs.io/en/stable/api.html#anyio.CancelScope "anyio.CancelScope")) – the cancel
scope inherited by all child tasks

_abstract async_ start(_func_, _\*args_,
_name\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup.start "Link to this definition")

Start a new task and wait until it signals for readiness.

Parameters:

- **func
  ** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis "(in Python v3.11)"), [`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "(in Python v3.11)")\[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\]\]) –
  a coroutine function

- **args** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – positional
  arguments to call the function with

- **name** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – name of the task,
  for the purposes of introspection and debugging

Return type:

[`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")

Returns:

the value passed to `task_status.started()`

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.11)") – if the task
finishes without calling `task_status.started()`

New in version 3.0.

_abstract_ start\_soon(_func_, _\*args_,
_name\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup.start_soon "Link to this definition")

Start a new task in this task group.

Parameters:

- **func
  ** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis "(in Python v3.11)"), [`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "(in Python v3.11)")\[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\]\]) –
  a coroutine function

- **args** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – positional
  arguments to call the function with

- **name** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – name of the task,
  for the purposes of introspection and debugging

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

New in version 3.0.

_class_ anyio.abc.TaskStatus(_\*args_,
_\*\*kwargs_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskStatus "Link to this definition")

Bases: [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol "(in Python v3.11)")\[`T_contra`\]

started(
_value\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskStatus.started "Link to this definition")

Signal that the task has started.

Parameters:

**value
** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_contra`,
contravariant=True)\]) – object passed back to the starter of the task

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

## Running code in worker threads[¶](https://anyio.readthedocs.io/en/stable/api.html#running-code-in-worker-threads "Link to this heading")

_async_ anyio.to\_thread.run\_sync(_func_, _\*args_, _cancellable\=False_,
_limiter\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.to_thread.run_sync "Link to this definition")

Call the given function with the given arguments in a worker thread.

If the `cancellable` option is enabled and the task waiting for its completion is cancelled, the thread will still run
its course but its return value (or any raised exception) will be ignored.

Parameters:

- **func
  ** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis "(in Python v3.11)"), [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)\]) –
  a callable

- **args** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – positional
  arguments for the callable

- **cancellable** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – `True` to
  allow cancellation of the operation

- **limiter
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`CapacityLimiter`](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter "anyio.CapacityLimiter")\]) –
  capacity limiter to use to limit the total amount of threads running (if omitted, the default limiter is used)

Return type:

[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)

Returns:

an awaitable that yields the return value of the function.

anyio.to\_thread.current\_default\_thread\_limiter()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.to_thread.current_default_thread_limiter "Link to this definition")

Return the capacity limiter that is used by default to limit the number of concurrent threads.

Return type:

[`CapacityLimiter`](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter "anyio.CapacityLimiter")

Returns:

a capacity limiter object

## Running code in worker processes[¶](https://anyio.readthedocs.io/en/stable/api.html#running-code-in-worker-processes "Link to this heading")

_async_ anyio.to\_process.run\_sync(_func_, _\*args_, _cancellable\=False_,
_limiter\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.to_process.run_sync "Link to this definition")

Call the given function with the given arguments in a worker process.

If the `cancellable` option is enabled and the task waiting for its completion is cancelled, the worker process running
it will be abruptly terminated using SIGKILL (or `terminateProcess()` on Windows).

Parameters:

- **func
  ** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis "(in Python v3.11)"), [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)\]) –
  a callable

- **args** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – positional
  arguments for the callable

- **cancellable** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – `True` to
  allow cancellation of the operation while it’s running

- **limiter
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`CapacityLimiter`](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter "anyio.CapacityLimiter")\]) –
  capacity limiter to use to limit the total amount of processes running (if omitted, the default limiter is used)

Return type:

[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)

Returns:

an awaitable that yields the return value of the function.

anyio.to\_process.current\_default\_process\_limiter()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.to_process.current_default_process_limiter "Link to this definition")

Return the capacity limiter that is used by default to limit the number of worker processes.

Return type:

[`CapacityLimiter`](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter "anyio.CapacityLimiter")

Returns:

a capacity limiter object

## Running asynchronous code from other threads[¶](https://anyio.readthedocs.io/en/stable/api.html#running-asynchronous-code-from-other-threads "Link to this heading")

anyio.from\_thread.run(_func_,
_\*args_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.run "Link to this definition")

Call a coroutine function from a worker thread.

Parameters:

- **func
  ** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis "(in Python v3.11)"), [`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "(in Python v3.11)")\[[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)\]\]) –
  a coroutine function

- **args** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – positional
  arguments for the callable

Return type:

[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)

Returns:

the return value of the coroutine function

anyio.from\_thread.run\_sync(_func_,
_\*args_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.run_sync "Link to this definition")

Call a function in the event loop thread from a worker thread.

Parameters:

- **func
  ** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis "(in Python v3.11)"), [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)\]) –
  a callable

- **args** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – positional
  arguments for the callable

Return type:

[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)

Returns:

the return value of the callable

anyio.from\_thread.start\_blocking\_portal(_backend\='asyncio'_,
_backend\_options\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.start_blocking_portal "Link to this definition")

Start a new event loop in a new thread and run a blocking portal in its main task.

The parameters are the same as for [`run()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.run "anyio.run").

Parameters:

- **backend** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – name of the backend

- **backend\_options
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\]\]) –
  backend options

Return type:

[`Generator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "(in Python v3.11)")\[[`BlockingPortal`](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.BlockingPortal "anyio.from_thread.BlockingPortal"), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)"), [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]

Returns:

a context manager that yields a blocking portal

Changed in version 3.0: Usage as a context manager is now required.

_class_
anyio.from\_thread.BlockingPortal[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.BlockingPortal "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

An object that lets external threads run code in an asynchronous event loop.

call(_func_,
_\*args_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.BlockingPortal.call "Link to this definition")

Call the given function in the event loop thread.

If the callable returns a coroutine object, it is awaited on.

Parameters:

**func
** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis "(in Python v3.11)"), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "(in Python v3.11)")\[[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)\], [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)\]\]) –
any callable

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.11)") – if the portal
is not running or if this method is called from within the event loop thread

Return type:

[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)

_async_
sleep\_until\_stopped()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.BlockingPortal.sleep_until_stopped "Link to this definition")

Sleep
until [`stop()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.BlockingPortal.stop "anyio.from_thread.BlockingPortal.stop")
is called.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

start\_task(_func_, _\*args_,
_name\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.BlockingPortal.start_task "Link to this definition")

Start a task in the portal’s task group and wait until it signals for readiness.

This method works the same way
as [`abc.TaskGroup.start()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup.start "anyio.abc.TaskGroup.start").

Parameters:

- **func
  ** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis "(in Python v3.11)"), [`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "(in Python v3.11)")\[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\]\]) –
  the target function

- **args** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – positional
  arguments passed to `func`

- **name** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – name of the
  task (will be coerced to a string if not `None`)

Returns:

a tuple of (future, task\_status\_value) where the `task_status_value` is the value passed to `task_status.started()`
from within the target function

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.11)")\[[concurrent.futures.Future](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "(in Python v3.11)")
\[Any\], Any\]

New in version 3.0.

start\_task\_soon(_func_, _\*args_,
_name\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.BlockingPortal.start_task_soon "Link to this definition")

Start a task in the portal’s task group.

The task will be run inside a cancel scope which can be cancelled by cancelling the returned future.

Parameters:

- **func
  ** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis "(in Python v3.11)"), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "(in Python v3.11)")\[[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)\], [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Retval`)\]\]) –
  the target function

- **args** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – positional
  arguments passed to `func`

- **name** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – name of the
  task (will be coerced to a string if not `None`)

Returns:

a future that resolves with the return value of the callable if the task completes successfully, or with the exception
raised in the task

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.11)") – if the portal
is not running or if this method is called from within the event loop thread

Return type:

[concurrent.futures.Future](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "(in Python v3.11)")
\[T\_Retval\]

New in version 3.0.

_async_ stop(
_cancel\_remaining\=False_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.BlockingPortal.stop "Link to this definition")

Signal the portal to shut down.

This marks the portal as no longer accepting new calls and exits
from [`sleep_until_stopped()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.BlockingPortal.sleep_until_stopped "anyio.from_thread.BlockingPortal.sleep_until_stopped").

Parameters:

**cancel\_remaining** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – `True` to
cancel all the remaining tasks, `False` to let them finish before returning

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

wrap\_async\_context\_manager(
_cm_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.BlockingPortal.wrap_async_context_manager "Link to this definition")

Wrap an async context manager as a synchronous context manager via this portal.

Spawns a task that will call both `__aenter__()` and `__aexit__()`, stopping in the middle until the synchronous context
manager exits.

Parameters:

**cm
** ([`AsyncContextManager`](https://docs.python.org/3/library/typing.html#typing.AsyncContextManager "(in Python v3.11)")\[[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_co`)\]) –
an asynchronous context manager

Return type:

[`ContextManager`](https://docs.python.org/3/library/typing.html#typing.ContextManager "(in Python v3.11)")\[[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_co`)\]

Returns:

a synchronous context manager

New in version 2.1.

## Async file I/O[¶](https://anyio.readthedocs.io/en/stable/api.html#async-file-i-o "Link to this heading")

_async_ anyio.open\_file(_file_, _mode\='r'_, _buffering\=\-1_, _encoding\=None_, _errors\=None_, _newline\=None_,
_closefd\=True_,
_opener\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.open_file "Link to this definition")

Open a file asynchronously.

The arguments are exactly the same as for the
builtin [`open()`](https://docs.python.org/3/library/functions.html#open "(in Python v3.11)").

Return type:

[`AsyncFile`](https://anyio.readthedocs.io/en/stable/api.html#anyio.AsyncFile "anyio.AsyncFile")\[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\]

Returns:

an asynchronous file object

anyio.wrap\_file(_file_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.wrap_file "Link to this definition")

Wrap an existing file as an asynchronous file.

Parameters:

**file
** ([`IO`](https://docs.python.org/3/library/typing.html#typing.IO "(in Python v3.11)")\[[`AnyStr`](https://docs.python.org/3/library/typing.html#typing.AnyStr "(in Python v3.11)")\]) –
an existing file-like object

Return type:

[`AsyncFile`](https://anyio.readthedocs.io/en/stable/api.html#anyio.AsyncFile "anyio.AsyncFile")\[[`AnyStr`](https://docs.python.org/3/library/typing.html#typing.AnyStr "(in Python v3.11)")\]

Returns:

an asynchronous file object

_class_ anyio.AsyncFile(
_fp_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.AsyncFile "Link to this definition")

Bases: [`AsyncResource`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AsyncResource "anyio.abc.AsyncResource"), [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.11)")

An asynchronous file object.

This class wraps a standard file object and provides async friendly versions of the following blocking methods (where
available on the original file object):

- read

- read1

- readline

- readlines

- readinto

- readinto1

- write

- writelines

- truncate

- seek

- tell

- flush

All other methods are directly passed through.

This class supports the asynchronous context manager protocol which closes the underlying file at the end of the context
block.

This class also supports asynchronous iteration:

```
async with await open_file(...) as f:
    async for line in f:
        print(line)

```

_async_ aclose()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.AsyncFile.aclose "Link to this definition")

Close the resource.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_property_
wrapped_: [IO](https://docs.python.org/3/library/typing.html#typing.IO "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.AsyncFile.wrapped "Link to this definition")

The wrapped file object.

_class_ anyio.Path(_\*args_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Path "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

An asynchronous version
of [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.11)").

This class cannot be substituted
for [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.11)")
or [`pathlib.PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "(in Python v3.11)"), but it is
compatible with the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.11)")
interface.

It implements the Python 3.10 version
of [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.11)") interface, except
for the
deprecated [`link_to()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.link_to "(in Python v3.11)")
method.

Any methods that do disk I/O need to be awaited on. These methods are:

- [`absolute()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.absolute "(in Python v3.11)")

- [`chmod()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.chmod "(in Python v3.11)")

- [`cwd()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.cwd "(in Python v3.11)")

- [`exists()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.exists "(in Python v3.11)")

- [`expanduser()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.expanduser "(in Python v3.11)")

- [`group()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.group "(in Python v3.11)")

- [`hardlink_to()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.hardlink_to "(in Python v3.11)")

- [`home()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.home "(in Python v3.11)")

- [`is_block_device()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_block_device "(in Python v3.11)")

- [`is_char_device()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_char_device "(in Python v3.11)")

- [`is_dir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_dir "(in Python v3.11)")

- [`is_fifo()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_fifo "(in Python v3.11)")

- [`is_file()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_file "(in Python v3.11)")

- [`is_mount()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_mount "(in Python v3.11)")

- [`lchmod()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.lchmod "(in Python v3.11)")

- [`lstat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.lstat "(in Python v3.11)")

- [`mkdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir "(in Python v3.11)")

- [`open()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.open "(in Python v3.11)")

- [`owner()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.owner "(in Python v3.11)")

- [`read_bytes()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_bytes "(in Python v3.11)")

- [`read_text()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_text "(in Python v3.11)")

- [`readlink()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.readlink "(in Python v3.11)")

- [`rename()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rename "(in Python v3.11)")

- [`replace()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.replace "(in Python v3.11)")

- [`rmdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rmdir "(in Python v3.11)")

- [`samefile()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.samefile "(in Python v3.11)")

- [`stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "(in Python v3.11)")

- [`touch()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.touch "(in Python v3.11)")

- [`unlink()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.unlink "(in Python v3.11)")

- [`write_bytes()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_bytes "(in Python v3.11)")

- [`write_text()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_text "(in Python v3.11)")

Additionally, the following methods return an async iterator
yielding [`Path`](https://anyio.readthedocs.io/en/stable/api.html#anyio.Path "anyio.Path") objects:

- [`glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "(in Python v3.11)")

- [`iterdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir "(in Python v3.11)")

- [`rglob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob "(in Python v3.11)")

## Streams and stream wrappers[¶](https://anyio.readthedocs.io/en/stable/api.html#streams-and-stream-wrappers "Link to this heading")

anyio.create\_memory\_object\_stream(
_max\_buffer\_size: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)") \= 0_,
_item\_type: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)") \=
None_) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.11)")\[[MemoryObjectSendStream](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectSendStream "anyio.streams.memory.MemoryObjectSendStream")
\[T\_Item\], [MemoryObjectReceiveStream](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectReceiveStream "anyio.streams.memory.MemoryObjectReceiveStream")
\[T\_Item\]\][¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.create_memory_object_stream "Link to this definition")

Create a memory object stream.

The stream’s item type can be annotated like `create_memory_object_stream[T_Item]()`.

Parameters:

- **max\_buffer\_size** – number of items held in the buffer until `send()` starts blocking

- **item\_type** –

  old way of marking the streams with the right generic type for static typing (does nothing on AnyIO 4)

  Deprecated since version 4.0: Use `create_memory_object_stream[YourItemType](...)` instead.

Returns:

a tuple of (send stream, receive stream)

_class_
anyio.abc.UnreliableObjectReceiveStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectReceiveStream "Link to this definition")

Bases: [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.11)")\[`T_co`\], [`AsyncResource`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AsyncResource "anyio.abc.AsyncResource"), [`TypedAttributeProvider`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeProvider "anyio.TypedAttributeProvider")

An interface for receiving objects.

This interface makes no guarantees that the received messages arrive in the order in which they were sent, or that no
messages are missed.

Asynchronously iterating over objects of this type will yield objects matching the given type parameter.

_abstract async_
receive()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectReceiveStream.receive "Link to this definition")

Receive the next item.

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if the
  receive stream has been explicitly closed

- [**EndOfStream**](https://anyio.readthedocs.io/en/stable/api.html#anyio.EndOfStream "anyio.EndOfStream") – if this
  stream has been closed from the other end

- [**BrokenResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.BrokenResourceError "anyio.BrokenResourceError") – if this
  stream has been rendered unusable due to external causes

Return type:

[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_co`, covariant=True)

_class_
anyio.abc.UnreliableObjectSendStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectSendStream "Link to this definition")

Bases: [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.11)")\[`T_contra`\], [`AsyncResource`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AsyncResource "anyio.abc.AsyncResource"), [`TypedAttributeProvider`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeProvider "anyio.TypedAttributeProvider")

An interface for sending objects.

This interface makes no guarantees that the messages sent will reach the recipient(s) in the same order in which they
were sent, or at all.

_abstract async_ send(
_item_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectSendStream.send "Link to this definition")

Send an item to the peer(s).

Parameters:

**item** ([`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_contra`,
contravariant=True)) – the item to send

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if the
  send stream has been explicitly closed

- [**BrokenResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.BrokenResourceError "anyio.BrokenResourceError") – if this
  stream has been rendered unusable due to external causes

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_
anyio.abc.UnreliableObjectStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectStream "Link to this definition")

Bases: [`UnreliableObjectReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectReceiveStream "anyio.abc.UnreliableObjectReceiveStream")\[`T_Item`\], [`UnreliableObjectSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectSendStream "anyio.abc.UnreliableObjectSendStream")\[`T_Item`\]

A bidirectional message stream which does not guarantee the order or reliability of message delivery.

_class_
anyio.abc.ObjectReceiveStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectReceiveStream "Link to this definition")

Bases: [`UnreliableObjectReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectReceiveStream "anyio.abc.UnreliableObjectReceiveStream")\[`T_co`\]

A receive message stream which guarantees that messages are received in the same order in which they were sent, and that
no messages are missed.

_class_
anyio.abc.ObjectSendStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectSendStream "Link to this definition")

Bases: [`UnreliableObjectSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectSendStream "anyio.abc.UnreliableObjectSendStream")\[`T_contra`\]

A send message stream which guarantees that messages are delivered in the same order in which they were sent, without
missing any messages in the middle.

_class_
anyio.abc.ObjectStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectStream "Link to this definition")

Bases: [`ObjectReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectReceiveStream "anyio.abc.ObjectReceiveStream")\[`T_Item`\], [`ObjectSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectSendStream "anyio.abc.ObjectSendStream")\[`T_Item`\], [`UnreliableObjectStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectStream "anyio.abc.UnreliableObjectStream")\[`T_Item`\]

A bidirectional message stream which guarantees the order and reliability of message delivery.

_abstract async_
send\_eof()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectStream.send_eof "Link to this definition")

Send an end-of-file indication to the peer.

You should not try to send any further data to this stream after calling this method. This method is idempotent (does
nothing on successive calls).

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_
anyio.abc.ByteReceiveStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteReceiveStream "Link to this definition")

Bases: [`AsyncResource`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AsyncResource "anyio.abc.AsyncResource"), [`TypedAttributeProvider`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeProvider "anyio.TypedAttributeProvider")

An interface for receiving bytes from a single peer.

Iterating this byte stream will yield a byte string of arbitrary length, but no more than 65536 bytes.

_abstract async_ receive(
_max\_bytes\=65536_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteReceiveStream.receive "Link to this definition")

Receive at most `max_bytes` bytes from the peer.

Note

Implementors of this interface should not return an
empty [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)") object, and users should
ignore them.

Parameters:

**max\_bytes** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – maximum number of
bytes to receive

Return type:

[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")

Returns:

the received bytes

Raises:

[**EndOfStream**](https://anyio.readthedocs.io/en/stable/api.html#anyio.EndOfStream "anyio.EndOfStream") – if this
stream has been closed from the other end

_class_
anyio.abc.ByteSendStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteSendStream "Link to this definition")

Bases: [`AsyncResource`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AsyncResource "anyio.abc.AsyncResource"), [`TypedAttributeProvider`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeProvider "anyio.TypedAttributeProvider")

An interface for sending bytes to a single peer.

_abstract async_ send(
_item_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteSendStream.send "Link to this definition")

Send the given bytes to the peer.

Parameters:

**item** ([`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")) – the bytes to send

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_
anyio.abc.ByteStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteStream "Link to this definition")

Bases: [`ByteReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteReceiveStream "anyio.abc.ByteReceiveStream"), [`ByteSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteSendStream "anyio.abc.ByteSendStream")

A bidirectional byte stream.

_abstract async_
send\_eof()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteStream.send_eof "Link to this definition")

Send an end-of-file indication to the peer.

You should not try to send any further data to this stream after calling this method. This method is idempotent (does
nothing on successive calls).

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_
anyio.abc.Listener[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Listener "Link to this definition")

Bases: [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.11)")\[`T_co`\], [`AsyncResource`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AsyncResource "anyio.abc.AsyncResource"), [`TypedAttributeProvider`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeProvider "anyio.TypedAttributeProvider")

An interface for objects that let you accept incoming connections.

_abstract async_ serve(_handler_,
_task\_group\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Listener.serve "Link to this definition")

Accept incoming connections as they come in and start tasks to handle them.

Parameters:

- **handler
  ** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[\[[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_co`,
  covariant=True)\], [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\]) – a
  callable that will be used to handle each accepted connection

- **task\_group
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`TaskGroup`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup "anyio.abc.TaskGroup")\]) –
  the task group that will be used to start tasks for handling each accepted connection (if omitted, an ad-hoc task
  group will be created)

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

anyio.abc.AnyUnreliableByteReceiveStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AnyUnreliableByteReceiveStream "Link to this definition")

alias
of [`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`UnreliableObjectReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectReceiveStream "anyio.abc.UnreliableObjectReceiveStream")\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\], [`ByteReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteReceiveStream "anyio.abc.ByteReceiveStream")\]

anyio.abc.AnyUnreliableByteSendStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AnyUnreliableByteSendStream "Link to this definition")

alias
of [`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`UnreliableObjectSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectSendStream "anyio.abc.UnreliableObjectSendStream")\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\], [`ByteSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteSendStream "anyio.abc.ByteSendStream")\]

anyio.abc.AnyUnreliableByteStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AnyUnreliableByteStream "Link to this definition")

alias
of [`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`UnreliableObjectStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectStream "anyio.abc.UnreliableObjectStream")\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\], [`ByteStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteStream "anyio.abc.ByteStream")\]

anyio.abc.AnyByteReceiveStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AnyByteReceiveStream "Link to this definition")

alias
of [`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`ObjectReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectReceiveStream "anyio.abc.ObjectReceiveStream")\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\], [`ByteReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteReceiveStream "anyio.abc.ByteReceiveStream")\]

anyio.abc.AnyByteSendStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AnyByteSendStream "Link to this definition")

alias
of [`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`ObjectSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectSendStream "anyio.abc.ObjectSendStream")\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\], [`ByteSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteSendStream "anyio.abc.ByteSendStream")\]

anyio.abc.AnyByteStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AnyByteStream "Link to this definition")

alias
of [`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`ObjectStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectStream "anyio.abc.ObjectStream")\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\], [`ByteStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteStream "anyio.abc.ByteStream")\]

_class_ anyio.streams.buffered.BufferedByteReceiveStream(
_receive\_stream_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.buffered.BufferedByteReceiveStream "Link to this definition")

Bases: [`ByteReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteReceiveStream "anyio.abc.ByteReceiveStream")

Wraps any bytes-based receive stream and uses a buffer to provide sophisticated receiving capabilities in the form of a
byte stream.

_async_
aclose()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.buffered.BufferedByteReceiveStream.aclose "Link to this definition")

Close the resource.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_property_
buffer_: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.buffered.BufferedByteReceiveStream.buffer "Link to this definition")

The bytes currently in the buffer.

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned
mapping (but the wrapper may override the callables from the wrapped instance).

_async_ receive(
_max\_bytes\=65536_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.buffered.BufferedByteReceiveStream.receive "Link to this definition")

Receive at most `max_bytes` bytes from the peer.

Note

Implementors of this interface should not return an
empty [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)") object, and users should
ignore them.

Parameters:

**max\_bytes** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – maximum number of
bytes to receive

Return type:

[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")

Returns:

the received bytes

Raises:

[**EndOfStream**](https://anyio.readthedocs.io/en/stable/api.html#anyio.EndOfStream "anyio.EndOfStream") – if this
stream has been closed from the other end

_async_ receive\_exactly(
_nbytes_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.buffered.BufferedByteReceiveStream.receive_exactly "Link to this definition")

Read exactly the given amount of bytes from the stream.

Parameters:

**nbytes** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – the number of bytes to
read

Return type:

[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")

Returns:

the bytes read

Raises:

[**IncompleteRead**](https://anyio.readthedocs.io/en/stable/api.html#anyio.IncompleteRead "anyio.IncompleteRead") – if
the stream was closed before the requested amount of bytes could be read from the stream

_async_ receive\_until(_delimiter_,
_max\_bytes_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.buffered.BufferedByteReceiveStream.receive_until "Link to this definition")

Read from the stream until the delimiter is found or max\_bytes have been read.

Parameters:

- **delimiter** ([`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")) – the marker to
  look for in the stream

- **max\_bytes** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – maximum number of
  bytes that will be read before
  raising [`DelimiterNotFound`](https://anyio.readthedocs.io/en/stable/api.html#anyio.DelimiterNotFound "anyio.DelimiterNotFound")

Return type:

[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")

Returns:

the bytes read (not including the delimiter)

Raises:

- [**IncompleteRead**](https://anyio.readthedocs.io/en/stable/api.html#anyio.IncompleteRead "anyio.IncompleteRead") – if
  the stream was closed before the delimiter was found

- [**DelimiterNotFound
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.DelimiterNotFound "anyio.DelimiterNotFound") – if the
  delimiter is not found within the bytes read up to the maximum allowed

_class_
anyio.streams.file.FileStreamAttribute[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileStreamAttribute "Link to this definition")

Bases: [`TypedAttributeSet`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeSet "anyio.TypedAttributeSet")

file_: [`BinaryIO`](https://docs.python.org/3/library/typing.html#typing.BinaryIO "(in Python v3.11)")_
_\= <object object>_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileStreamAttribute.file "Link to this definition")

the open file descriptor

fileno_: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")_
_\= <object object>_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileStreamAttribute.fileno "Link to this definition")

the file number, if available (file must be a real file or a TTY)

path_: [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.11)")_
_\= <object object>_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileStreamAttribute.path "Link to this definition")

the path of the file on the file system, if available (file must be a real file)

_class_ anyio.streams.file.FileReadStream(
_file_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileReadStream "Link to this definition")

Bases: `_BaseFileStream`, [`ByteReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteReceiveStream "anyio.abc.ByteReceiveStream")

A byte stream that reads from a file in the file system.

Parameters:

**file** ([`BinaryIO`](https://docs.python.org/3/library/typing.html#typing.BinaryIO "(in Python v3.11)")) – a file that
has been opened for reading in binary mode

New in version 3.0.

_async classmethod_ from\_path(
_path_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileReadStream.from_path "Link to this definition")

Create a file read stream by opening the given file.

Parameters:

**path
** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)") | [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\]) –
path of the file to read from

Return type:

[`FileReadStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileReadStream "anyio.streams.file.FileReadStream")

_async_ receive(
_max\_bytes\=65536_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileReadStream.receive "Link to this definition")

Receive at most `max_bytes` bytes from the peer.

Note

Implementors of this interface should not return an
empty [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)") object, and users should
ignore them.

Parameters:

**max\_bytes** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – maximum number of
bytes to receive

Return type:

[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")

Returns:

the received bytes

Raises:

[**EndOfStream**](https://anyio.readthedocs.io/en/stable/api.html#anyio.EndOfStream "anyio.EndOfStream") – if this
stream has been closed from the other end

_async_ seek(_position_,
_whence\=0_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileReadStream.seek "Link to this definition")

Seek the file to the given position.

Note

Not all file descriptors are seekable.

Parameters:

- **position** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – position to seek
  the file to

- **whence** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – controls
  how `position` is interpreted

Return type:

[`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")

Returns:

the new absolute position

Raises:

[**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "(in Python v3.11)") – if the file is not
seekable

_async_
tell()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileReadStream.tell "Link to this definition")

Return the current stream position.

Note

Not all file descriptors are seekable.

Return type:

[`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")

Returns:

the current absolute position

Raises:

[**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "(in Python v3.11)") – if the file is not
seekable

_class_ anyio.streams.file.FileWriteStream(
_file_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileWriteStream "Link to this definition")

Bases: `_BaseFileStream`, [`ByteSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteSendStream "anyio.abc.ByteSendStream")

A byte stream that writes to a file in the file system.

Parameters:

**file** ([`BinaryIO`](https://docs.python.org/3/library/typing.html#typing.BinaryIO "(in Python v3.11)")) – a file that
has been opened for writing in binary mode

New in version 3.0.

_async classmethod_ from\_path(_path_,
_append\=False_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileWriteStream.from_path "Link to this definition")

Create a file write stream by opening the given file for writing.

Parameters:

- **path
  ** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)") | [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\]) –
  path of the file to write to

- **append** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – if `True`, open the
  file for appending; if `False`, any existing file at the given path will be truncated

Return type:

[`FileWriteStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileWriteStream "anyio.streams.file.FileWriteStream")

_async_ send(
_item_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileWriteStream.send "Link to this definition")

Send the given bytes to the peer.

Parameters:

**item** ([`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")) – the bytes to send

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_ anyio.streams.memory.MemoryObjectReceiveStream(
_\_state_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectReceiveStream "Link to this definition")

Bases: [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.11)")\[`T_co`\], [`ObjectReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectReceiveStream "anyio.abc.ObjectReceiveStream")\[`T_co`\]

_async_
aclose()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectReceiveStream.aclose "Link to this definition")

Close the resource.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

clone()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectReceiveStream.clone "Link to this definition")

Create a clone of this receive stream.

Each clone can be closed separately. Only when all clones have been closed will the receiving end of the memory stream
be considered closed by the sending ends.

Return type:

[`MemoryObjectReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectReceiveStream "anyio.streams.memory.MemoryObjectReceiveStream")\[[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_co`,
covariant=True)\]

Returns:

the cloned stream

close()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectReceiveStream.close "Link to this definition")

Close the stream.

This works the exact same way
as [`aclose()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectReceiveStream.aclose "anyio.streams.memory.MemoryObjectReceiveStream.aclose"),
but is provided as a special case for the benefit of synchronous callbacks.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_async_
receive()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectReceiveStream.receive "Link to this definition")

Receive the next item.

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if the
  receive stream has been explicitly closed

- [**EndOfStream**](https://anyio.readthedocs.io/en/stable/api.html#anyio.EndOfStream "anyio.EndOfStream") – if this
  stream has been closed from the other end

- [**BrokenResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.BrokenResourceError "anyio.BrokenResourceError") – if this
  stream has been rendered unusable due to external causes

Return type:

[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_co`, covariant=True)

receive\_nowait()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectReceiveStream.receive_nowait "Link to this definition")

Receive the next item if it can be done without waiting.

Return type:

[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_co`, covariant=True)

Returns:

the received item

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if this
  send stream has been closed

- [**EndOfStream**](https://anyio.readthedocs.io/en/stable/api.html#anyio.EndOfStream "anyio.EndOfStream") – if the
  buffer is empty and this stream has been closed from the sending end

- [**WouldBlock**](https://anyio.readthedocs.io/en/stable/api.html#anyio.WouldBlock "anyio.WouldBlock") – if there are
  no items in the buffer and no tasks waiting to send

statistics()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectReceiveStream.statistics "Link to this definition")

Return statistics about the current state of this stream. :
rtype: [`MemoryObjectStreamStatistics`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectStreamStatistics "anyio.streams.memory.MemoryObjectStreamStatistics")

New in version 3.0.

_class_ anyio.streams.memory.MemoryObjectSendStream(
_\_state_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectSendStream "Link to this definition")

Bases: [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.11)")\[`T_contra`\], [`ObjectSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectSendStream "anyio.abc.ObjectSendStream")\[`T_contra`\]

_async_
aclose()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectSendStream.aclose "Link to this definition")

Close the resource.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

clone()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectSendStream.clone "Link to this definition")

Create a clone of this send stream.

Each clone can be closed separately. Only when all clones have been closed will the sending end of the memory stream be
considered closed by the receiving ends.

Return type:

[`MemoryObjectSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectSendStream "anyio.streams.memory.MemoryObjectSendStream")\[[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_contra`,
contravariant=True)\]

Returns:

the cloned stream

close()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectSendStream.close "Link to this definition")

Close the stream.

This works the exact same way
as [`aclose()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectSendStream.aclose "anyio.streams.memory.MemoryObjectSendStream.aclose"),
but is provided as a special case for the benefit of synchronous callbacks.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_async_ send(
_item_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectSendStream.send "Link to this definition")

Send an item to the stream.

If the buffer is full, this method blocks until there is again room in the buffer or the item can be sent directly to a
receiver.

Parameters:

**item** ([`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_contra`,
contravariant=True)) – the item to send

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if this
  send stream has been closed

- [**BrokenResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.BrokenResourceError "anyio.BrokenResourceError") – if the
  stream has been closed from the receiving end

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

send\_nowait(
_item_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectSendStream.send_nowait "Link to this definition")

Send an item immediately if it can be done without waiting.

Parameters:

**item** ([`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_contra`,
contravariant=True)) – the item to send

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if this
  send stream has been closed

- [**BrokenResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.BrokenResourceError "anyio.BrokenResourceError") – if the
  stream has been closed from the receiving end

- [**WouldBlock**](https://anyio.readthedocs.io/en/stable/api.html#anyio.WouldBlock "anyio.WouldBlock") – if the buffer
  is full and there are no tasks waiting to receive

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

statistics()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectSendStream.statistics "Link to this definition")

Return statistics about the current state of this stream. :
rtype: [`MemoryObjectStreamStatistics`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectStreamStatistics "anyio.streams.memory.MemoryObjectStreamStatistics")

New in version 3.0.

_class_ anyio.streams.memory.MemoryObjectStreamStatistics(_current\_buffer\_used_, _max\_buffer\_size_,
_open\_send\_streams_, _open\_receive\_streams_, _tasks\_waiting\_send_,
_tasks\_waiting\_receive_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectStreamStatistics "Link to this definition")

Bases: [`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple "(in Python v3.11)")

current\_buffer\_used_: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectStreamStatistics.current_buffer_used "Link to this definition")

number of items stored in the buffer

max\_buffer\_size_: [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectStreamStatistics.max_buffer_size "Link to this definition")

maximum number of items that can be stored on this stream (
or [`math.inf`](https://docs.python.org/3/library/math.html#math.inf "(in Python v3.11)"))

open\_receive\_streams_: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectStreamStatistics.open_receive_streams "Link to this definition")

number of unclosed clones of the receive stream

open\_send\_streams_: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectStreamStatistics.open_send_streams "Link to this definition")

number of unclosed clones of the send stream

tasks\_waiting\_receive_: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectStreamStatistics.tasks_waiting_receive "Link to this definition")

number of tasks blocked
on [`MemoryObjectReceiveStream.receive()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectReceiveStream.receive "anyio.streams.memory.MemoryObjectReceiveStream.receive")

tasks\_waiting\_send_: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectStreamStatistics.tasks_waiting_send "Link to this definition")

number of tasks blocked
on [`MemoryObjectSendStream.send()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectSendStream.send "anyio.streams.memory.MemoryObjectSendStream.send")

_class_ anyio.streams.stapled.MultiListener(
_listeners_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.MultiListener "Link to this definition")

Bases: [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.11)")\[`T_Stream`\], [`Listener`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Listener "anyio.abc.Listener")\[`T_Stream`\]

Combines multiple listeners into one, serving connections from all of them at once.

Any MultiListeners in the given collection of listeners will have their listeners moved into this one.

Extra attributes are provided from each listener, with each successive listener overriding any conflicting attributes
from the previous one.

Parameters:

**listeners** (_Sequence__\[
_[_Listener_](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Listener "anyio.abc.Listener")_\[__T\_Stream
__\]__\]_) – listeners to serve

_async_
aclose()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.MultiListener.aclose "Link to this definition")

Close the resource.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned
mapping (but the wrapper may override the callables from the wrapped instance).

_async_ serve(_handler_,
_task\_group\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.MultiListener.serve "Link to this definition")

Accept incoming connections as they come in and start tasks to handle them.

Parameters:

- **handler
  ** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[\[[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Stream`)\], [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\]) –
  a callable that will be used to handle each accepted connection

- **task\_group
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`TaskGroup`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup "anyio.abc.TaskGroup")\]) –
  the task group that will be used to start tasks for handling each accepted connection (if omitted, an ad-hoc task
  group will be created)

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_ anyio.streams.stapled.StapledByteStream(_send\_stream_,
_receive\_stream_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.StapledByteStream "Link to this definition")

Bases: [`ByteStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteStream "anyio.abc.ByteStream")

Combines two byte streams into a single, bidirectional byte stream.

Extra attributes will be provided from both streams, with the receive stream providing the values in case of a conflict.

Parameters:

- **send\_stream** ([
  _ByteSendStream_](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteSendStream "anyio.abc.ByteSendStream")) –
  the sending byte stream

- **receive\_stream** ([
  _ByteReceiveStream_](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteReceiveStream "anyio.abc.ByteReceiveStream")) –
  the receiving byte stream

_async_
aclose()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.StapledByteStream.aclose "Link to this definition")

Close the resource.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned
mapping (but the wrapper may override the callables from the wrapped instance).

_async_ receive(
_max\_bytes\=65536_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.StapledByteStream.receive "Link to this definition")

Receive at most `max_bytes` bytes from the peer.

Note

Implementors of this interface should not return an
empty [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)") object, and users should
ignore them.

Parameters:

**max\_bytes** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – maximum number of
bytes to receive

Return type:

[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")

Returns:

the received bytes

Raises:

[**EndOfStream**](https://anyio.readthedocs.io/en/stable/api.html#anyio.EndOfStream "anyio.EndOfStream") – if this
stream has been closed from the other end

_async_ send(
_item_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.StapledByteStream.send "Link to this definition")

Send the given bytes to the peer.

Parameters:

**item** ([`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")) – the bytes to send

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_async_
send\_eof()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.StapledByteStream.send_eof "Link to this definition")

Send an end-of-file indication to the peer.

You should not try to send any further data to this stream after calling this method. This method is idempotent (does
nothing on successive calls).

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_ anyio.streams.stapled.StapledObjectStream(_send\_stream_,
_receive\_stream_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.StapledObjectStream "Link to this definition")

Bases: [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.11)")\[`T_Item`\], [`ObjectStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectStream "anyio.abc.ObjectStream")\[`T_Item`\]

Combines two object streams into a single, bidirectional object stream.

Extra attributes will be provided from both streams, with the receive stream providing the values in case of a conflict.

Parameters:

- **send\_stream** ([
  _ObjectSendStream_](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectSendStream "anyio.abc.ObjectSendStream")) –
  the sending object stream

- **receive\_stream** ([
  _ObjectReceiveStream_](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectReceiveStream "anyio.abc.ObjectReceiveStream")) –
  the receiving object stream

_async_
aclose()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.StapledObjectStream.aclose "Link to this definition")

Close the resource.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned
mapping (but the wrapper may override the callables from the wrapped instance).

_async_
receive()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.StapledObjectStream.receive "Link to this definition")

Receive the next item.

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if the
  receive stream has been explicitly closed

- [**EndOfStream**](https://anyio.readthedocs.io/en/stable/api.html#anyio.EndOfStream "anyio.EndOfStream") – if this
  stream has been closed from the other end

- [**BrokenResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.BrokenResourceError "anyio.BrokenResourceError") – if this
  stream has been rendered unusable due to external causes

Return type:

[`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Item`)

_async_ send(
_item_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.StapledObjectStream.send "Link to this definition")

Send an item to the peer(s).

Parameters:

**item** ([`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "(in Python v3.11)")(`T_Item`)) – the
item to send

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if the
  send stream has been explicitly closed

- [**BrokenResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.BrokenResourceError "anyio.BrokenResourceError") – if this
  stream has been rendered unusable due to external causes

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_async_
send\_eof()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.StapledObjectStream.send_eof "Link to this definition")

Send an end-of-file indication to the peer.

You should not try to send any further data to this stream after calling this method. This method is idempotent (does
nothing on successive calls).

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_ anyio.streams.text.TextReceiveStream(_transport\_stream_, _encoding\='utf-8'_,
_errors\='strict'_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.text.TextReceiveStream "Link to this definition")

Bases: [`ObjectReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectReceiveStream "anyio.abc.ObjectReceiveStream")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\]

Stream wrapper that decodes bytes to strings using the given encoding.

Decoding is done
using [`IncrementalDecoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder "(in Python v3.11)")
which returns any completely received unicode characters as soon as they come in.

Parameters:

- **transport\_stream
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[`ObjectReceiveStream`\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\], [`ByteReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteReceiveStream "anyio.abc.ByteReceiveStream")\]) –
  any bytes-based receive stream

- **encoding** (`InitVar`) – character encoding to use for decoding bytes to strings (defaults to `utf-8`)

- **errors** (`InitVar`) – handling scheme for decoding errors (defaults to `strict`; see
  the [codecs module documentation](https://docs.python.org/3/library/codecs.html#codec-objects) for a comprehensive
  list of options)

_async_
aclose()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.text.TextReceiveStream.aclose "Link to this definition")

Close the resource.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned
mapping (but the wrapper may override the callables from the wrapped instance).

_async_
receive()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.text.TextReceiveStream.receive "Link to this definition")

Receive the next item.

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if the
  receive stream has been explicitly closed

- [**EndOfStream**](https://anyio.readthedocs.io/en/stable/api.html#anyio.EndOfStream "anyio.EndOfStream") – if this
  stream has been closed from the other end

- [**BrokenResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.BrokenResourceError "anyio.BrokenResourceError") – if this
  stream has been rendered unusable due to external causes

Return type:

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")

_class_ anyio.streams.text.TextSendStream(_transport\_stream_, _encoding\='utf-8'_,
_errors\='strict'_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.text.TextSendStream "Link to this definition")

Bases: [`ObjectSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectSendStream "anyio.abc.ObjectSendStream")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\]

Sends strings to the wrapped stream as bytes using the given encoding.

Parameters:

- **transport\_stream** (_AnyByteSendStream_) – any bytes-based send stream

- **encoding** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – character encoding
  to use for encoding strings to bytes (defaults to `utf-8`)

- **errors** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – handling scheme for
  encoding errors (defaults to `strict`; see
  the [codecs module documentation](https://docs.python.org/3/library/codecs.html#codec-objects) for a comprehensive
  list of options)

_async_
aclose()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.text.TextSendStream.aclose "Link to this definition")

Close the resource.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned
mapping (but the wrapper may override the callables from the wrapped instance).

_async_ send(
_item_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.text.TextSendStream.send "Link to this definition")

Send an item to the peer(s).

Parameters:

**item** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – the item to send

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if the
  send stream has been explicitly closed

- [**BrokenResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.BrokenResourceError "anyio.BrokenResourceError") – if this
  stream has been rendered unusable due to external causes

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_ anyio.streams.text.TextStream(_transport\_stream_, _encoding\='utf-8'_,
_errors\='strict'_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.text.TextStream "Link to this definition")

Bases: [`ObjectStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectStream "anyio.abc.ObjectStream")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\]

A bidirectional stream that decodes bytes to strings on receive and encodes strings to bytes on send.

Extra attributes will be provided from both streams, with the receive stream providing the values in case of a conflict.

Parameters:

- **transport\_stream** (_AnyByteStream_) – any bytes-based stream

- **encoding** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – character encoding
  to use for encoding/decoding strings to/from bytes (defaults to `utf-8`)

- **errors** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – handling scheme for
  encoding errors (defaults to `strict`; see
  the [codecs module documentation](https://docs.python.org/3/library/codecs.html#codec-objects) for a comprehensive
  list of options)

_async_
aclose()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.text.TextStream.aclose "Link to this definition")

Close the resource.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned
mapping (but the wrapper may override the callables from the wrapped instance).

_async_
receive()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.text.TextStream.receive "Link to this definition")

Receive the next item.

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if the
  receive stream has been explicitly closed

- [**EndOfStream**](https://anyio.readthedocs.io/en/stable/api.html#anyio.EndOfStream "anyio.EndOfStream") – if this
  stream has been closed from the other end

- [**BrokenResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.BrokenResourceError "anyio.BrokenResourceError") – if this
  stream has been rendered unusable due to external causes

Return type:

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")

_async_ send(
_item_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.text.TextStream.send "Link to this definition")

Send an item to the peer(s).

Parameters:

**item** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – the item to send

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if the
  send stream has been explicitly closed

- [**BrokenResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.BrokenResourceError "anyio.BrokenResourceError") – if this
  stream has been rendered unusable due to external causes

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_async_
send\_eof()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.text.TextStream.send_eof "Link to this definition")

Send an end-of-file indication to the peer.

You should not try to send any further data to this stream after calling this method. This method is idempotent (does
nothing on successive calls).

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_
anyio.streams.tls.TLSAttribute[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSAttribute "Link to this definition")

Bases: [`TypedAttributeSet`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeSet "anyio.TypedAttributeSet")

Contains Transport Layer Security related attributes.

alpn\_protocol_: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\]_
_\= <object object>_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSAttribute.alpn_protocol "Link to this definition")

the selected ALPN protocol

channel\_binding\_tls\_unique_: [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")_
_\= <object object>_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSAttribute.channel_binding_tls_unique "Link to this definition")

the channel binding for type `tls-unique`

cipher_: [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")\]_
_\= <object object>_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSAttribute.cipher "Link to this definition")

the selected cipher

peer\_certificate\_binary_: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\]_
_\= <object object>_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSAttribute.peer_certificate_binary "Link to this definition")

the peer certificate in binary form

server\_side_: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")_
_\= <object object>_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSAttribute.server_side "Link to this definition")

`True` if this is the server side of the connection

shared\_ciphers_: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")\[[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")\]\]\]_
_\= <object object>_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSAttribute.shared_ciphers "Link to this definition")

ciphers shared by the client during the TLS handshake (`None` if this is the client side)

ssl\_object_: [`SSLObject`](https://docs.python.org/3/library/ssl.html#ssl.SSLObject "(in Python v3.11)")_
_\= <object object>_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSAttribute.ssl_object "Link to this definition")

the [`SSLObject`](https://docs.python.org/3/library/ssl.html#ssl.SSLObject "(in Python v3.11)") used for encryption

standard\_compatible_: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")_
_\= <object object>_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSAttribute.standard_compatible "Link to this definition")

`True` if this stream does (and expects) a closing TLS handshake when the stream is being closed

tls\_version_: [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")_
_\= <object object>_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSAttribute.tls_version "Link to this definition")

the TLS protocol version (e.g. `TLSv1.2`)

_class_ anyio.streams.tls.TLSStream(_transport\_stream_, _standard\_compatible_, _\_ssl\_object_, _\_read\_bio_,
_\_write\_bio_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream "Link to this definition")

Bases: [`ByteStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteStream "anyio.abc.ByteStream")

A stream wrapper that encrypts all sent data and decrypts received data.

This class has no public initializer;
use [`wrap()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream.wrap "anyio.streams.tls.TLSStream.wrap")
instead. All extra attributes
from [`TLSAttribute`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSAttribute "anyio.streams.tls.TLSAttribute")
are supported.

Variables:

**transport\_stream** (_AnyByteStream_) – the wrapped stream

_async_
aclose()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream.aclose "Link to this definition")

Close the resource.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned
mapping (but the wrapper may override the callables from the wrapped instance).

_async_ receive(
_max\_bytes\=65536_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream.receive "Link to this definition")

Receive at most `max_bytes` bytes from the peer.

Note

Implementors of this interface should not return an
empty [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)") object, and users should
ignore them.

Parameters:

**max\_bytes** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – maximum number of
bytes to receive

Return type:

[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")

Returns:

the received bytes

Raises:

[**EndOfStream**](https://anyio.readthedocs.io/en/stable/api.html#anyio.EndOfStream "anyio.EndOfStream") – if this
stream has been closed from the other end

_async_ send(
_item_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream.send "Link to this definition")

Send the given bytes to the peer.

Parameters:

**item** ([`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")) – the bytes to send

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_async_
send\_eof()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream.send_eof "Link to this definition")

Send an end-of-file indication to the peer.

You should not try to send any further data to this stream after calling this method. This method is idempotent (does
nothing on successive calls).

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_async_
unwrap()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream.unwrap "Link to this definition")

Does the TLS closing handshake.

Return type:

[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.11)")\[[`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[`ObjectStream`\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\], [`ByteStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteStream "anyio.abc.ByteStream")\], [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\]

Returns:

a tuple of (wrapped byte stream, bytes left in the read buffer)

_async classmethod_ wrap(_transport\_stream_, _\*_, _server\_side\=None_, _hostname\=None_, _ssl\_context\=None_,
_standard\_compatible\=True_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream.wrap "Link to this definition")

Wrap an existing stream with Transport Layer Security.

This performs a TLS handshake with the peer.

Parameters:

- **transport\_stream
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[`ObjectStream`\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\], [`ByteStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteStream "anyio.abc.ByteStream")\]) –
  a bytes-transporting stream to wrap

- **server\_side
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")\]) – `True`
  if this is the server side of the connection, `False` if this is the client side (if omitted, will be set to `False`
  if `hostname` has been provided, `False` otherwise). Used only to create a default context when an explicit context
  has not been provided.

- **hostname
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\]) –
  host name of the peer (if host name checking is desired)

- **ssl\_context
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "(in Python v3.11)")\]) –
  the SSLContext object to use (if not provided, a secure default will be created)

- **standard\_compatible** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) –
  if `False`, skip the closing handshake when closing the connection, and don’t raise an exception if the peer does the
  same

Raises:

[**SSLError**](https://docs.python.org/3/library/ssl.html#ssl.SSLError "(in Python v3.11)") – if the TLS handshake fails

Return type:

[`TLSStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream "anyio.streams.tls.TLSStream")

_class_ anyio.streams.tls.TLSListener(_listener_, _ssl\_context_, _standard\_compatible\=True_,
_handshake\_timeout\=30_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSListener "Link to this definition")

Bases: [`Listener`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Listener "anyio.abc.Listener")\[[`TLSStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream "anyio.streams.tls.TLSStream")\]

A convenience listener that wraps another listener and auto-negotiates a TLS session on every accepted connection.

If the TLS handshake times out or raises an
exception, [`handle_handshake_error()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSListener.handle_handshake_error "anyio.streams.tls.TLSListener.handle_handshake_error")
is called to do whatever post-mortem processing is deemed necessary.

Supports only
the [`standard_compatible`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSAttribute.standard_compatible "anyio.streams.tls.TLSAttribute.standard_compatible")
extra attribute.

Parameters:

- **listener** ([_Listener_](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Listener "anyio.abc.Listener")) –
  the listener to wrap

- **ssl\_context** ([`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "(in Python v3.11)")) – the
  SSL context object

- **standard\_compatible** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – a
  flag passed through
  to [`TLSStream.wrap()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream.wrap "anyio.streams.tls.TLSStream.wrap")

- **handshake\_timeout** ([`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – time
  limit for the TLS handshake (passed
  to [`fail_after()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.fail_after "anyio.fail_after"))

_async_
aclose()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSListener.aclose "Link to this definition")

Close the resource.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned
mapping (but the wrapper may override the callables from the wrapped instance).

_async static_ handle\_handshake\_error(_exc_,
_stream_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSListener.handle_handshake_error "Link to this definition")

Handle an exception raised during the TLS handshake.

This method does 3 things:

1. Forcefully closes the original stream

2. Logs the exception (unless it was a cancellation exception) using the `anyio.streams.tls` logger

3. Reraises the exception if it was a base exception or a cancellation exception

Parameters:

- **exc** ([`BaseException`](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.11)")) – the
  exception

- **stream
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[`ObjectStream`\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\], [`ByteStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteStream "anyio.abc.ByteStream")\]) –
  the original stream

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_async_ serve(_handler_,
_task\_group\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSListener.serve "Link to this definition")

Accept incoming connections as they come in and start tasks to handle them.

Parameters:

- **handler
  ** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[\[[`TLSStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream "anyio.streams.tls.TLSStream")\], [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\]) –
  a callable that will be used to handle each accepted connection

- **task\_group
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`TaskGroup`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup "anyio.abc.TaskGroup")\]) –
  the task group that will be used to start tasks for handling each accepted connection (if omitted, an ad-hoc task
  group will be created)

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

## Sockets and networking[¶](https://anyio.readthedocs.io/en/stable/api.html#sockets-and-networking "Link to this heading")

_async_ anyio.connect\_tcp(_remote\_host_, _remote\_port_, _\*_, _local\_host\=None_, _tls\=False_,
_ssl\_context\=None_, _tls\_standard\_compatible\=True_, _tls\_hostname\=None_,
_happy\_eyeballs\_delay\=0.25_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.connect_tcp "Link to this definition")

Connect to a host using the TCP protocol.

This function implements the stateless version of the Happy Eyeballs algorithm (RFC 6555). If `remote_host` is a host
name that resolves to multiple IP addresses, each one is tried until one connection attempt succeeds. If the first
attempt does not connected within 250 milliseconds, a second attempt is started using the next address in the list, and
so on. On IPv6 enabled systems, an IPv6 address (if available) is tried first.

When the connection has been established, a TLS handshake will be done if either `ssl_context` or `tls_hostname` is
not `None`, or if `tls` is `True`.

Parameters:

- **remote\_host
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "(in Python v3.11)"), [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "(in Python v3.11)")\]) –
  the IP address or host name to connect to

- **remote\_port** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – port on the
  target host to connect to

- **local\_host
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "(in Python v3.11)"), [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "(in Python v3.11)"), [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]) –
  the interface address or name to bind the socket to before connecting

- **tls** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – `True` to do a TLS
  handshake with the connected stream and return
  a [`TLSStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream "anyio.streams.tls.TLSStream")
  instead

- **ssl\_context
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "(in Python v3.11)")\]) –
  the SSL context object to use (if omitted, a default context is created)

- **tls\_standard\_compatible** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) –
  If `True`, performs the TLS shutdown handshake before closing the stream and requires that the server does this as
  well. Otherwise, [`SSLEOFError`](https://docs.python.org/3/library/ssl.html#ssl.SSLEOFError "(in Python v3.11)") may
  be raised during reads from the stream. Some protocols, such as HTTP, require this option to be `False`.
  See [`wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "(in Python v3.11)") for
  details.

- **tls\_hostname
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\]) –
  host name to check the server certificate against (defaults to the value of `remote_host`)

- **happy\_eyeballs\_delay** ([`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) –
  delay (in seconds) before starting the next connection attempt

Return type:

[`SocketStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketStream "anyio.abc.SocketStream") | [`TLSStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream "anyio.streams.tls.TLSStream")

Returns:

a socket stream object if no TLS handshake was done, otherwise a TLS stream

Raises:

[**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "(in Python v3.11)") – if the connection attempt
fails

_async_ anyio.connect\_unix(
_path_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.connect_unix "Link to this definition")

Connect to the given UNIX socket.

Not available on Windows.

Parameters:

**path
** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)") | [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\]) –
path to the socket

Return type:

[`UNIXSocketStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UNIXSocketStream "anyio.abc.UNIXSocketStream")

Returns:

a socket stream object

_async_ anyio.create\_tcp\_listener(_\*_, _local\_host\=None_, _local\_port\=0_, _family\=AddressFamily.AF\_UNSPEC_,
_backlog\=65536_,
_reuse\_port\=False_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.create_tcp_listener "Link to this definition")

Create a TCP socket listener.

Parameters:

- **local\_port** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – port number to
  listen on

- **local\_host
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "(in Python v3.11)"), [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "(in Python v3.11)"), [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]) –
  IP address of the interface to listen on. If omitted, listen on all IPv4 and IPv6 interfaces. To listen on all
  interfaces on a specific address family, use `0.0.0.0` for IPv4 or `::` for IPv6.

- **family
  ** ([`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.11)")\[`<AddressFamily.AF_UNSPEC: 0>`, `<AddressFamily.AF_INET: 2>`, `<AddressFamily.AF_INET6: 10>`\]) –
  address family (used if `local_host` was omitted)

- **backlog** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – maximum number of
  queued incoming connections (up to a maximum of 2\*\*16, or 65536)

- **reuse\_port** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – `True` to
  allow multiple sockets to bind to the same address/port (not supported on Windows)

Return type:

[`MultiListener`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.MultiListener "anyio.streams.stapled.MultiListener")\[[`SocketStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketStream "anyio.abc.SocketStream")\]

Returns:

a list of listener objects

_async_ anyio.create\_unix\_listener(_path_, _\*_, _mode\=None_,
_backlog\=65536_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.create_unix_listener "Link to this definition")

Create a UNIX socket listener.

Not available on Windows.

Parameters:

- **path
  ** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)") | [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\]) –
  path of the socket

- **mode
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")\]) –
  permissions to set on the socket

- **backlog** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – maximum number of
  queued incoming connections (up to a maximum of 2\*\*16, or 65536)

Return type:

[`SocketListener`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketListener "anyio.abc.SocketListener")

Returns:

a listener object

Changed in version 3.0: If a socket already exists on the file system in the given path, it will be removed first.

_async_ anyio.create\_udp\_socket(_family\=AddressFamily.AF\_UNSPEC_, _\*_, _local\_host\=None_, _local\_port\=0_,
_reuse\_port\=False_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.create_udp_socket "Link to this definition")

Create a UDP socket.

If `port` has been given, the socket will be bound to this port on the local machine, making this socket suitable for
providing UDP based services.

Parameters:

- **family
  ** ([`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.11)")\[`<AddressFamily.AF_UNSPEC: 0>`, `<AddressFamily.AF_INET: 2>`, `<AddressFamily.AF_INET6: 10>`\]) –
  address family (`AF_INET` or `AF_INET6`) – automatically determined from `local_host` if omitted

- **local\_host
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "(in Python v3.11)"), [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "(in Python v3.11)"), [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]) –
  IP address or host name of the local interface to bind to

- **local\_port** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – local port to
  bind to

- **reuse\_port** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – `True` to
  allow multiple sockets to bind to the same address/port (not supported on Windows)

Return type:

[`UDPSocket`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UDPSocket "anyio.abc.UDPSocket")

Returns:

a UDP socket

_async_ anyio.create\_connected\_udp\_socket(_remote\_host_, _remote\_port_, _\*_, _family\=AddressFamily.AF\_UNSPEC_,
_local\_host\=None_, _local\_port\=0_,
_reuse\_port\=False_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.create_connected_udp_socket "Link to this definition")

Create a connected UDP socket.

Connected UDP sockets can only communicate with the specified remote host/port, an any packets sent from other sources
are dropped.

Parameters:

- **remote\_host
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "(in Python v3.11)"), [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "(in Python v3.11)")\]) –
  remote host to set as the default target

- **remote\_port** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – port on the
  remote host to set as the default target

- **family
  ** ([`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.11)")\[`<AddressFamily.AF_UNSPEC: 0>`, `<AddressFamily.AF_INET: 2>`, `<AddressFamily.AF_INET6: 10>`\]) –
  address family (`AF_INET` or `AF_INET6`) – automatically determined from `local_host` or `remote_host` if omitted

- **local\_host
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "(in Python v3.11)"), [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "(in Python v3.11)"), [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]) –
  IP address or host name of the local interface to bind to

- **local\_port** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – local port to
  bind to

- **reuse\_port** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – `True` to
  allow multiple sockets to bind to the same address/port (not supported on Windows)

Return type:

[`ConnectedUDPSocket`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ConnectedUDPSocket "anyio.abc.ConnectedUDPSocket")

Returns:

a connected UDP socket

_async_ anyio.getaddrinfo(_host_, _port_, _\*_, _family\=0_, _type\=0_, _proto\=0_,
_flags\=0_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.getaddrinfo "Link to this definition")

Look up a numeric IP address given a host name.

Internationalized domain names are translated according to the (non-transitional) IDNA 2008 standard.

Note

4-tuple IPv6 socket addresses are automatically converted to 2-tuples of (host, port), unlike
what [`socket.getaddrinfo()`](https://docs.python.org/3/library/socket.html#socket.getaddrinfo "(in Python v3.11)")
does.

Parameters:

- **host
  ** ([`UnionType`](https://docs.python.org/3/library/types.html#types.UnionType "(in Python v3.11)")\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]) –
  host name

- **port
  ** ([`UnionType`](https://docs.python.org/3/library/types.html#types.UnionType "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)"), [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]) –
  port number

- **family** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)") | `AddressFamily`) –
  socket family (‘AF\_INET\`, …)

- **type** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)") | `SocketKind`) – socket
  type (`SOCK_STREAM`, …)

- **proto** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – protocol number

- **flags** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – flags to pass to
  upstream `getaddrinfo()`

Return type:

[`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")\[[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.11)")\[`AddressFamily`, `SocketKind`, [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")\]\]\]

Returns:

list of tuples containing (family, type, proto, canonname, sockaddr)

anyio.getnameinfo(_sockaddr_,
_flags\=0_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.getnameinfo "Link to this definition")

Look up the host name of an IP address.

Parameters:

- **sockaddr
  ** ([`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")\]) –
  socket address (e.g. (ipaddress, port) for IPv4)

- **flags** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – flags to pass to
  upstream `getnameinfo()`

Return type:

[`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "(in Python v3.11)")\[[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\]\]

Returns:

a tuple of (host name, service name)

anyio.wait\_socket\_readable(
_sock_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.wait_socket_readable "Link to this definition")

Wait until the given socket has data to be read.

This does **NOT** work on Windows when using the asyncio backend with a proactor event loop (default on py3.8+).

Warning

Only use this on raw sockets that have not been wrapped by any higher level constructs like socket streams!

Parameters:

**sock** ([`socket`](https://docs.python.org/3/library/socket.html#socket.socket "(in Python v3.11)")) – a socket object

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if the
  socket was closed while waiting for the socket to become readable

- [**BusyResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.BusyResourceError "anyio.BusyResourceError") – if another
  task is already waiting for the socket to become readable

Return type:

[`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "(in Python v3.11)")\[[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]

anyio.wait\_socket\_writable(
_sock_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.wait_socket_writable "Link to this definition")

Wait until the given socket can be written to.

This does **NOT** work on Windows when using the asyncio backend with a proactor event loop (default on py3.8+).

Warning

Only use this on raw sockets that have not been wrapped by any higher level constructs like socket streams!

Parameters:

**sock** ([`socket`](https://docs.python.org/3/library/socket.html#socket.socket "(in Python v3.11)")) – a socket object

Raises:

- [**ClosedResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "anyio.ClosedResourceError") – if the
  socket was closed while waiting for the socket to become writable

- [**BusyResourceError
  **](https://anyio.readthedocs.io/en/stable/api.html#anyio.BusyResourceError "anyio.BusyResourceError") – if another
  task is already waiting for the socket to become writable

Return type:

[`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "(in Python v3.11)")\[[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]

_class_
anyio.abc.SocketAttribute[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketAttribute "Link to this definition")

Bases: [`TypedAttributeSet`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeSet "anyio.TypedAttributeSet")

_class_
anyio.abc.SocketStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketStream "Link to this definition")

Bases: [`ByteStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteStream "anyio.abc.ByteStream"), `_SocketProvider`

Transports bytes over a socket.

Supports all relevant extra attributes
from [`SocketAttribute`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketAttribute "anyio.abc.SocketAttribute").

_class_
anyio.abc.SocketListener[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketListener "Link to this definition")

Bases: [`Listener`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Listener "anyio.abc.Listener")\[[`SocketStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketStream "anyio.abc.SocketStream")\], `_SocketProvider`

Listens to incoming socket connections.

Supports all relevant extra attributes
from [`SocketAttribute`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketAttribute "anyio.abc.SocketAttribute").

_abstract async_
accept()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketListener.accept "Link to this definition")

Accept an incoming connection.

Return type:

[`SocketStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketStream "anyio.abc.SocketStream")

_async_ serve(_handler_,
_task\_group\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketListener.serve "Link to this definition")

Accept incoming connections as they come in and start tasks to handle them.

Parameters:

- **handler
  ** ([`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")\[\[[`SocketStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketStream "anyio.abc.SocketStream")\], [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\]) –
  a callable that will be used to handle each accepted connection

- **task\_group
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`TaskGroup`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.TaskGroup "anyio.abc.TaskGroup")\]) –
  the task group that will be used to start tasks for handling each accepted connection (if omitted, an ad-hoc task
  group will be created)

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_
anyio.abc.UDPSocket[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UDPSocket "Link to this definition")

Bases: [`UnreliableObjectStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectStream "anyio.abc.UnreliableObjectStream")\[`Tuple`\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)"), `Tuple`\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")\]\]\], `_SocketProvider`

Represents an unconnected UDP socket.

Supports all relevant extra attributes
from [`SocketAttribute`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketAttribute "anyio.abc.SocketAttribute").

_async_ sendto(_data_, _host_,
_port_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UDPSocket.sendto "Link to this definition")

Alias
for [`send()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectSendStream.send "anyio.abc.UnreliableObjectSendStream.send") ((
data, (host, port))).

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_
anyio.abc.ConnectedUDPSocket[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ConnectedUDPSocket "Link to this definition")

Bases: [`UnreliableObjectStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectStream "anyio.abc.UnreliableObjectStream")\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\], `_SocketProvider`

Represents an connected UDP socket.

Supports all relevant extra attributes
from [`SocketAttribute`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketAttribute "anyio.abc.SocketAttribute").

_class_
anyio.abc.UNIXSocketStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UNIXSocketStream "Link to this definition")

Bases: [`SocketStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketStream "anyio.abc.SocketStream")

_abstract async_ receive\_fds(_msglen_,
_maxfds_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UNIXSocketStream.receive_fds "Link to this definition")

Receive file descriptors along with a message from the peer.

Parameters:

- **msglen** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – length of the message
  to expect from the peer

- **maxfds** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – maximum number of
  file descriptors to expect from the peer

Return type:

[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.11)")\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")\[[`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")\]\]

Returns:

a tuple of (message, file descriptors)

_abstract async_ send\_fds(_message_,
_fds_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UNIXSocketStream.send_fds "Link to this definition")

Send file descriptors along with a message to the peer.

Parameters:

- **message** ([`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")) – a non-empty
  bytestring

- **fds
  ** ([`Collection`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "(in Python v3.11)")\[[`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)") | [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "(in Python v3.11)")\]) –
  a collection of files (either numeric file descriptors or open file or socket objects)

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

## Subprocesses[¶](https://anyio.readthedocs.io/en/stable/api.html#subprocesses "Link to this heading")

_async_ anyio.run\_process(_command_, _\*_, _input\=None_, _stdout\=\-1_, _stderr\=\-1_, _check\=True_, _cwd\=None_,
_env\=None_,
_start\_new\_session\=False_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.run_process "Link to this definition")

Run an external command in a subprocess and wait until it completes.

Parameters:

- **command
  ** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)") | [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)") | [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)") | [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\]) –
  either a string to pass to the shell, or an iterable of strings containing the executable name or path and its
  arguments

- **input
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\]) –
  bytes passed to the standard input of the subprocess

- **stdout
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)"), [`IO`](https://docs.python.org/3/library/typing.html#typing.IO "(in Python v3.11)")\[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\], [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]) –
  one
  of [`subprocess.PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "(in Python v3.11)"), [`subprocess.DEVNULL`](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "(in Python v3.11)"),
  a file-like object, or None

- **stderr
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)"), [`IO`](https://docs.python.org/3/library/typing.html#typing.IO "(in Python v3.11)")\[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\], [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]) –
  one
  of [`subprocess.PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "(in Python v3.11)"), [`subprocess.DEVNULL`](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "(in Python v3.11)"), [`subprocess.STDOUT`](https://docs.python.org/3/library/subprocess.html#subprocess.STDOUT "(in Python v3.11)"),
  a file-like object, or None

- **check** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – if `True`,
  raise [`CalledProcessError`](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError "(in Python v3.11)")
  if the process terminates with a return code other than 0

- **cwd
  ** ([`UnionType`](https://docs.python.org/3/library/types.html#types.UnionType "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)"), [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\], [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]) –
  If not `None`, change the working directory to this before running the command

- **env
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\]\]) –
  if not `None`, this mapping replaces the inherited environment variables from the parent process

- **start\_new\_session** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) –
  if `true` the setsid() system call will be made in the child process prior to the execution of the subprocess. (POSIX
  only)

Return type:

[`CompletedProcess`](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess "(in Python v3.11)")\[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\]

Returns:

an object representing the completed process

Raises:

[**CalledProcessError
**](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError "(in Python v3.11)") – if `check`
is `True` and the process exits with a nonzero return code

_async_ anyio.open\_process(_command_, _\*_, _stdin\=\-1_, _stdout\=\-1_, _stderr\=\-1_, _cwd\=None_, _env\=None_,
_start\_new\_session\=False_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.open_process "Link to this definition")

Start an external command in a subprocess.

Parameters:

- **command
  ** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)") | [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)") | [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)") | [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)")\]) –
  either a string to pass to the shell, or an iterable of strings containing the executable name or path and its
  arguments

- **stdin
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)"), [`IO`](https://docs.python.org/3/library/typing.html#typing.IO "(in Python v3.11)")\[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\], [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]) –
  one
  of [`subprocess.PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "(in Python v3.11)"), [`subprocess.DEVNULL`](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "(in Python v3.11)"),
  a file-like object, or `None`

- **stdout
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)"), [`IO`](https://docs.python.org/3/library/typing.html#typing.IO "(in Python v3.11)")\[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\], [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]) –
  one
  of [`subprocess.PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "(in Python v3.11)"), [`subprocess.DEVNULL`](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "(in Python v3.11)"),
  a file-like object, or `None`

- **stderr
  ** ([`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.11)")\[[`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)"), [`IO`](https://docs.python.org/3/library/typing.html#typing.IO "(in Python v3.11)")\[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.11)")\], [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]) –
  one
  of [`subprocess.PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "(in Python v3.11)"), [`subprocess.DEVNULL`](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "(in Python v3.11)"), [`subprocess.STDOUT`](https://docs.python.org/3/library/subprocess.html#subprocess.STDOUT "(in Python v3.11)"),
  a file-like object, or `None`

- **cwd
  ** ([`UnionType`](https://docs.python.org/3/library/types.html#types.UnionType "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)"), [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\], [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")\]) –
  If not `None`, the working directory is changed before executing

- **env
  ** ([`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.11)")\[[`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.11)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")\]\]) –
  If env is not `None`, it must be a mapping that defines the environment variables for the new process

- **start\_new\_session** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) –
  if `true` the setsid() system call will be made in the child process prior to the execution of the subprocess. (POSIX
  only)

Return type:

[`Process`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Process "anyio.abc.Process")

Returns:

an asynchronous process object

_class_
anyio.abc.Process[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Process "Link to this definition")

Bases: [`AsyncResource`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.AsyncResource "anyio.abc.AsyncResource")

An asynchronous version
of [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "(in Python v3.11)").

_abstract_ kill()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Process.kill "Link to this definition")

Kills the process.

On Windows, this calls `TerminateProcess()`. On POSIX systems, this sends `SIGKILL` to the process. :
rtype: [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_abstract property_
pid_: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Process.pid "Link to this definition")

The process ID of the process.

_abstract property_
returncode_: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Process.returncode "Link to this definition")

The return code of the process. If the process has not yet terminated, this will be `None`.

_abstract_ send\_signal(
_signal_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Process.send_signal "Link to this definition")

Send a signal to the subprocess.

Parameters:

**signal** ([`Signals`](https://docs.python.org/3/library/signal.html#signal.Signals "(in Python v3.11)")) – the signal
number (e.g. [`signal.SIGHUP`](https://docs.python.org/3/library/signal.html#signal.SIGHUP "(in Python v3.11)"))

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_abstract property_
stderr_: [ByteReceiveStream](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteReceiveStream "anyio.abc.ByteReceiveStream") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Process.stderr "Link to this definition")

The stream for the standard error output of the process.

_abstract property_
stdin_: [ByteSendStream](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteSendStream "anyio.abc.ByteSendStream") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Process.stdin "Link to this definition")

The stream for the standard input of the process.

_abstract property_
stdout_: [ByteReceiveStream](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteReceiveStream "anyio.abc.ByteReceiveStream") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Process.stdout "Link to this definition")

The stream for the standard output of the process.

_abstract_
terminate()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Process.terminate "Link to this definition")

Terminates the process, gracefully if possible.

On Windows, this calls `TerminateProcess()`. On POSIX systems, this sends `SIGTERM` to the process. :
rtype: [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_abstract async_
wait()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.Process.wait "Link to this definition")

Wait until the process exits.

Return type:

[`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")

Returns:

the exit code of the process

## Synchronization[¶](https://anyio.readthedocs.io/en/stable/api.html#synchronization "Link to this heading")

_class_ anyio.Event[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Event "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

is\_set()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Event.is_set "Link to this definition")

Return `True` if the flag is set, `False` if not.

Return type:

[`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")

set()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Event.set "Link to this definition")

Set the flag, notifying all listeners.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

statistics()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Event.statistics "Link to this definition")

Return statistics about the current state of this event.

Return type:

[`EventStatistics`](https://anyio.readthedocs.io/en/stable/api.html#anyio.EventStatistics "anyio.EventStatistics")

_async_ wait()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Event.wait "Link to this definition")

Wait until the flag has been set.

If the flag has already been set when this method is called, it returns immediately.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_ anyio.Lock[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Lock "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

_async_ acquire()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Lock.acquire "Link to this definition")

Acquire the lock.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

acquire\_nowait()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Lock.acquire_nowait "Link to this definition")

Acquire the lock, without blocking.

Raises:

[**WouldBlock**](https://anyio.readthedocs.io/en/stable/api.html#anyio.WouldBlock "anyio.WouldBlock") – if the operation
would block

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

locked()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Lock.locked "Link to this definition")

Return True if the lock is currently held.

Return type:

[`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")

release()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Lock.release "Link to this definition")

Release the lock.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

statistics()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Lock.statistics "Link to this definition")

Return statistics about the current state of this lock. :
rtype: [`LockStatistics`](https://anyio.readthedocs.io/en/stable/api.html#anyio.LockStatistics "anyio.LockStatistics")

New in version 3.0.

_class_ anyio.Condition(
_lock\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Condition "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

_async_ acquire()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Condition.acquire "Link to this definition")

Acquire the underlying lock.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

acquire\_nowait()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Condition.acquire_nowait "Link to this definition")

Acquire the underlying lock, without blocking.

Raises:

[**WouldBlock**](https://anyio.readthedocs.io/en/stable/api.html#anyio.WouldBlock "anyio.WouldBlock") – if the operation
would block

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

locked()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Condition.locked "Link to this definition")

Return True if the lock is set.

Return type:

[`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")

notify(_n\=1_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Condition.notify "Link to this definition")

Notify exactly n listeners.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

notify\_all()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Condition.notify_all "Link to this definition")

Notify all the listeners.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

release()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Condition.release "Link to this definition")

Release the underlying lock.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

statistics()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Condition.statistics "Link to this definition")

Return statistics about the current state of this condition. :
rtype: [`ConditionStatistics`](https://anyio.readthedocs.io/en/stable/api.html#anyio.ConditionStatistics "anyio.ConditionStatistics")

New in version 3.0.

_async_ wait()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Condition.wait "Link to this definition")

Wait for a notification.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_class_ anyio.Semaphore(_initial\_value_, _\*_,
_max\_value\=None_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Semaphore "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

_async_ acquire()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Semaphore.acquire "Link to this definition")

Decrement the semaphore value, blocking if necessary.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

acquire\_nowait()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Semaphore.acquire_nowait "Link to this definition")

Acquire the underlying lock, without blocking.

Raises:

[**WouldBlock**](https://anyio.readthedocs.io/en/stable/api.html#anyio.WouldBlock "anyio.WouldBlock") – if the operation
would block

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_property_
max\_value_: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Semaphore.max_value "Link to this definition")

The maximum value of the semaphore.

release()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Semaphore.release "Link to this definition")

Increment the semaphore value.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

statistics()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Semaphore.statistics "Link to this definition")

Return statistics about the current state of this semaphore. :
rtype: [`SemaphoreStatistics`](https://anyio.readthedocs.io/en/stable/api.html#anyio.SemaphoreStatistics "anyio.SemaphoreStatistics")

New in version 3.0.

_property_
value_: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.Semaphore.value "Link to this definition")

The current value of the semaphore.

_class_ anyio.CapacityLimiter(
_total\_tokens: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

_async_
acquire()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter.acquire "Link to this definition")

Acquire a token for the current task, waiting if necessary for one to become available.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

acquire\_nowait()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter.acquire_nowait "Link to this definition")

Acquire a token for the current task without waiting for one to become available.

Raises:

[**WouldBlock**](https://anyio.readthedocs.io/en/stable/api.html#anyio.WouldBlock "anyio.WouldBlock") – if there are no
tokens available for borrowing

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_async_ acquire\_on\_behalf\_of(
_borrower_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter.acquire_on_behalf_of "Link to this definition")

Acquire a token, waiting if necessary for one to become available.

Parameters:

**borrower** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – the entity
borrowing a token

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

acquire\_on\_behalf\_of\_nowait(
_borrower_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter.acquire_on_behalf_of_nowait "Link to this definition")

Acquire a token without waiting for one to become available.

Parameters:

**borrower** ([`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")) – the entity
borrowing a token

Raises:

[**WouldBlock**](https://anyio.readthedocs.io/en/stable/api.html#anyio.WouldBlock "anyio.WouldBlock") – if there are no
tokens available for borrowing

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

_property_
available\_tokens_: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter.available_tokens "Link to this definition")

The number of tokens currently available to be borrowed

_property_
borrowed\_tokens_: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter.borrowed_tokens "Link to this definition")

The number of tokens that have currently been borrowed.

release()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter.release "Link to this definition")

Release the token held by the current task.

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.11)") – if the current
task has not borrowed a token from this limiter.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

release\_on\_behalf\_of(
_borrower_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter.release_on_behalf_of "Link to this definition")

Release the token held by the given borrower.

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.11)") – if the borrower
has not borrowed a token from this limiter.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

statistics()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter.statistics "Link to this definition")

Return statistics about the current state of this limiter. :
rtype: [`CapacityLimiterStatistics`](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiterStatistics "anyio.CapacityLimiterStatistics")

New in version 3.0.

_property_
total\_tokens_: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")_[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter.total_tokens "Link to this definition")

The total number of tokens available for borrowing.

This is a read-write property. If the total number of tokens is increased, the proportionate number of tasks waiting on
this limiter will be granted their tokens.

Changed in version 3.0: The property is now writable.

_class_ anyio.LockStatistics(_locked_, _owner_,
_tasks\_waiting_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.LockStatistics "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

Variables:

- **locked** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – flag indicating if
  this lock is locked or not

- **owner** ([_TaskInfo_](https://anyio.readthedocs.io/en/stable/api.html#anyio.TaskInfo "anyio.TaskInfo")) – task
  currently holding the lock (or `None` if the lock is not held by any task)

- **tasks\_waiting** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – number of
  tasks waiting
  on [`acquire()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.Lock.acquire "anyio.Lock.acquire")

_class_ anyio.EventStatistics(
_tasks\_waiting_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.EventStatistics "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

Variables:

**tasks\_waiting** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – number of tasks
waiting on [`wait()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.Event.wait "anyio.Event.wait")

_class_ anyio.ConditionStatistics(_tasks\_waiting_,
_lock\_statistics_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.ConditionStatistics "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

Variables:

- **tasks\_waiting** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – number of
  tasks blocked
  on [`wait()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.Condition.wait "anyio.Condition.wait")

- **lock\_statistics** ([
  _LockStatistics_](https://anyio.readthedocs.io/en/stable/api.html#anyio.LockStatistics "anyio.LockStatistics")) –
  statistics of the underlying [`Lock`](https://anyio.readthedocs.io/en/stable/api.html#anyio.Lock "anyio.Lock")

_class_ anyio.CapacityLimiterStatistics(_borrowed\_tokens_, _total\_tokens_, _borrowers_,
_tasks\_waiting_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiterStatistics "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

Variables:

- **borrowed\_tokens** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – number of
  tokens currently borrowed by tasks

- **total\_tokens** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – total
  number of available tokens

- **borrowers** ([_tuple_](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.11)")) – tasks or other
  objects currently holding tokens borrowed from this limiter

- **tasks\_waiting** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – number of
  tasks waiting
  on [`acquire()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter.acquire "anyio.CapacityLimiter.acquire")
  or [`acquire_on_behalf_of()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.CapacityLimiter.acquire_on_behalf_of "anyio.CapacityLimiter.acquire_on_behalf_of")

_class_ anyio.SemaphoreStatistics(
_tasks\_waiting_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.SemaphoreStatistics "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

Variables:

**tasks\_waiting** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – number of tasks
waiting
on [`acquire()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.Semaphore.acquire "anyio.Semaphore.acquire")

## Operating system signals[¶](https://anyio.readthedocs.io/en/stable/api.html#operating-system-signals "Link to this heading")

anyio.open\_signal\_receiver(
_\*signals_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.open_signal_receiver "Link to this definition")

Start receiving operating system signals.

Parameters:

**signals** ([`Signals`](https://docs.python.org/3/library/signal.html#signal.Signals "(in Python v3.11)")) – signals to
receive (e.g. `signal.SIGINT`)

Return type:

[`ContextManager`](https://docs.python.org/3/library/typing.html#typing.ContextManager "(in Python v3.11)")\[[`AsyncIterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "(in Python v3.11)")\[[`Signals`](https://docs.python.org/3/library/signal.html#signal.Signals "(in Python v3.11)")\]\]

Returns:

an asynchronous context manager for an asynchronous iterator which yields signal numbers

Warning

Windows does not support signals natively so it is best to avoid relying on this in cross-platform applications.

Warning

On asyncio, this permanently replaces any previous signal handler for the given signals, as set
via [`add_signal_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_signal_handler "(in Python v3.11)").

## Low level operations[¶](https://anyio.readthedocs.io/en/stable/api.html#low-level-operations "Link to this heading")

_async_
anyio.lowlevel.checkpoint()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.lowlevel.checkpoint "Link to this definition")

Check for cancellation and allow the scheduler to switch to another task.

Equivalent to (but more efficient than):

```
await checkpoint_if_cancelled()
await cancel_shielded_checkpoint()

```

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

New in version 3.0.

_async_
anyio.lowlevel.checkpoint\_if\_cancelled()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.lowlevel.checkpoint_if_cancelled "Link to this definition")

Enter a checkpoint if the enclosing cancel scope has been cancelled.

This does not allow the scheduler to switch to a different task. :
rtype: [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

New in version 3.0.

_async_
anyio.lowlevel.cancel\_shielded\_checkpoint()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.lowlevel.cancel_shielded_checkpoint "Link to this definition")

Allow the scheduler to switch to another task but without checking for cancellation.

Equivalent to (but potentially more efficient than):

```
with CancelScope(shield=True):
    await checkpoint()

```

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

New in version 3.0.

_class_ anyio.lowlevel.RunVar(_name_,
_default\=\_NoValueSet.NO\_VALUE\_SET_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.lowlevel.RunVar "Link to this definition")

Bases: [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.11)")\[`T`\]

Like a [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "(in Python v3.11)"),
except scoped to the running event loop.

## Testing and debugging[¶](https://anyio.readthedocs.io/en/stable/api.html#testing-and-debugging "Link to this heading")

_class_ anyio.TaskInfo(_id_, _parent\_id_, _name_,
_coro_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.TaskInfo "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)")

Represents an asynchronous task.

Variables:

- **id** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – the unique identifier of
  the task

- **parent\_id** (_Optional__\[_[_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")_\]_) –
  the identifier of the parent task, if any

- **name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – the description of the
  task (if any)

- **coro** ([
  _Coroutine_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Coroutine "(in Python v3.11)")) –
  the coroutine object of the task

anyio.get\_current\_task()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.get_current_task "Link to this definition")

Return the current task.

Return type:

[`TaskInfo`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TaskInfo "anyio.TaskInfo")

Returns:

a representation of the current task

anyio.get\_running\_tasks()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.get_running_tasks "Link to this definition")

Return a list of running tasks in the current event loop.

Return type:

[`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")\[[`TaskInfo`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TaskInfo "anyio.TaskInfo")\]

Returns:

a list of task info objects

_async_
anyio.wait\_all\_tasks\_blocked()[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.wait_all_tasks_blocked "Link to this definition")

Wait until all other tasks are waiting for something.

Return type:

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)")

## Exceptions[¶](https://anyio.readthedocs.io/en/stable/api.html#exceptions "Link to this heading")

_exception_
anyio.BrokenResourceError[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.BrokenResourceError "Link to this definition")

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.11)")

Raised when trying to use a resource that has been rendered unusable due to external causes (e.g. a send stream whose
peer has disconnected).

_exception_ anyio.BusyResourceError(
_action_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.BusyResourceError "Link to this definition")

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.11)")

Raised when two tasks are trying to read from or write to the same resource concurrently.

_exception_
anyio.ClosedResourceError[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.ClosedResourceError "Link to this definition")

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.11)")

Raised when trying to use a resource that has been closed.

_exception_ anyio.DelimiterNotFound(
_max\_bytes_)[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.DelimiterNotFound "Link to this definition")

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.11)")

Raised
during [`receive_until()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.buffered.BufferedByteReceiveStream.receive_until "anyio.streams.buffered.BufferedByteReceiveStream.receive_until")
if the maximum number of bytes has been read without the delimiter being found.

_exception_
anyio.EndOfStream[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.EndOfStream "Link to this definition")

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.11)")

Raised when trying to read from a stream that has been closed from the other end.

_exception_
anyio.IncompleteRead[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.IncompleteRead "Link to this definition")

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.11)")

Raised
during [`receive_exactly()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.buffered.BufferedByteReceiveStream.receive_exactly "anyio.streams.buffered.BufferedByteReceiveStream.receive_exactly")
or [`receive_until()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.buffered.BufferedByteReceiveStream.receive_until "anyio.streams.buffered.BufferedByteReceiveStream.receive_until")
if the connection is closed before the requested amount of bytes has been read.

_exception_
anyio.TypedAttributeLookupError[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeLookupError "Link to this definition")

Bases: [`LookupError`](https://docs.python.org/3/library/exceptions.html#LookupError "(in Python v3.11)")

Raised
by [`extra()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TypedAttributeProvider.extra "anyio.TypedAttributeProvider.extra")
when the given typed attribute is not found and no default value has been given.

_exception_
anyio.WouldBlock[¶](https://anyio.readthedocs.io/en/stable/api.html#anyio.WouldBlock "Link to this definition")

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.11)")

Raised by `X_nowait` functions if `X()` would block.
