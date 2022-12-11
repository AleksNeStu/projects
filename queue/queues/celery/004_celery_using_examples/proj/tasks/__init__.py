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