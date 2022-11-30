# I) URLS
[URL1](https://usrl1.com/) - URL1 desc\
[URL2](https://usrl2.com/) - URL2 desc


# II) Description
1) Desc1
There are two main approaches to executing loops in parallel in Python, they are:
• Thread-based concurrency using the threading module. \
• Process-based concurrency using the multiprocessing module.


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

**Process-based Concurrency**
Process-based concurrency is ideally suited to CPU-bound tasks like calculating, parsing, encoding, and modeling.
We can also use process-based concurrency for I/O-bound tasks, but it is not well suited.
The reason is that all data shared between processes must be pickled (serialized), which can
be slow. Also, we may be limited in the maximum number of processes that can be created.
We can develop loops that execute in parallel with process-based concurrency using one of
three classes:
1. The Process class.
2. The Pool class.
3. The ProcessPoolExecutor class.

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
