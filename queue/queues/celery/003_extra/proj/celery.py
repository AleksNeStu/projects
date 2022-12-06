from __future__ import absolute_import

from celery import Celery

app = Celery(
    main='proj',
     broker='pyamqp://root:rootroot@localhost/vhost',
     backend='db+sqlite:///new_app.db',
     include=['proj.tasks']
)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)


if __name__ == '__main__':
    app.start()