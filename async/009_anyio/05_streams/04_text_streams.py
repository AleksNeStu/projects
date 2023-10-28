"""
Text streams wrap existing receive/send streams and encode/decode strings to bytes and vice versa.
"""


from anyio import run, create_memory_object_stream
from anyio.streams.text import TextReceiveStream, TextSendStream


async def main():
    bytes_send, bytes_receive = create_memory_object_stream(1)
    text_send = TextSendStream(bytes_send)
    await text_send.send('åäö')
    result = await bytes_receive.receive()
    print(repr(result))
    assert result == b'\xc3\xa5\xc3\xa4\xc3\xb6'  # encoded

    text_receive = TextReceiveStream(bytes_receive)
    await bytes_send.send(result)
    result = await text_receive.receive()
    print(repr(result))
    assert result == 'åäö'


async def main2():
    bytes_send, bytes_receive = create_memory_object_stream(1)
    text_send = TextSendStream(bytes_send)
    text_receive = TextReceiveStream(bytes_receive)

    await text_send.send('åäö')
    result = await text_receive.receive()
    assert result == 'åäö'  # encoded



run(main)
run(main2)