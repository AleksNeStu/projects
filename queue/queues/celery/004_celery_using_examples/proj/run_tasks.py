# django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
# django.setup()

from tasks.tasks01 import add, produce_hot_repo_report_task


# Ex1
res = add.delay(1, 2)
print(res.status)
print(res.result)
print(res.get())

# # Ex2
# # https://docs.celeryq.dev/en/latest/userguide/calling.html#basics
# res2 = add.apply_async((2, 22), countdown=1)
# result2 = res2.get()    # this takes at least 3 seconds to return
# print(result2)


# Ex3
# linked_add = group(add.s(33, 33), add.s(99, 99))
# linked_add.link(add.s())
# result3 = linked_add()

# def is_task_done(task):
#     from celery.result import AsyncResult
#     from celery.result import allow_join_result
#     task_obj = AsyncResult(task.id)
#     with allow_join_result():
#         res = task_obj.get()
#         if res.status != "SUCCESS":
#             return False
#         else:
#             return True

print('HARD')
res5 = produce_hot_repo_report_task.delay('today')
# res5.wait(10)
result5 = res5.get()

print(result5)