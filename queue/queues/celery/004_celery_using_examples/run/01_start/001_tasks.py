import django
# Shell
from celery_uncovered.toyex.tasks import produce_hot_repo_report_task


if __name__ == '__main__':
    django.setup()
    res = produce_hot_repo_report_task.delay('today').get(timeout=5)

    # repr = res.__dict__
    #
    # # to get res needs backend configured
    # assert res.ready() is True
    #
    # #  can wait for the result to complete, but this is rarely used since it turns the asynchronous call into a synchronous one:
    # res_val = res.get(timeout=1)



    # Celerybeat
    # celery -A celery_uncovered beat -l info
