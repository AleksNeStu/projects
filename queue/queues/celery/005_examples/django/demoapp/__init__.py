import sys

print(str(sys.argv))

if "site-packages/celery/__main__.py" and "/bin/celery" not in str(sys.argv):
    import os
    import django
    # django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
    django.setup()