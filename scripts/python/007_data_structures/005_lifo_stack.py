'''
Stack Implementations in Python: Summary
As you’ve seen, Python ships with several implementations for a stack data structure. All of them have slightly different characteristics as well as performance and usage trade-offs.

If you’re not looking for parallel processing support (or if you don’t want to handle locking and unlocking manually), then your choice comes down to the built-in list type or collections.deque. The difference lies in the data structure used behind the scenes and overall ease of use.

list is backed by a dynamic array, which makes it great for fast random access but requires occasional resizing when elements are added or removed.

The list over-allocates its backing storage so that not every push or pop requires resizing, and you get an amortized O(1) time complexity for these operations. But you do need to be careful to only insert and remove items using append() and pop(). Otherwise, performance slows down to O(n).

collections.deque is backed by a doubly-linked list, which optimizes appends and deletes at both ends and provides consistent O(1) performance for these operations. Not only is its performance more stable, the deque class is also easier to use because you don’t have to worry about adding or removing items from the wrong end.

In summary, collections.deque is an excellent choice for implementing a stack (LIFO queue) in Python.
'''



# Stacks (LIFOs)
# A stack is a collection of objects that supports fast Last-In/First-Out (LIFO) semantics for inserts and deletes.
# Unlike lists or arrays, stacks typically don’t allow for random access to the objects they contain. The insert and delete operations are also often called push and pop.

#  used in language parsing as well as runtime memory management, which relies on a call stack.
#  depth-first search (DFS) on a tree or graph data structure.

# 1) list: Simple, Built-In Stacks
# Python’s built-in list type makes a decent stack data structure as it supports push and pop operations in amortized O(1) time.
# There’s an important performance caveat that you should be aware of when using lists as stacks: To get the amortized O(1) performance for inserts and deletes, new items must be added to the end of the list with the append() method and removed again from the end using pop().

# For optimum performance, stacks based on Python lists should grow towards higher indexes and shrink towards lower ones.

# !!!
# Adding and removing from the front is much slower and takes O(n) time, as the existing elements must be shifted around to make room for the new element.
s = []
s.append("eat")
s.append("sleep")
s.append("code")

s


s.pop()

s.pop()

s.pop()


# s.pop()
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# IndexError: pop from empty list

# 2) collections.deque: Fast and Robust Stacks
# The deque class implements a double-ended queue that supports adding and removing elements from either end in O(1) time (non-amortized). Because deques support adding and removing elements from either end equally well, they can serve both as queues and as stacks.

# O(1) consistent performance for inserting and deleting elements
# O(n) performance for randomly accessing elements in the middle of a stack

# * standard library that has the performance characteristics of a linked-list implementation
from collections import deque
s2 = deque()
s2.append("eat")
s2.append("sleep")
s2.append("code")
#
# s

s2.pop()
s2.pop()
s2.pop()
# s2.pop()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: pop from an empty deque

# 3) queue.LifoQueue: Locking Semantics for Parallel Computing
# The LifoQueue stack implementation in the Python standard library is synchronized and provides locking semantics to support multiple concurrent producers and consumers.
import queue

# Besides LifoQueue, the queue module contains several other classes that implement multi-producer, multi-consumer queues that are useful for parallel computing.

from queue import LifoQueue
s3 = LifoQueue()
s3.put("eat")
s3.put("sleep")
s3.put("code")

s3


assert "code" == s3.get()
s3.get()
s3.get()

# s3.get_nowait()
# _queue.Empty

# s3.get()  # Blocks/waits forever...