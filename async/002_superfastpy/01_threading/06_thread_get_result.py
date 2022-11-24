# How to return a result from a Python thread

# The problem
# Suppose you have a Python thread that runs your target function.
#
# 1) Simple scenario: That target function returns a result that you want to retrieve.
# 2) A more advanced scenario: You want to retrieve the result of the target function if the thread does not time out.

# Solutions:
# 1) concurrent.futures.ThreadPoolExecutor (concurrent.futures)
# https://docs.python.org/3/library/concurrent.futures.html
# 2) multiprocessing.pool.ThreadPool
# https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.dummy
# 3) threading + Queue
# https://docs.python.org/3/library/threading.html
# https://docs.python.org/3/library/queue.html
# 4) only threading (this one)

import sys
import threading
import time


# Extend the threading.Thread class and add a result member to your new class. Make sure to take into account positional and keyword arguments in the constructor.
class ReturnValueThread(threading.Thread):
    # In the constructor, we declare a result member that will store the result returned by the target function
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result = None

    # Override the base class’s run() method: in addition to running the target function as expected (with its args and kwargs intact), it has to store the target’s result in the new member result.
    def run(self):
        if self._target is None:
            return  # could alternatively raise an exception, depends on the use case
        try:
            self.result = self._target(*self._args, **self._kwargs)
        except Exception as exc:
            print(f'{type(exc).__name__}: {exc}', file=sys.stderr)  # properly handle the exception

    # Override the base class’s join() method: with args and kwargs intact, simply join() as in the base class but also return the result.
    def join(self, *args, **kwargs):
        super().join(*args, **kwargs)
        return self.result



# Target function returns a result that you want to retrieve
def square(x):
    """returns the square of its argument instantly"""
    return x ** 2


# Result of the target function if the thread does not time out.
def think_about_square(x):
    """ returns the square of its argument after having… thought about it for a while"""
    time.sleep(x)
    return square(x)


def check_th_timeout(thread: ReturnValueThread, value, result):
    # test whether the thread finished at line 24 via thread2.is_alive()
    if thread.is_alive():
        print('Timeout in think_about_square')  # properly handle timeout
    else:
        print(f'think_about_square({value}) = {result}')

def main():
    value = 3

    # thread1 is the thread running square() (instant result, retrieved as expected).
    thread1 = ReturnValueThread(target=square, args=(value,))
    thread1.start()
    # Then when you instantiate your new thread class, intercept the result returned by join().
    result1 = thread1.join()
    print(f'square({value}) = {result1}')


    # thread2, on the other hand, runs think_about_square(), and it just so happens that it does not finish within the
    # allotted time.
    thread2 = ReturnValueThread(target=think_about_square, args=(value,))
    thread2.start()
    check_th_timeout(thread2, value, thread2.join(timeout=1))
    # check_th_timout(thread2, value, thread2.join(timeout=3))

# ReturnValueThread returns the result of the target function, our thread2 in the above example (the thread that times out) does not exit cleanly. In fact, it runs until the sleep() ends.


if __name__ == '__main__':
    main()