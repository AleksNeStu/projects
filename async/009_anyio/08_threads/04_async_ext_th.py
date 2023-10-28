"""
Calling asynchronous code from an external thread
If you need to run async code from a thread that is not a worker thread spawned by the event loop, you need a
blocking portal. This needs to be obtained from within the event loop thread.

One way to do this is to start a new event loop with a portal, using start_blocking_portal (which takes mostly the
same arguments as run():
"""
from anyio.from_thread import start_blocking_portal

with start_blocking_portal(backend='trio') as portal:
    portal.call(...)

# If you already have an event loop running and wish to grant access to external threads, you can create a
# BlockingPortal directly:


from anyio import run
from anyio.from_thread import BlockingPortal


async def main():
    async with BlockingPortal() as portal:
        # ...hand off the portal to external threads...
        await portal.sleep_until_stopped()


run(main)
