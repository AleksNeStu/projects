source /Projects/projects/.venv/bin/activate
#python manage.py runserver
celery -A celery_uncovered worker -l INFO
