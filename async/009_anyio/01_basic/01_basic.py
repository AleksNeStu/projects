import anyio
import sniffio
import trio


async def main():
    print('Hello')
    await anyio.sleep(1)
    print("I'm running on", sniffio.current_async_library())

# This will run the program above on the default backend (asyncio)
anyio.run(main)

# To run it on another supported backend, say Trio, you can use the backend argument
anyio.run(main, backend='trio')

# But AnyIO code is not required to be run via run(). You can just as well use the native run() function of the
# backend library:
trio.run(main)

"""
AnyIO lets you mix and match code written for AnyIO and code written for the asynchronous framework of your choice. There are a few rules to keep in mind however:

You can only use “native” libraries for the backend you’re running, so you cannot, for example, use a library written for Trio together with a library written for asyncio.

Tasks spawned by these “native” libraries on backends other than Trio are not subject to the cancellation rules enforced by AnyIO

Threads spawned outside of AnyIO cannot use from_thread.run() to call asynchronous code
"""