1) Install 

https://docs.djangoproject.com/en/4.0/intro/tutorial01/
```sh
django-admin startproject nestu
```

2) django-admin is Django’s command-line utility for administrative tasks \
https://docs.djangoproject.com/en/4.0/ref/django-admin/

In addition, manage.py is automatically created in each Django project. It does the same thing as django-admin but also sets the DJANGO_SETTINGS_MODULE environment variable so that it points to your project’s settings.py file.

3) Structure \
nestu \
   &nbsp;manage.py - https://docs.djangoproject.com/en/4.0/ref/django-admin/ A command-line utility that lets you interact with this Django project in various ways. \
   &nbsp;nestu/ - Actual Python package for your project.\
   &nbsp;&nbsp;&nbsp;&nbsp;__init__.py \
   &nbsp;&nbsp;&nbsp;&nbsp;settings.py - Settings/configuration for this Django project.\
   &nbsp;&nbsp;&nbsp;&nbsp;urls.py -  The URL declarations for this Django project; a “table of contents” of your Django-powered site. \
   &nbsp;&nbsp;&nbsp;&nbsp;asgi.py - An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.\
   &nbsp;&nbsp;&nbsp;&nbsp;wsgi.py - An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.