import os

from celery import Celery

# use .setdefault() of os.environ to assure that your Django project’s settings.py module is accessible through the "DJANGO_SETTINGS_MODULE" key.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")

# create the Celery application instance and provide the name of the main module as an argument. In the context of your Django application, the main module is the Django app that contains celery.py, so you pass "django_celery".
app = Celery("django_celery")


# define the Django settings file as the configuration file for Celery and provide a namespace, "CELERY". You’ll need to preprend the namespace value, followed by an underscore (_), to every configuration variable related to Celery. You could define a different settings file, but keeping the Celery configuration in Django’s settings file allows you to stick with a single central place for configurations.
app.config_from_object("django.conf:settings", namespace="CELERY")

# your Celery application instance to automatically find all tasks in each app of your Django project. This works as long as you stick to the structure of reusable apps and define all Celery tasks for an app in a dedicated tasks.py module. You’ll create and populate this file for your django_celery app when you refactor the email sending code later.
app.autodiscover_tasks()
