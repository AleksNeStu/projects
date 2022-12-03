from celery import Celery

# The first thing you need is a Celery instance. We call this the Celery application or just app for short. As this instance is used as the entry-point for everything you want to do in Celery, like creating tasks and managing workers, it must be possible for other modules to import it.
app = Celery(
    'tasks',
    # The first argument to Celery is the name of the current module. This is only needed so that names can be automatically generated when the tasks are defined in the __main__ module.
    # broker='pyamqp://guest@localhost//',
    broker='pyamqp://root:rootroot@localhost/vhost',
    # The second argument is the broker keyword argument, specifying the URL of the message broker you want to use. Here we are using RabbitMQ (also the default option).
    #
    # See Choosing a Broker above for more choices – for RabbitMQ you can use amqp://localhost, or for Redis you can use redis://localhost.
    # https://docs.celeryq.dev/en/stable/userguide/tasks.html#task-result-backends
    backend='redis://localhost'
)

# The configuration can be set on the app directly or by using a dedicated configuration module. As an example you can configure the default serializer used for serializing task payloads by changing the task_serializer setting:
# app.conf.update(
#     task_serializer='json',
#     accept_content=['json'],  # Ignore other content
#     result_serializer='json',
#     timezone='Europe/Oslo',
#     enable_utc=True,
# )


#
# For larger projects, a dedicated configuration module is recommended. Hard coding periodic task intervals and task routing options is discouraged. It is much better to keep these in a centralized location. This is especially true for libraries, as it enables users to control how their tasks behave. A centralized configuration will also allow your SysAdmin to make simple changes in the event of system trouble.

app.config_from_object('celeryconfig')  # no overwrite
# In the above case, a module named celeryconfig.py must be available to load from the current directory or on the Python path. It could look something like this

assert app.conf['broker_url'] == 'pyamqp://root:rootroot@localhost/vhost'




@app.task
def add(x, y):
    return x + y

