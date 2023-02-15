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


# 3) Run
python manage.py runserver
# py manage.py runserver
python manage.py migrate
python manage.py migrate
python manage.py createsuperuser

# 4) Add
# Add ORM models
python manage.py makemigrations
# Migrations for 'notes':
#  notes/migrations/0001_initial.py
#    - Create model Notes
python manage.py migrate

# 5) Shell
python manage.py shell
    from notes.models import Notes
    note = Notes.objects.get(pk='1')
    note
    note.title
    %history
    note.text
    Notes.objects.get_all()
    Notes.objects.all()
    new_note = Notes.objects.get(title='n_2', text='txt2')
    new_note = Notes.objects.create(title='n_2', text='txt2')
    Notes.objects.all()
    Notes.objects.filter(title__startswith='My')
    Notes.objects.exclude(title__icontains='My')
    %history

```
[The Django template language](https://docs.djangoproject.com/en/4.1/ref/templates/language/)
