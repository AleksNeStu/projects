import time

import trio


from common.utils import timer


@timer
# A regular function
def regular_double(x):
    time.sleep(2)
    return 2 * x

r0 = regular_double(55)

@timer
# An async function
async def async_double(x):
    await trio.sleep(2)
    return 2 * x

# To call an async function, you have to use the await keyword. So instead of writing regular_double(3), you write await async_double(3).
#
# You can’t use the await keyword inside the body of a regular function. If you try it, you’ll get a syntax error:

# def print_double(x):
#     print(await async_double(x))   # <-- SyntaxError here


async def print_double(x):
    print(await async_double(x))   # <-- OK!


# 1) A runner function, which is a special synchronous function that takes and calls an asynchronous function. In Trio, this is trio.run:
with timer:
    r1 = trio.run(async_double, 3)  # returns 6