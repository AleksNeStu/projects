"""
A stapled stream combines any mutually compatible receive and send stream together, forming a single bidirectional
stream.

It comes in two variants:

stapledByteStream (combines a ByteReceiveStream with a ByteSendStream)

StapledObjectStream (combines an ObjectReceiveStream with a compatible ObjectSendStream)
"""
from anyio.abc import ByteReceiveStream, ByteSendStream, ObjectSendStream, ObjectReceiveStream
from anyio.streams.stapled import StapledByteStream, StapledObjectStream
