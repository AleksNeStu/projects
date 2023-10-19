import time

import trio

from common.utils import timer_dc, timer_cm, w_err


@timer_dc
# A regular function
def regular_double(x):
    return 2 * x


regular_double(3)


# def print_double(x):
#     print(await async_double(x))   # <-- SyntaxError here


async def print_double(x):
    print(await async_double(x))


@timer_dc
# An async function
async def async_double(x):
    return 2 * x
trio.run(async_double, 3)  # returns 6# <-- OK!


@timer_dc
async def double_sleep(x):
    await trio.sleep(2 * x)


with timer_cm():
    trio.run(double_sleep, 1)  # does nothing for 6 seconds then returns
# trio.run -> [async function] -> ... -> [async function] -> trio.whatever

# Sync func `regular_double` elapsed time: 0.000002 s
# Async func `async_double` elapsed time: 0.000002 s
# Async func `double_sleep` elapsed time: 6.005770 s
# Context manager operation elapsed time: 6.006345 s


