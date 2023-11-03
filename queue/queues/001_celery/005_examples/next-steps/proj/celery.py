from celery import Celery

app = Celery('proj',
             broker='amqp://',
             backend='rpc://',
             include=['src.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
