import time

import trio
from codetiming import Timer

from common.utils import timer_d, timer_c


@timer_d
# A regular function
def regular_double(x):
    return 2 * x


regular_double(3)


# def print_double(x):
#     print(await async_double(x))   # <-- SyntaxError here


async def print_double(x):
    print(await async_double(x))


@timer_d
# An async function
async def async_double(x):
    return 2 * x
trio.run(async_double, 3)  # returns 6# <-- OK!


@timer_d
async def double_sleep(x):
    await trio.sleep(2 * x)


with timer_c():
    trio.run(double_sleep, 3)  # does nothing for 6 seconds then returns

# Sync func `regular_double` elapsed time: 0.000002 s
# Async func `async_double` elapsed time: 0.000002 s
# Async func `double_sleep` elapsed time: 6.005770 s
# Context manager operation elapsed time: 6.006345 s