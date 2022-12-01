source /Projects/projects/.venv/bin/activate

# both
# { celery -A app worker -l info & flask run; }

# only celery
celery -A app worker -l info