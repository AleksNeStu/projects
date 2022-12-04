from __future__ import absolute_import

import os

import dotenv
from celery import Celery, signals


# dotenv.load_dotenv("./app.env")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.local'

env = dotenv.dotenv_values("./app.env")



# django.setup()
app = Celery('celery_uncovered')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


#TODO: uncoment and fix ModuleNotFoundError: No module named 'celery.task'
import celery_uncovered.tricks.celery_conf
