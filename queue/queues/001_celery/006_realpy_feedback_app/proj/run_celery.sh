source /Projects/projects/.venv/bin/activate
celery -A django_celery worker -l INFO
