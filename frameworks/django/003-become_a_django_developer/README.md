https://www.linkedin.com/learning/paths/become-a-django-developer

Become a Django Developer

Django is a popular Python web framework designed to help developers rapidly build secure, scalable web applications. Get the skills to build web applications with Django, work with data and forms, and deploy your Django applications in this fast-paced learning path.

Build dynamic apps that pass data from client to server.
Work with data by building and consuming RESTful APIs.
Deploy your applications to the cloud.

```sh
# 1) Create project
# /usr/local/bin/django-admin
django-admin startproject smartnotes .
# create dir smartnotes and file manage.py


# 2) Create apps 
django-admin startapp home  # add to settings.py
django-admin startapp notes
# settings.py
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')


# 3) Run init
python manage.py runserver
# py manage.py runserver
python manage.py migrate  # initially for apply auth start
python manage.py createsuperuser


# 4) Add and change models

# Add ORM models
python manage.py makemigrations

# It is impossible to add a non-nullable field 'updated' to notes without specifying a default. This is because the database needs something to populate existing rows.
#Please select a fix:
# 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
# 2) Quit and manually define a default value in models.py.
#Select an option: 1
#Please enter the default value as valid Python.
#The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
#Type 'exit' to exit this prompt


# Migrations for 'notes':
#  notes/migrations/0001_initial.py
#    - Create model Notes
python manage.py migrate


# 5) Shell IPython 8.8.0 -- An enhanced Interactive Python. Type '?' for help.
# 5.1)
python manage.py shell
    ...
    %history

# 5.2) 
python manage.py shell
execfile('myscript.py')

# 5.3)
python manage.py shell < myscript.py
exec(open('myscript.py').read())
```

[The Django template language](https://docs.djangoproject.com/en/4.1/ref/templates/language/)

**Finished 3.2**