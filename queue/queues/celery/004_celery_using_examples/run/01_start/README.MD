### Trying It Out

In order to launch and test how the task is working, first we need to start the Celery process:

        $ celery -A celery_uncovered worker -l info

Next, we need to create the `celery_uncovered/media/` directory. Then, you will be able to test its functionality either via Shell or Celerybeat:

**Shell**:

    from datetime import date
    from celery_uncovered.toyex.tasks import produce_hot_repo_report_task
    produce_hot_repo_report_task.delay('today').get(timeout=5)

**Celerybeat**:

        # Start celerybeat with the following command
        $ celery -A celery_uncovered beat -l info

You can watch the results under the `MEDIA_ROOT/` directory.
