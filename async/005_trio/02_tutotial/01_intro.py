import asyncio

import trio

from common.utils import timer_dc, timer_cm, w_err

# That was a lot of text, but again, you don’t need to understand everything here to use Trio – in fact, Trio goes to great lengths to make each task feel like it executes in a simple, linear way. (Just like your operating system goes to great lengths to make it feel like your single-threaded code executes in a simple linear way, even though under the covers the operating system juggles between different threads and processes in essentially the same way Trio does.) But it is useful to have a rough model in your head of how the code you write is actually executed, and – most importantly – the consequences of that for parallelism.
#
# Alternatively, if this has just whetted your appetite and you want to know more about how async/await works internally, then this blog post is a good deep dive, or check out this great walkthrough to see how to build a simple async I/O framework from the ground up.

# Trio is the Python I/O library I always wanted; I find it makes building I/O-oriented programs easier, less error-prone, and just plain more fun


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


with w_err({TypeError: 'TypeError("unsupported operand type(s) for +: \'coroutine\' and \'int\'")'}):
    async_double(3) + 1

r4 = asyncio.run(async_double(3)) + 1
print(r4)
