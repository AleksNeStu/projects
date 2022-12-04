#
# For Celery's import magic to work, it is important *where* the celery commands are run.
# If you are in the same folder with *manage.py*, you should be right.

# run
source /Projects/projects/.venv/bin/activate
echo $(pwd)
cd ../../
echo $(pwd)
celery -A celery_uncovered worker -l info

# celery -A celery_uncovered beat -l info
