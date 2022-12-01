# I) URLS
https://www.educative.io/m/implement-least-recently-used-cache
https://realpython.com/lru-cache-python/


# II) Description
### Caching
Is an optimization technique that you can use in your applications to keep recent or often-used data in memory locations that are faster or computationally cheaper to access than their source.

### LRU Cache
Problem Statement
Least Recently Used (LRU) is a common caching strategy. It defines the policy to evict elements from the cache to make room for new elements when the cache is full, meaning it discards the least recently used items first.

### Implementing a Cache Using a Python Dictionary[](https://realpython.com/lru-cache-python/#implementing-a-cache-using-a-python-dictionary "Permanent link")
You can implement a caching solution in Python using a [dictionary](https://realpython.com/python-dicts/).

# Caching in Python Using the LRU Cache Strategy – Real Python

> ## Excerpt
> Caching is an essential optimization technique. In this tutorial, you'll learn how to use Python's @lru_cache decorator to cache the results of your functions using the LRU cache strategy. This is a powerful technique you can use to leverage the power of caching in your implementations.


There are several different strategies that you can use to evict items from the cache and keep it from growing past from its maximum size. Here are five of the most popular ones, with an explanation of when each is most useful:

| Strategy | Eviction policy | Use case |
| --- | --- | --- |
| First-In/First-Out (FIFO) | Evicts the oldest of the entries | Newer entries are most likely to be reused |
| Last-In/First-Out (LIFO) | Evicts the latest of the entries | Older entries are most likely to be reused |
| Least Recently Used (LRU) | Evicts the least recently used entry | Recently used entries are most likely to be reused |
| Most Recently Used (MRU) | Evicts the most recently used entry | Least recently used entries are most likely to be reused |
| Least Frequently Used (LFU) | Evicts the least often accessed entry | Entries with a lot of hits are more likely to be reused |

LRU strategy and how to implement it using the `@lru_cache` decorator from Python’s `functools` module.



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
