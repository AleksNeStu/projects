# Trio has one more trick up its sleeve, that makes async functions more powerful than regular functions:

import trio


async def child1():
    print("  child1: started! sleeping now...")
    await trio.sleep(1)
    print("  child1: exiting!")


async def child2():
    print("  child2: started! sleeping now...")
    await trio.sleep(1)
    print("  child2: exiting!")


async def parent():
    # There are only 4 lines of code that really do anything here. On line 17, we use trio.open_nursery() to get a
    # “nursery” object, and then inside the async with block we call nursery.start_soon twice, on lines 19 and 22.
    # There are actually two ways to call an async function: the first one is the one we already saw, using await
    # async_fn(); the new one is nursery.start_soon(async_fn): it asks Trio to start running this async function,
    # but then returns immediately without waiting for the function to finish. So after our two calls to
    # nursery.start_soon, child1 and child2 are now running in the background.
    print("parent: started!")
    async with trio.open_nursery() as nursery:
        print("parent: spawning child1...")
        nursery.start_soon(child1)

        print("parent: spawning child2...")
        nursery.start_soon(child2)

        print("parent: waiting for children to finish...")
        # -- we exit the nursery block here --
        # the commented line, we hit the end of the async with block, and the nursery’s __aexit__ function runs. What
        # this does is force parent to stop here and wait for all the children in the nursery to exit.
    print("parent: all done!")

    # One reason this is important is that if there’s a bug or other problem in one of the children, and it raises an
    # exception, then it lets us propagate that exception into the parent; in many other frameworks, exceptions like
    # this are just discarded. Trio never discards exceptions.


trio.run(parent)
# parent: started!
# parent: spawning child1...
# parent: spawning child2...
# parent: waiting for children to finish...
#   child2: started! sleeping now...
#   child1: started! sleeping now...
#     [... 1 second passes ...]
#   child1: exiting!
#   child2: exiting!
# parent: all done!


# Let’s start with this async with thing. It’s actually pretty simple. In regular Python, a statement like with
# someobj: ... instructs the interpreter to call someobj.__enter__() at the beginning of the block, and to call
# someobj.__exit__() at the end of the block. We call someobj a “context manager”. An async with does exactly the
# same thing, except that where a regular with statement calls regular methods, an async with statement calls async
# methods: at the start of the block it does await someobj.__aenter__() and at that end of the block it does await
# someobj.__aexit__(). In this case we call someobj an “async context manager”. So in short: with blocks are a
# shorthand for calling some functions, and since with async/await Python now has two kinds of functions,
# it also needs two kinds of with blocks. That’s all there is to it! If you understand async functions,
# then you understand async with.
#
# Note
#
# This example doesn’t use them, but while we’re here we might as well mention the one other piece of new syntax that
# async/await added: async for. It’s basically the same idea as async with versus with: An async for loop is just
# like a for loop, except that where a for loop does iterator.__next__() to fetch the next item, an async for does
# await async_iterator.__anext__(). Now you understand all of async/await. Basically just remember that it involves
# making sandwiches and sticking the word “async” in front of everything, and you’ll do fine.

# trio.run -> [async function] -> ... -> [async function] -> trio.whatever


# Now, if you’re familiar with programming using threads, this might look familiar – and that’s intentional. But it’s
# important to realize that there are no threads here. All of this is happening in a single thread. To remind
# ourselves of this, we use slightly different terminology: instead of spawning two “threads”, we say that we spawned
# two “tasks”. There are two differences between tasks and threads: (1) many tasks can take turns running on a single
# thread, and (2) with threads, the Python interpreter/operating system can switch which thread is running whenever
# they feel like it; with tasks, we can only switch at certain designated places we call “checkpoints”. In the next
# section, we’ll dig into what this means.
