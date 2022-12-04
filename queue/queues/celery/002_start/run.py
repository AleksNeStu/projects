from celery.result import AsyncResult

from .tasks import add

res = add.delay(4, 14)
assert isinstance(res, AsyncResult)
repr = res.__dict__

# to get res needs backend configured
assert res.ready() is True

#  can wait for the result to complete, but this is rarely used since it turns the asynchronous call into a synchronous one:
res_val = res.get(timeout=1)

# In case the task raised an exception, get() will re-raise the exception, but you can override this by specifying the propagate argument:
#
# >>> result.get(propagate=False)
# If the task raised an exception, you can also gain access to the original traceback:
#
# >>> result.traceback

# The task has now been processed by the worker you started earlier. You can verify this by looking at the worker’s console output.

# [2022-12-02 16:41:59,015: INFO/MainProcess] Task tasks.add[63e550ec-5f0c-4003-a8e2-b7f1eaf481c7] received
# [2022-12-02 16:41:59,015: INFO/ForkPoolWorker-8] Task tasks.add[63e550ec-5f0c-4003-a8e2-b7f1eaf481c7] succeeded in 8.852200699038804e-05s: 22323232318


# https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult
# Calling a task returns an AsyncResult instance. This can be used to check the state of the task, wait for the task to finish, or get its return value (or if the task failed, to get the exception and traceback).

# Results are not enabled by default. In order to do remote procedure calls or keep track of task results in a database, you will need to configure Celery to use a result backend. This is described in the next section.


# To keep track of the tasks’ states, Celery needs to store or send the states somewhere. There are several built-in result backends to choose from: SQLAlchemy/Django ORM, MongoDB, Memcached, Redis, RPC (RabbitMQ/AMQP), and – or you can define your own.
# https://docs.celeryq.dev/en/stable/userguide/tasks.html#task-result-backends

# For larger projects, a dedicated configuration module is recommended
