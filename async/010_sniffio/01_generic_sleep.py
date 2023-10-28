import asyncio

import anyio
import trio
from sniffio import current_async_library


async def generic_sleep(seconds):
    library = current_async_library()
    print(f"Current lib is {library}")
    if library == "trio":
        import trio
        await trio.sleep(seconds)
    elif library == "asyncio":
        import asyncio
        await asyncio.sleep(seconds)
    # ... and so on ...
    else:
        raise RuntimeError(f"Unsupported library {library!r}")


# async def child_trio():
#     await trio.sleep(1)
#
# async def child_asyncio():
#     await asyncio.sleep(1)
#
# async def child_anyio():
#     await asyncio.sleep(1)

async def child():
    await generic_sleep(1)
    print("child done")


for fr in [trio, asyncio, anyio]:
    func = child() if fr is asyncio else child
    fr.run(func)
