from __future__ import absolute_import

import os

from celery import Celery

# https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html
# dotenv.load_dotenv("./app.env")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.local'

# env = dotenv.dotenv_values("../app.env")



# django.setup()
app = Celery('celery_uncovered')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

#TODO: uncoment and fix ModuleNotFoundError: No module named 'celery.task'
import celery_uncovered.tricks.celery_conf
