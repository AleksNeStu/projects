# Working with UNIX datagram sockets
# UNIX datagram sockets are a subset of UNIX domain sockets, with the difference being that while UNIX sockets
# implement reliable communication of a continuous byte stream (similarly to TCP), UNIX datagram sockets implement
# communication of data packets (similarly to UDP).
#
# The API for UNIX datagram sockets is modeled after the one for UDP sockets, except that instead of host/port
# combinations, you use file system paths - here is the UDP “hello” service example written with UNIX datagram sockets:

from anyio import create_unix_datagram_socket, run


async def main():
    async with await create_unix_datagram_socket(
            local_path='/tmp/mysock'
    ) as unix_dg:
        async for packet, path in unix_dg:
            await unix_dg.sendto(b'Hello, ' + packet, path)


run(main)
# Note If local_path is not set, the UNIX datagram socket will be bound on an unnamed address, and will generally not
# be able to receive datagrams from other UNIX datagram sockets.
# Similarly to UDP sockets, if your case involves sending lots of packets to a single destination, you can “connect”
# your UNIX datagram socket to a specific path to avoid having to pass the path every time you send data to the peer:

from anyio import create_connected_unix_datagram_socket, run


async def main():
    async with await create_connected_unix_datagram_socket(
            remote_path='/dev/log'
    ) as unix_dg:
        await unix_dg.send(b'Hi there!\n')


run(main)
