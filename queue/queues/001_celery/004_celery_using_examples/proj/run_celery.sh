source /Projects/projects/.venv/bin/activate
#python manage.py runserver
python manage.py migrate
celery -A proj worker -l INFO
