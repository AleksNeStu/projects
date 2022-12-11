---
source: https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html \
created: 2022-12-06T23:34:30 (UTC +01:00) \
tags: [] \
author: 
---
# First steps with Django — Celery 5.2.7 documentation
---
## Using Celery with Django[¶](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#using-celery-with-django "Permalink to this headline")

Note

Previous versions of Celery required a separate library to work with Django, but since 3.1 this is no longer the case. Django is supported out of the box now so this document only contains a basic way to integrate Celery and Django. You’ll use the same API as non-Django users so you’re recommended to read the [First Steps with Celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#first-steps) tutorial first and come back to this tutorial. When you have a working example you can continue to the [Next Steps](https://docs.celeryq.dev/en/stable/getting-started/next-steps.html#next-steps) guide.

Note

Celery 5.0.x supports Django 1.11 LTS or newer versions. Please use Celery 4.4.x for versions older than Django 1.11.

To use Celery with your Django project you must first define an instance of the Celery library (called an “app”)

If you have a modern Django project layout like:

```
- proj/
  - manage.py
  - proj/
    - __init__.py
    - settings.py
    - urls.py

```

then the recommended way is to create a new proj/proj/celery.py module that defines the Celery instance:

file

proj/proj/celery.py

```
import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

```

Then you need to import this app in your `proj/proj/__init__.py` module. This ensures that the app is loaded when Django starts so that the `@shared_task` decorator (mentioned later) will use it:

`proj/proj/__init__.py`:

```
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)

```

Note that this example project layout is suitable for larger projects, for simple projects you may use a single contained module that defines both the app and tasks, like in the [First Steps with Celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#tut-celery) tutorial.

Let’s break down what happens in the first module, first, we set the default [`DJANGO_SETTINGS_MODULE`](https://django.readthedocs.io/en/latest/topics/settings.html#envvar-DJANGO_SETTINGS_MODULE "(in Django v4.2)") environment variable for the **celery** command-line program:

```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

```

You don’t need this line, but it saves you from always passing in the settings module to the `celery` program. It must always come before creating the app instances, as is what we do next:

This is our instance of the library, you can have many instances but there’s probably no reason for that when using Django.

We also add the Django settings module as a configuration source for Celery. This means that you don’t have to use multiple configuration files, and instead configure Celery directly from the Django settings; but you can also separate them if wanted.

```
app.config_from_object('django.conf:settings', namespace='CELERY')

```

The uppercase name-space means that all [Celery configuration options](https://docs.celeryq.dev/en/stable/userguide/configuration.html#configuration) must be specified in uppercase instead of lowercase, and start with `CELERY_`, so for example the [`task_always_eager`](https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-task_always_eager) setting becomes `CELERY_TASK_ALWAYS_EAGER`, and the [`broker_url`](https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-broker_url) setting becomes `CELERY_BROKER_URL`. This also applies to the workers settings, for instance, the [`worker_concurrency`](https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-worker_concurrency) setting becomes `CELERY_WORKER_CONCURRENCY`.

For example, a Django project’s configuration file might include:

settings.py[¶](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#id1 "Permalink to this code")

```
...

# Celery Configuration Options
CELERY_TIMEZONE = "Australia/Tasmania"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

```

You can pass the settings object directly instead, but using a string is better since then the worker doesn’t have to serialize the object. The `CELERY_` namespace is also optional, but recommended (to prevent overlap with other Django settings).

Next, a common practice for reusable apps is to define all tasks in a separate `tasks.py` module, and Celery does have a way to auto-discover these modules:

With the line above Celery will automatically discover tasks from all of your installed apps, following the `tasks.py` convention:

```
- app1/
    - tasks.py
    - models.py
- app2/
    - tasks.py
    - models.py

```

This way you don’t have to manually add the individual modules to the [`CELERY_IMPORTS`](https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-imports) setting.

Finally, the `debug_task` example is a task that dumps its own request information. This is using the new `bind=True` task option introduced in Celery 3.1 to easily refer to the current task instance.

## Extensions[¶](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#extensions "Permalink to this headline")

### `django-celery-results` - Using the Django ORM/Cache as a result backend[¶](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#django-celery-results-using-the-django-orm-cache-as-a-result-backend "Permalink to this headline")

The [django-celery-results](https://pypi.python.org/pypi/django-celery-results/) extension provides result backends using either the Django ORM, or the Django Cache framework.

To use this with your project you need to follow these steps:

1.  Install the [django-celery-results](https://pypi.python.org/pypi/django-celery-results/) library:
    
    > ```
    > $ pip install django-celery-results
    > 
    > ```
    
2.  Add `django_celery_results` to `INSTALLED_APPS` in your Django project’s `settings.py`:
    
    ```
    INSTALLED_APPS = (
        ...,
        'django_celery_results',
    )
    
    ```
    
    Note that there is no dash in the module name, only underscores.
    
3.  Create the Celery database tables by performing a database migrations:
    
    > ```
    > $ python manage.py migrate django_celery_results
    > 
    > ```
    
4.  Configure Celery to use the [django-celery-results](https://pypi.python.org/pypi/django-celery-results/) backend.
    
    > Assuming you are using Django’s `settings.py` to also configure Celery, add the following settings:
    > 
    > ```
    > CELERY_RESULT_BACKEND = 'django-db'
    > 
    > ```
    > 
    > For the cache backend you can use:
    > 
    > ```
    > CELERY_CACHE_BACKEND = 'django-cache'
    > 
    > ```
    > 
    > We can also use the cache defined in the CACHES setting in django.
    > 
    > ```
    > # celery setting.
    > CELERY_CACHE_BACKEND = 'default'
    > 
    > # django setting.
    > CACHES = {
    >     'default': {
    >         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
    >         'LOCATION': 'my_cache_table',
    >     }
    > }
    > 
    > ```
    > 
    > For additional configuration options, view the [Task result backend settings](https://docs.celeryq.dev/en/stable/userguide/configuration.html#conf-result-backend) reference.
    

## Starting the worker process[¶](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#starting-the-worker-process "Permalink to this headline")

In a production environment you’ll want to run the worker in the background as a daemon - see [Daemonization](https://docs.celeryq.dev/en/stable/userguide/daemonizing.html#daemonizing) - but for testing and development it is useful to be able to start a worker instance by using the **celery worker** manage command, much as you’d use Django’s **manage.py runserver**:

```
$ celery -A proj worker -l INFO

```

For a complete listing of the command-line options available, use the help command:

## Where to go from here[¶](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#where-to-go-from-here "Permalink to this headline")

If you want to learn more you should continue to the [Next Steps](https://docs.celeryq.dev/en/stable/getting-started/next-steps.html#next-steps) tutorial, and after that you can study the [User Guide](https://docs.celeryq.dev/en/stable/userguide/index.html#guide).
