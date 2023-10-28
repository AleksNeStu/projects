# Working with UDP sockets
# UDP (User Datagram Protocol) is a way of sending packets over the network without features like connections,
# retries or error correction.
#
# For example, if you wanted to create a UDP “hello” service that just reads a packet and then sends a packet to the
# sender with the contents prepended with “Hello, “, you would do this:

import socket

from anyio import create_udp_socket, run


async def main():
    async with await create_udp_socket(
            family=socket.AF_INET, local_port=1234
    ) as udp:
        async for packet, (host, port) in udp:
            await udp.sendto(b'Hello, ' + packet, host, port)


run(main)
# Note If you are testing on your local machine or don’t know which family socket to use, it is a good idea to
# replace family=socket.AF_INET by local_host='localhost' in the previous example.
# If your use case involves sending lots of packets to a single destination, you can still “connect” your UDP socket
# to a specific host and port to avoid having to pass the address and port every time you send data to the peer:

from anyio import create_connected_udp_socket, run


async def main():
    async with await create_connected_udp_socket(
            remote_host='hostname', remote_port=1234) as udp:
        await udp.send(b'Hi there!\n')


run(main)
