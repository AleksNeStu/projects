"""Working with UNIX sockets
UNIX domain sockets are a form of interprocess communication on UNIX-like operating systems. They cannot be used to
connect to remote hosts and do not work on Windows.

The API for UNIX domain sockets is much like the one for TCP sockets, except that instead of host/port combinations,
you use file system paths.

This is what the client from the TCP example looks like when converted to use UNIX sockets:"""

from anyio import connect_unix, run


async def main():
    async with await connect_unix('/tmp/mysock') as client:
        await client.send(b'Client\n')
        response = await client.receive(1024)
        print(response)


run(main)
# And the listener:

from anyio import create_unix_listener, run


async def handle(client):
    async with client:
        name = await client.receive(1024)
        await client.send(b'Hello, %s\n' % name)


async def main():
    listener = await create_unix_listener('/tmp/mysock')
    await listener.serve(handle)


run(main)
"""Note The UNIX socket listener does not remove the socket it creates, so you may need to delete them manually.
Sending and receiving file descriptors
UNIX sockets can be used to pass open file descriptors (sockets and files) to another process. The receiving end can 
then use either os.fdopen() or socket.socket to get a usable file or socket object, respectively.

The following is an example where a client connects to a UNIX socket server and receives the descriptor of a file 
opened on the server, reads the contents of the file and then prints them on standard output.

Client:"""

import os

from anyio import connect_unix, run


async def main():
    async with await connect_unix('/tmp/mysock') as client:
        _, fds = await client.receive_fds(0, 1)
        with os.fdopen(fds[0]) as file:
            print(file.read())


run(main)
# Server:

from pathlib import Path

from anyio import create_unix_listener, run


async def handle1(client):
    async with client:
        with path.open('r') as file:
            await client.send_fds(b'this message is ignored', [file])


async def main():
    listener = await create_unix_listener('/tmp/mysock')
    await listener.serve(handle1)


path = Path('/tmp/examplefile')
path.write_text('Test file')
run(main)
