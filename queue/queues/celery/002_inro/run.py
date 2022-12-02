from tasks import add

gg = 1
add.delay(4, 14)
g = 1
# The task has now been processed by the worker you started earlier. You can verify this by looking at the worker’s console output.

# [2022-12-02 16:41:59,015: INFO/MainProcess] Task tasks.add[63e550ec-5f0c-4003-a8e2-b7f1eaf481c7] received
# [2022-12-02 16:41:59,015: INFO/ForkPoolWorker-8] Task tasks.add[63e550ec-5f0c-4003-a8e2-b7f1eaf481c7] succeeded in 8.852200699038804e-05s: 22323232318


# https://docs.celeryq.dev/en/stable/reference/celery.result.html#celery.result.AsyncResult
# Calling a task returns an AsyncResult instance. This can be used to check the state of the task, wait for the task to finish, or get its return value (or if the task failed, to get the exception and traceback).

# Results are not enabled by default. In order to do remote procedure calls or keep track of task results in a database, you will need to configure Celery to use a result backend. This is described in the next section.