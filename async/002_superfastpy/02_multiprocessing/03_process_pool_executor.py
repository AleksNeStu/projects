# example of a parallel for loop with the ProcessPoolExecutor class
import concurrent.futures as ft
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
    with ft.ProcessPoolExecutor() as exe:
        t.text = f'{t.text} ex1'
        # 0.020876
        with t:
            # Example 1
            # issue some tasks and collect futures
            futures = [exe.submit(task, i) for i in range(50)]
            # process results as tasks are completed
            for future in ft.as_completed(futures):
                print(future._result)


        # Example 2
        t.text = f'{t.text} ex2'
        # 0.005878
        with t:
            # issue one task for each call to the function
            for result in exe.map(task, range(50)):
                print(result)
    # report that all tasks are completed
    print('Done')