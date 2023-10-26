import anyio
import sniffio
from anyio import run


async def main():
    print('Hello')
    await anyio.sleep(1)
    print("I'm running on", sniffio.current_async_library())

# This will run the program above on the default backend (asyncio)
run(main)

# To run it on another supported backend, say Trio, you can use the backend argument
run(main, backend='trio')