# example of a parallel for loop with the ThreadPool class
from multiprocessing.pool import ThreadPool
from codetiming import Timer
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
    # 2.128846
    with t:
        # create the pool with the default number of workers
        # ThreadPool class that will create one worker for each logical
        # CPU core in the system.
        with ThreadPool() as pool:
            # issue one task for each call to the function
            for result in pool.map(task, range(1000000)):
                # handle the result
                print(result)
        # report that all tasks are completed
        print('Done')



# We can create a pool of worker threads that can be reused for many tasks.
# This can be achieved using the ThreadPool class that will create one worker for each logical
# CPU core in the system.
# The ThreadPool class can be created using the context manager interface, which ensures
# that it is closed and all workers are released once we are finished with it.
# We can call the same function many times with different arguments using the map() method
# on the ThreadPool class. Each call to the target function will be issued as a separate task.
# The example below demonstrates a parallel for-loop with the ThreadPool class.