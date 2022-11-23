# example of a parallel for loop with the Thread class
from threading import Thread
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
    # 63.521885
    t.start()
    # create all tasks
    threads = [Thread(target=task, args=(i,)) for i in range(settings.COUNT_TASKS)]
    # start all threads
    for thread in threads:
        thread.start()
    # wait for all threads to complete
    for thread in threads:
        thread.join()
        # TODO: get results via Queue or other solution
    # report that all tasks are completed
    print('Done')
    t.stop()


# [+]
# 1) This approach is effective for a small number of tasks that all need to be run at once.

# [-]
# 1) It is less effective if we have many more tasks than we can support concurrently because all
# of the tasks will run at the same time and could slow each other down.
# 2) It also does not allow results from tasks to be returned easily.



# We can create a new thread for each iteration of the loop.
# This can be achieved by creating a Thread object and setting the target argument to the
# name of the function to execute and pass any arguments via the args argument.
# We can create all the required threads first using a list comprehension. Once created, all of
# the threads can be started at once by calling the start() method on each. Finally, we can
# wait for all the threads to finish by joining each in turn with the join() method.
# The example below demonstrates a parallel for-loop using the Thread class.