# I) URLS
[URL1](https://usrl1.com/) - URL1 desc\
[URL2](https://usrl2.com/) - URL2 desc


# II) Description
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



4) MVC / MTV
   https://iq.opengenus.org/model-view-controller-django/
- VC is a design pattern popularly used to create web applications that consist of 3 components namely Model, View, and Controller.
- The Model manages the data-logic, View manages the user interface and the Controller interacts with the user and controls Model and View.
- The concept of MVC could be applied differently in different frameworks.
- MVC -> MTV is used in Django:
    - Views = Templates(T)
    - Controller = framework + Views(V).

# III) Usage
1) Case1
2) Case2

# IV) Pros
1) Good1
2) Good2

# V) Cons
1) Bad1
2) Bad2

# VI) Compare
1) Diff1
2) Diff2
