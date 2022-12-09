# app.py == app name of module
source /Projects/projects/.venv/bin/activate
celery -A tasks worker --loglevel=INFO
# celery -A app worker -l info

# In production you’ll want to run the worker in the background as a daemon. To do this you need to use the tools provided by your platform, or something like supervisord (see Daemonization for more information).

# http://supervisord.org/
# https://github.com/celery/celery/tree/master/extra/supervisord/


# https://docs.celeryq.dev/en/stable/userguide/daemonizing.html#daemonizing

# For a complete listing of the command-line options available, do:
#celery worker --help
#celery --help