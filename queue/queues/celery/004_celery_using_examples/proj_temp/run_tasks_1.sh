source /Projects/projects/.venv/bin/activate
#python manage.py runserver
celery -A celery_uncovered beat -l info
