**Thread-based Concurrency**

Thread-based concurrency is suited to I/O-bound tasks, such as reading and writing files, sockets, and interacting with devices like cameras.
Thread-based concurrency is not appropriate for CPU-bound tasks, such as calculating or modeling. This is because of the Global Interpreter Lock that prevents more than one thread
from running at a time while the lock is held. The lock is not held in some cases, such as
while performing I/O.
We can develop loops that execute in parallel with thread-based concurrency using one of
three classes:
1. The Thread class.
2. The ThreadPool class.
3. The ThreadPoolExecutor class.