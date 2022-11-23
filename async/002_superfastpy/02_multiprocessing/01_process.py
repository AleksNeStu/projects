# example of a parallel for loop with the Process class
from multiprocessing import Process
import settings
from codetiming import Timer
t = Timer(text=f"{__file__}: {{:.6f}}")


# execute a task
def task(value):
    # add your work here...
    # ...
    # all done
    res = (f' [done {value}] ')
    print(res)
    return res

# protect the entry point
if __name__ == '__main__':
    # 1.098959
    with t:
        # create all tasks
        processes = [Process(target=task, args=(i,)) for i in range(settings.COUNT_TASKS)]
        # start all processes
        for process in processes:
            process.start()
        # wait for all processes to complete
        for process in processes:
            process.join()
        # report that all tasks are completed
        print('Done')


# [+]
# 1) This approach is effective for a small number of tasks that all need to be run at once.

# [-]
# 1) It is less effective if we have many more tasks than we have CPU cores because all of the
# tasks will run at the same time and slow each other down.
# 2) It also does not allow results from tasks to be returned easily.


# We can create a new child process for each iteration of the loop.
# This can be achieved by creating a Process object and setting the target argument to the
# name of the function to execute and pass any arguments via the args argument.
# We can create all the required processes first using a list comprehension. Once created, all of
# the processes can be started at once by calling the start() method on each. Finally, we can
# wait for all the processes to finish by joining each in turn with the join() method.
