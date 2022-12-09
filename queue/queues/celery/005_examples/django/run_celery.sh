source /Projects/projects/.venv/bin/activate
#python manage.py runserver
celery -A proj worker -l INFO