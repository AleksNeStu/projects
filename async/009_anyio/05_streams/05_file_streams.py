"""
File streams read from or write to files on the file system. They can be useful for substituting a file for another
source of data, or writing output to a file for logging or debugging purposes.
"""

from anyio import run
from anyio.streams.file import FileReadStream, FileWriteStream


async def main():
    path = '/tmp/testfile'
    async with await FileWriteStream.from_path(path) as stream:
        await stream.send(b'Hello, World!')

    async with await FileReadStream.from_path(path) as stream:
        async for chunk in stream:
            print(chunk.decode(), end='')

    print()


run(main)
