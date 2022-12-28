# 1) Via sh
# 1.1)
#  $ python manage.py shell
#  >>> from myapp.tasks import add
#  >>> add.delay(2, 2)
# <AsyncResult: 80abe5c2-0f4f-4b93-b924-2ebad70b44b7>
# >>>


# 1.2)
# $ ./manage.py shell
# ...
# >>> execfile('myscript.py')

# 1.3)
# $ ./manage.py shell < myscript.py
# python 3
# >>> exec(open('myscript.py').read())

# 2) Via py
import os

import django

# django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
import sys

import sys

print(str(sys.argv))

def is_celery_connected():
    for arg in ["site-packages/celery/__main__.py", "['manage.py', 'migrate']", "/bin/celery"]:
        if arg in str(sys.argv):
            return True
    else:
        return False


if not is_celery_connected():
    import os
    import django
    # django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
    django.setup()