https://github.com/dabeaz/curio
https://curio.readthedocs.io/en/latest/tutorial.html

Curio is a coroutine-based library for:
1) concurrent Python systems programming using async/await 
It provides standard programming abstractions such as
2) tasks
3) sockets
4) files
5) locks
6) queues
7) advanced features such as support for structured concurrency.

Structured concurrency is about treating multiple tasks running in different threads as a single unit of work, whereas Future is mostly useful when treating multiple tasks as individual tasks. A scope should block only once to await its subtasks' results, and it should then process exceptions centrally

It works on Unix and Windows and has zero dependencies. You'll find it to be familiar, small, fast, and fun.

**FAQ**

Q: What is the point of the Curio project?

A: Curio is async programming, reimagined as something smaller, faster, and easier to reason about. It is meant to be both educational and practical.

Q: Is Curio implemented using asyncio?

A: No. Curio is a standalone library directly created from low-level I/O primitives.

Q: Is Curio meant to be a clone of asyncio?

A: No. Although Curio provides a significant amount of overlapping functionality, the API is different. Compatibility with other libaries is not a goal.

Q: Is Curio meant to be compatible with other async libraries?

A: No. Curio is a stand-alone project that emphasizes a certain software architecture based on separation of environments. Other libraries have largely ignored this concept, preferring to simply provide variations on the existing approach found in asyncio.

Q: Can Curio interoperate with other event loops?

A: It depends on what you mean by the word "interoperate." Curio's preferred mechanism of communication with the external world is a queue. It is possible to communicate between Curio, threads, and other event loops using queues.

Q: How fast is Curio?

A: Curio's primary goal is to be an async library that is minimal and understandable. Performance is not the primary concern. That said, in rough benchmarking of a simple echo server, Curio is more than twice as fast as comparable code using coroutines in asyncio or trio. This was last measured on OS-X using Python 3.9. Keep in mind there is a lot more to overall application performance than the performance of a simple echo server so your mileage might vary. However, as a runtime environment, Curio doesn't introduce a lot of extra overhead. See the examples/benchmark directory for various testing programs.