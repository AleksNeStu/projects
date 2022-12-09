# 1) Via sh
#  $ python manage.py shell
#  >>> from myapp.tasks import add
#  >>> add.delay(2, 2)
# <AsyncResult: 80abe5c2-0f4f-4b93-b924-2ebad70b44b7>
# >>>


# 2) Via py
import os

import django

# django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
django.setup()