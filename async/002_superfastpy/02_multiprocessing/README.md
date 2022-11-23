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