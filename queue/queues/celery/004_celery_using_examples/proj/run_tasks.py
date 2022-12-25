# django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
# django.setup()
from celery.result import AsyncResult, GroupResult

from tasks.tasks01 import add, produce_hot_repo_report_task_v1, produce_hot_repo_report_task_v2


# Ex1
print('EXAMPLE RESULT')
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



# Recursive function to get all child tasks for a given parent task
def get_all_child_tasks(parent_task_result):
    """Tree structure of tasks in Celery, where each task may have multiple child tasks,
    you can use recursive functions to traverse the tree and get all the child tasks for a given
    parent task.
    This recursive function will return a list of all the child tasks for the given parent task, including
    any grandchild tasks and so on. You can then use the AsyncResult objects in the list to get the status, result, or other information about the tasks.
    """
    # Get the list of child tasks
    # if isinstance(parent_task_result, (AsyncResult, GroupResult)):
    children = parent_task_result.children
    if children:
        all_tasks = []
        # Recursively get the child tasks for each child task
        for child in children:
            all_tasks.extend(get_all_child_tasks(child))
        # Add the current child tasks to the list
        all_tasks.extend(children)
        return all_tasks
    else:
        return []


def wait_task(task):
    from celery.result import AsyncResult
    import time
    task_obj = AsyncResult(task) if isinstance(task, str) else task

    if task_obj.successful():
        return task_obj
    else:
        while True:
            time.sleep(1)
            if task_obj.successful():
                return task_obj


print('TASKS RESULT')


def run_tasks1v1():
    print("Run tasks 1v1")
    # Execute the parent task and get the AsyncResult object
    # django.db.utils.OperationalError: database is locked for Sqlite
    task1v1 = wait_task(produce_hot_repo_report_task_v1.delay('today'))
    # task1 = produce_hot_repo_report_task_v1.delay('today')


    # Wait for the parent task and all its child tasks to complete, and get the final result
    # task1_res = task1.get()

    # Get all child tasks for the parent task
    all_tasks1v1 = get_all_child_tasks(task1v1)
    # task1_res = task1.get()
    # all_tasks = get_all_children_tasks(task1)
    # tasks1v1_t = tasks1v1.get(timeout=5)
    print(f'Res tasks 1v1: {all_tasks1v1}')
    # all_children_tasks = get_all_children_tasks(task1)
    # tasks1v1.wait(10)
    tasks1v1_res = 1
    # from celery.result import GroupResult
    # saved_result = GroupResult.restore(task1.id)

# TODO: Fix get results
def run_tasks1v2():
    # It's important to note that the get and join methods will block the current thread of execution until the tasks are completed. If you want to execute tasks asynchronously and wait for their results without blocking the current thread, you can use the AsyncResult.wait method, which waits for a task to complete but does not block the current thread.
    print("Run tasks 1v2")
    tasks1v2 = wait_task(produce_hot_repo_report_task_v2.delay('today'))
    all_tasks1v2 = get_all_child_tasks(tasks1v2)
    print(f'Res tasks 1v2: {all_tasks1v2}')

run_tasks1v1()
#run_tasks1v2()