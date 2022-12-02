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
)

@app.task
def add(x, y):
    return x + y

