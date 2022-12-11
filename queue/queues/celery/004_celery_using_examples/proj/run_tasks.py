import os

import django
from celery import group

# django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
# django.setup()
import tasks.tasks01

from tasks.tasks01 import add, produce_hot_repo_report_task


# Ex1
res = add.delay(1, 2)
print(res.status)
print(res.result)
print(res.get())

# Ex2
# https://docs.celeryq.dev/en/latest/userguide/calling.html#basics
res2 = add.apply_async((2, 22), countdown=1)
result2 = res2.get()    # this takes at least 3 seconds to return
print(result2)


# Ex3
# linked_add = group(add.s(33, 33), add.s(99, 99))
# linked_add.link(add.s())
# result3 = linked_add()

res4 = produce_hot_repo_report_task('today')
print(res4)