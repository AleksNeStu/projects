# example of a parallel for loop with the ThreadPoolExecutor class
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures._base import Future
from typing import List

import settings
from codetiming import Timer
t = Timer(text=f"{__file__}: {{:.6f}}")


# execute a task
def task(value):
    # add your work here...
    # return a result, if needed
    res = (f' [done {value}] ')
    return res

# protect the entry point
if __name__ == '__main__':
    # create the pool with the default number of workers
    with ThreadPoolExecutor() as pool_exec:
        # Example 1
        # 22.604154
        t.start()
        # issue some tasks and collect futures
        futures: List[Future] = [pool_exec.submit(task, i) for i in range(settings.COUNT_TASKS)]
        # futures already done
        # handle results as tasks are completed
        for future in as_completed(futures):
            print(future._result)
        t.stop()


        # Example 2
        # 23.088654
        t.start()
        # issue one task for each call to the function
        for result in pool_exec.map(task, range(settings.COUNT_TASKS)):
            print(result)
        t.stop()
    # report that all tasks are completed
    print('Done')


# 1) This is the preferred approach for modern parallel for-loops.
# 2) This approach is effective for issuing one-off tasks as well as calling the same function many
# times with different arguments.
# 3) The ThreadPoolExecutor provides a modern approach for executing parallel for-loops in
# Python.


# We can create a pool of worker threads using the ThreadPoolExecutor class with a modern
# executor interface.
# This allows tasks to be issued as one-off tasks via the submit() method, returning Future
# object that provides a handle on the task. It also allows the same function to be called many
# times with different arguments via the map() method.
# The example below demonstrates parallel for-loops with the ThreadPoolExecutor class.