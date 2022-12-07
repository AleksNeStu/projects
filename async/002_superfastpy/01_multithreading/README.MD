# I) URLS
[URL1](https://usrl1.com/) - URL1 desc\
[URL2](https://usrl2.com/) - URL2 desc


# II) Description
1) Desc1
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

Executing function calls concurrently.
Executing object methods concurrently.

A Python thread is an object representation of a native thread provided by the underlying operating system.

**Concurrent:** Code that can be executed out of order.
**Parallel:** Capability to execute code simultaneously.

Each process is in fact one instance of the Python interpreter that executes Python instructions (Python byte-code), which is a slightly lower level than the code you type into your Python program.

**Thread vs Process**
Process: The operating system’s spawned and controlled entity that encapsulates an executing application. A process has two main functions. The first is to act as the resource holder for the application, and the second is to execute the instructions of the application.

A process will have at least one thread, called the main thread. Any additional threads that we create within the process will belong to that process.

The Python process will terminate once all (non background threads) are terminated.

Process: An instance of the Python interpreter has at least one thread called the MainThread.
Thread: A thread of execution within a Python process, such as the MainThread or a new thread.

The threading.Thread instance then provides a Python-based reference to this underlying native thread.

**Life-Cycle of a Thread**
creating and starting a thread.
run and start.
blocked and terminated


**life-cycle:**
1) New Thread.
2) Running Thread.
    1) Blocked Thread (optional) or execute code.
       block in many ways, such as reading or writing from a file or a socket or by waiting on a concurrency primitive such as a semaphore or a lock. After blocking, the thread will run again.
3) Terminated Thread or raising an error or exception.

2) Desc2


# III) Usage
1) Case1
2) Case2

# IV) Pros
1) Good1
2) Good2

# V) Cons
1) Bad1
2) Bad2

# VI) Compare
1) Diff1
2) Diff2
