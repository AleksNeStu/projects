async def broken_double_sleep(x):
    print("*yawn* Going to sleep")
    start_time = time.perf_counter()

    # Whoops, we forgot the 'await'!
    # RuntimeWarning: coroutine 'sleep' was never awaited
    #   trio.sleep(2 * x) # RuntimeWarning: coroutine 'sleep' was never awaited trio.sleep(2 * x)
    # RuntimeWarning: Enable tracemalloc to get the object allocation traceback
    # This is clearly broken – 0.00 seconds is not long enough to feel well rested! Yet the code acts like it succeeded – no exception was raised
    trio.sleep(2 * x) # no ok
    await trio.sleep(2 * x) # ok
    # If you’re using PyPy, you might not even get a warning at all until the next GC collection runs:

    sleep_time = time.perf_counter() - start_time
    print(f"Woke up after {sleep_time:.2f} seconds, feeling well rested!")

trio.run(broken_double_sleep, 1)


# $ python3 -m test
# *yawn* Going to sleep
# projects/tmp/test.py:13: RuntimeWarning: coroutine 'sleep' was never awaited
#   trio.sleep(2 * x) # no ok
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback
# Woke up after 0.00 seconds, feeling well rested!
# (projects-py3.12)
# # he @ he in projects/tmp on git:master x .venv [22:48:11]


# If you’re using PyPy, you might not even get a warning at all until the next GC collection runs:
# $ pypy3 -m test
# *yawn* Going to sleep
# Woke up after 0.00 seconds, feeling well rested!


# # but forcing a garbage collection gives us a warning:
import gc
gc.collect()