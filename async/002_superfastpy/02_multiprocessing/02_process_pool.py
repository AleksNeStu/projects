# example of a parallel for loop with the Pool class
from multiprocessing import Pool

from codetiming import Timer

import settings

t = Timer(text=f"{__file__}: {{:.6f}}")


# execute a task
def task(value):
    # add your work here...
    # ...
    # return a result, if needed
    res = (f' [done {value}] ')
    return res

# protect the entry point
if __name__ == '__main__':
    # 0.022337
    with t:
        # create the pool with the default number of workers
        with Pool() as process_pool:
            # issue one task for each call to the function
            for result in process_pool.map(task, range(settings.COUNT_TASKS)):
                # handle the result
                print(result)
        # report that all tasks are completed
        print('Done')

# [+]
# 1) This approach is very effective for executing tasks that involve calling the same function
# many times with different arguments.
# 11

# [-]


# We can create a pool of worker processes that can be reused for many tasks.
# This can be achieved using the Pool class that will create one worker for each logical CPU
# core in the system.
# The Pool class can be created using the context manager interface, which ensures that it is
# closed and all workers are released once we are finished with it.
# We can call the same function many times with different arguments using the map() method
# on the Pool class. Each call to the target function will be issued as a separate task.
# The example below demonstrates a parallel for-loop with the Pool class.