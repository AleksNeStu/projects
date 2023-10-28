"""
On AnyIO, streams and listeners can be layered on top of each other to provide extra functionality. But when you want
to look up information from one of the layers down below, you might have to traverse the entire chain to find what
you’re looking for, which is highly inconvenient. To address this, AnyIO has a system of typed attributes where you
can look for a specific attribute by its unique key. If a stream or listener wrapper does not have the attribute
you’re looking for, it will look it up in the wrapped instance, and that wrapper can look in its wrapped instance and
so on, until the attribute is either found or the end of the chain is reached. This also lets wrappers override
attributes from the wrapped objects when necessary.


"""

# A common use case is finding the IP address of the remote side of a TCP connection when the stream may be either
# SocketStream or TLSStream:
from anyio import connect_tcp
from anyio.abc import SocketAttribute


async def connect(host, port, tls: bool):
    stream = await connect_tcp(host, port, tls=tls)
    print('Connected to', stream.extra(SocketAttribute.remote_address))
