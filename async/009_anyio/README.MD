https://github.com/agronholm/anyio
https://anyio.readthedocs.io/en/stable/

- Task groups (nurseries in trio terminology)
- High-level networking (TCP, UDP and UNIX sockets)
- Happy eyeballs algorithm for TCP connections (more robust than that of asyncio on Python 3.8)
- async/await style UDP sockets (unlike asyncio where you still have to use Transports and Protocols)
- A versatile API for byte streams and object streams
- Inter-task synchronization and communication (locks, conditions, events, semaphores, object streams)
- Worker threads
- Subprocesses
- Asynchronous file I/O (using worker threads)
- Signal handling