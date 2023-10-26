"""
A “stream” in AnyIO is a simple interface for transporting information from one place to another. It can mean either in-process communication or sending data over a network.

AnyIO divides streams into two categories: byte streams and object streams.

Byte streams (“Streams” in Trio lingo) are objects that receive and/or send chunks of bytes. They are modelled after the limitations of the stream sockets, meaning the boundaries are not respected. In practice this means that if, for example, you call .send(b'hello ') and then .send(b'world'), the other end will receive the data chunked in any arbitrary way, like (b'hello' and b' world'), b'hello world' or (b'hel', b'lo wo', b'rld').

Object streams (“Channels” in Trio lingo), on the other hand, deal with Python objects. The most commonly used implementation of these is the memory object stream. The exact semantics of object streams vary a lot by implementation.

Many stream implementations wrap other streams. Of these, some can wrap any bytes-oriented streams, meaning ObjectStream[bytes] and ByteStream. This enables many interesting use cases.
"""
from common.utils import w_err

"""
Memory object streams are intended for implementing a producer-consumer pattern with multiple tasks. Using create_memory_object_stream(), you get a pair of object streams: one for sending, one for receiving. They essentially work like queues, but with support for closing and asynchronous iteration.

By default, memory object streams are created with a buffer size of 0. This means that send() will block until there’s another task that calls receive(). You can set the buffer size to a value of your choosing when creating the stream. It is also possible to have an unbounded buffer by passing math.inf as the buffer size but this is not recommended.

Memory object streams can be cloned by calling the clone() method. Each clone can be closed separately, but each end of the stream is only considered closed once all of its clones have been closed. For example, if you have two clones of the receive stream, the send stream will start raising BrokenResourceError only when both receive streams have been closed.

Multiple tasks can send and receive on the same memory object stream (or its clones) but each sent item is only ever delivered to a single recipient.

The receive ends of memory object streams can be iterated using the async iteration protocol. The loop exits when all clones of the send stream have been closed.
"""

from anyio import create_task_group, create_memory_object_stream, run, WouldBlock
from anyio.streams.memory import MemoryObjectReceiveStream


async def process_items(receive_stream: MemoryObjectReceiveStream[str]) -> None:
    async with receive_stream:
        async for item in receive_stream:
            print('received', item)


async def main():
    # The [str] specifies the type of the objects being passed through the
    # memory object stream. This is a bit of trick, as create_memory_object_stream
    # is actually a class masquerading as a function.
    # send_stream, receive_stream = create_memory_object_stream[str]()
    send_stream, receive_stream = create_memory_object_stream()
    async with create_task_group() as tg:
        tg.start_soon(process_items, receive_stream)
        async with send_stream:
            for num in range(10):
                await send_stream.send(f'number {num}')

                # In contrast to other AnyIO streams (but in line with Trio’s Channels), memory object streams can be closed synchronously, using either the close() method or by using the stream as a context manager:
                if num == 3:
                    with w_err({WouldBlock: None}):
                        send_stream.send_nowait(f'DONE {num} ')
                    send_stream.close()


run(main)