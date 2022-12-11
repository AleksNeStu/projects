import os

import django

# django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
# django.setup()
import tasks.tasks01

from tasks.tasks01 import add



res = add.delay(1, 2)
print(res.status)
print(res.result)
print(res.get())


# https://docs.celeryq.dev/en/latest/userguide/calling.html#basics
res = add.apply_async((2, 22), countdown=3)
result = res.get()    # this takes at least 3 seconds to return
print(result)