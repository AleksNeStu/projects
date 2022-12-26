import big_o

def find_max(x):
     """Find the maximum element in a list of positive integers."""
     max_ = 0
     for el in x:
             if el > max_:
                 max_ = el
     return max_




positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
best, others = big_o.big_o(find_max, positive_int_generator, n_repeats=100)
print(best)


# 2
res2 = big_o.big_o(sorted, lambda n: big_o.datagen.integers(n, 10000, 50000))[0]
print(res2)


# 3
from collections import deque

def insert_0_queue(queue):
    queue.insert(0, 0)

def queue_generator(n):
    return deque(range(n))

print(big_o.big_o(insert_0_queue, queue_generator, n_measures=100)[0])