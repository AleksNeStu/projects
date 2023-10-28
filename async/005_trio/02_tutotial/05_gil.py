"""
Trio doesn’t make your code run on multiple cores; in fact, as we saw above, it’s baked into Trio’s design that when
it has multiple tasks, they take turns, so at each moment only one of them is actively running. We’re not so much
overcoming the GIL as embracing it.
1) Excellent scalability: Trio can run 10,000+ tasks simultaneously without breaking a sweat, so long as their total
CPU demands don’t exceed what a single core can provide. (This is common in, for example, network servers that have
lots of clients connected, but only a few active at any given time.)
2) Fancy features: most threading systems are implemented in C and restricted to whatever features the operating
system provides. In Trio our logic is all in Python, which makes it possible to implement powerful and ergonomic
features like Trio’s cancellation system.
3) Code that’s easier to reason about: the await keyword means that potential task-switching points are explicitly
marked within each function. This can make Trio code dramatically easier to reason about than the equivalent program
using threads.
4) One reason this is important is that if there’s a bug or other problem in one of the children, and it raises an
exception, then it lets us propagate that exception into the parent; in many other frameworks, exceptions like this
are just discarded. Trio never discards exceptions.

 Making checkpoints explicit gives you more control over how your tasks can be interleaved – but with great power
 comes great responsibility. With threads, the runtime environment is responsible for making sure that each thread
 gets its fair share of running time. With Trio, if some task runs off and does stuff for seconds on end without
 executing a checkpoint, then… all your other tasks will just have to wait.
"""
# tasks-intro.py


import trio
import time


async def child1():
    print("  child1: started! sleeping now...")
    # await trio.sleep(1)
    time.sleep(1)
    print("  child1: exiting!")


async def child2():
    print("  child2: started! sleeping now...")
    # await trio.sleep(2)
    time.sleep(1)
    print("  child2: exiting!")


async def parent():
    print("parent: started!")
    async with trio.open_nursery() as nursery:
        print("parent: spawning child1...")
        nursery.start_soon(child1)

        print("parent: spawning child2...")
        nursery.start_soon(child2)

        print("parent: waiting for children to finish...")
        # -- we exit the nursery block here --
    print("parent: all done!")


trio.run(parent)

# Take our example from above, and replace the calls to trio.sleep() with calls to time.sleep()
# makes run lineral
