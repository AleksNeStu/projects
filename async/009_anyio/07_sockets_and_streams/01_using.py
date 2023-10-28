"""
Using sockets and streams¶
Networking capabilities are arguably the most important part of any asynchronous library. AnyIO contains its own high level implementation of networking on top of low level primitives offered by each of its supported backends.

Currently AnyIO offers the following networking functionality:

TCP sockets (client + server)

UNIX domain sockets (client + server)

UDP sockets

UNIX datagram sockets

More exotic forms of networking such as raw sockets and SCTP are currently not supported.

Warning Unlike the standard BSD sockets interface and most other networking libraries, AnyIO (from 2.0 onwards) signals the end of any stream by raising the EndOfStream exception instead of returning an empty bytes object.
"""