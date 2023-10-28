"""
A buffered byte stream wraps an existing bytes-oriented receive stream and provides certain amenities that require
buffering, such as receiving an exact number of bytes, or receiving until the given delimiter is found.
"""
from anyio import run, create_memory_object_stream
from anyio.streams.buffered import BufferedByteReceiveStream

from common.utils import pk_ver_diff

ver4 = pk_ver_diff('anyio', exp_ver="4.0.0", eq=True, more=True)


async def main():
    send, receive = create_memory_object_stream[bytes](4) if ver4 else create_memory_object_stream(4)
    buffered = BufferedByteReceiveStream(receive)
    for part in b'hel', b'lo, ', b'wo', b'rld!':
        await send.send(part)

    result = await buffered.receive_exactly(nbytes=8)
    # await buffered.receive() - will do part by part, do nto forget await
    print(repr(result))
    assert result == b'hello, w'

    result = await buffered.receive_until(b'!', 10)
    print(repr(result))
    assert result == b'orld'


run(main)
