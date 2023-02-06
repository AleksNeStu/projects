'''
Queues in Python: Summary
Python includes several queue implementations as part of the core language and its standard library.

list objects can be used as queues, but this is generally not recommended due to slow performance.

If you’re not looking for parallel processing support, then the implementation offered by collections.deque is an excellent default choice for implementing a FIFO queue data structure in Python. It provides the performance characteristics you’d expect from a good queue implementation and can also be used as a stack (LIFO queue).
'''
# Unlike lists or arrays, queues typically don’t allow for random access to the objects they contain.
# Queues are similar to stacks. The difference between them lies in how items are removed. With a queue, you remove the item least recently added (FIFO) but with a stack, you remove the item most recently added (LIFO).

# A short and beautiful algorithm using a queue is breadth-first search (BFS) on a tree or graph data structure.

# 1) list: Terribly Sloooow Queues
q = []
q.append("eat")
q.append("sleep")
q.append("code")

# q

# Careful: This is slow!
# Lists are quite slow for this purpose because inserting or deleting an element at the beginning requires shifting all the other elements by one, requiring O(n) time.
q.pop(0)


# 2) collections.deque: Fast and Robust Queues
from collections import deque
q = deque()
q.append("eat")
q.append("sleep")
q.append("code")

q
deque(['eat', 'sleep', 'code'])

q.popleft()
'eat'
q.popleft()
'sleep'
q.popleft()
'code'

# q.popleft()
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# IndexError: pop from an empty deque

# 3) queue.Queue: Locking Semantics for Parallel Computing
from queue import Queue
q = Queue()
q.put("eat")
q.put("sleep")
q.put("code")

# q
# <queue.Queue object at 0x1070f5b38>

q.get()
'eat'
q.get()
'sleep'
q.get()
'code'

# q.get_nowait()
# # queue.Empty
#
# q.get()  # Blocks/waits forever...

# 4) multiprocessing.Queue: Shared Job Queues
# multiprocessing.Queue is a shared job queue implementation that allows queued items to be processed in parallel by multiple concurrent workers.


from multiprocessing import Queue
q = Queue()
q.put("eat")
q.put("sleep")
q.put("code")

# q
q.get()
q.get()
q.get()
q.get()  # Blocks/waits forever...

# As a specialized queue implementation meant for sharing data between processes, multiprocessing.Queue makes it easy to
# distribute work across multiple processes in order to work around the GIL limitations.

# This type of queue can store and transfer any pickleable object across process boundaries:
# from multiprocessing import Queue
# q = Queue()
# q.put("eat")
# q.put("sleep")
# q.put("code")
#
# q
#
#
# q.get()
#
# q.get()
#
# q.get()
#

# q.get()  # Blocks/waits forever...