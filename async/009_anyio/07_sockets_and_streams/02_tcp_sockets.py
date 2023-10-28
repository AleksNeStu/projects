"""Working with TCP sockets
TCP (Transmission Control Protocol) is the most commonly used protocol on the Internet. It allows one to connect to a port on a remote host and send and receive data in a reliable manner.

To connect to a listening TCP socket somewhere, you can use connect_tcp():
"""
from anyio import connect_tcp, run


async def main():
    async with await connect_tcp('hostname', 1234) as client:
        await client.send(b'Client\n')
        response = await client.receive()
        print(response)

run(main)
"""As a convenience, you can also use connect_tcp() to establish a TLS session with the peer after connection, by passing tls=True or by passing a nonempty value for either ssl_context or tls_hostname.

To receive incoming TCP connections, you first create a TCP listener with create_tcp_listener() and call serve() on it:
"""
from anyio import create_tcp_listener, run


async def handle(client):
    async with client:
        name = await client.receive(1024)
        await client.send(b'Hello, %s\n' % name)


async def main():
    listener = await create_tcp_listener(local_port=1234)
    await listener.serve(handle)

run(main)
# See the section on TLS streams for more information.