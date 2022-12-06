import django
# Shell
from celery_uncovered.toyex.tasks import produce_hot_repo_report_task

# from celery_uncovered.celery import debug_task

# django.setup()
# res1 = debug_task.delay()
# result1 = res1.get()


res = produce_hot_repo_report_task.delay('today')
result = res.get()

# h = 1
#
#
# #
# # fin = res.get(timeout=5)
# # assert res.ready() is True
#
# h = 1

# repr = res.__dict__
#
# # to get res needs backend configured
# assert res.ready() is True
#
# #  can wait for the result to complete, but this is rarely used since it turns the asynchronous call into a synchronous one:
# res_val = res.get(timeout=1)



# Celerybeat
# celery -A celery_uncovered beat -l info
