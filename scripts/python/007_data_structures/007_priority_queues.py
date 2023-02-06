'''
Priority Queues in Python: Summary
Python includes several priority queue implementations ready for you to use.

queue.PriorityQueue stands out from the pack with a nice object-oriented interface and a name that clearly states its intent. It should be your preferred choice.

If you’d like to avoid the locking overhead of queue.PriorityQueue, then using the heapq module directly is also a good option.
'''

# A priority queue is a container data structure that manages a set of records with totally-ordered keys to provide quick access to the record with the smallest or largest key in the set.
from bisect import insort

# 1) list: Manually Sorted Queues
# - sorted list to quickly identify and delete the smallest or largest element O(n) operation.

# -While the insertion point can be found in O(log n)
# time using bisect.insort in the standard library, this is always dominated by the slow insertion step.

# Maintaining the order by appending to the list and re-sorting also takes at least O(n log n) time.

# This means sorted lists are only suitable as priority queues when there will be few insertions:
q = []
q.append((2, "code"))
q.append((1, "eat"))
q.append((3, "sleep"))
# Remember to re-sort every time a new element is inserted,
# or use bisect.insort()
q.sort(reverse=True)

while q:
    next_item = q.pop()
    print(next_item)
# (1, 'eat')
# (2, 'code')
# bisect — Array bisection algorithm¶
# bisect.insort


# 2) heapq: List-Based Binary Heaps
# heapq: List-Based Binary Heaps
# heapq is a binary heap implementation usually backed by a plain list, and it supports insertion and extraction of the smallest element in O(log n) time.
#
# This module is a good choice for implementing priority queues in Python
import heapq
q = []
heapq.heappush(q, (2, "code"))
heapq.heappush(q, (1, "eat"))
heapq.heappush(q, (3, "sleep"))

while q:
    next_item = heapq.heappop(q)
    print(next_item)

# (1, 'eat')
# (2, 'code')
# (3, 'sleep')

# 3) queue.PriorityQueue: Beautiful Priority Queues
# queue.PriorityQueue uses heapq internally and shares the same time and space complexities.
# The difference is that PriorityQueue is synchronized and provides locking semantics to support multiple concurrent producers and consumers

#  In any case, you might prefer the class-based interface provided by PriorityQueue over the function-based interface provided by heapq:

from queue import PriorityQueue
q = PriorityQueue()
q.put((2, "code"))
q.put((1, "eat"))
q.put((3, "sleep"))

while not q.empty():
    next_item = q.get()
    print(next_item)
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')