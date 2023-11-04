###LRU Cache
Problem Statement
Least Recently Used (LRU) is a common caching strategy. It defines the policy to evict elements from the cache to make room for new elements when the cache is full, meaning it discards the least recently used items first.

There are many ways to achieve fast and responsive applications. **Caching** is one approach that, when used correctly, makes things much faster while decreasing the load on computing resources. Python’s [`functools` module](https://docs.python.org/3/library/functools.html) comes with the [`@lru_cache` decorator](https://docs.python.org/3/library/functools.html#functools.lru_cache), which gives you the ability to cache the result of your functions using the **Least Recently Used (LRU) strategy**.

Staying with the newsreader example, instead of going directly to the server every time you need to download an article, you can check whether you have the content in your cache and go back to the server only if you don’t. You can use the article’s URL as the key and its content as the value.

### Caching Strategies[](https://realpython.com/lru-cache-python/#caching-strategies "Permanent link")

There’s one big problem with this cache implementation: the content of the dictionary will grow indefinitely! As the user downloads more articles, the application will keep storing them in memory, eventually causing the application to crash.

### Diving Into the Least Recently Used (LRU) Cache Strategy[](https://realpython.com/lru-cache-python/#diving-into-the-least-recently-used-lru-cache-strategy "Permanent link")

A cache implemented using the LRU strategy organizes its items in order of use. Every time you access an entry, the LRU algorithm will move it to the top of the cache. This way, the algorithm can quickly identify the entry that’s gone unused the longest by looking at the bottom of the list.


The following figure shows a hypothetical cache representation after your user requests an article from the network:

[![How are items inserted in the LRU Cache as they are accessed from the network](https://files.realpython.com/media/lru_cache_1_1.2eb80a8b24a3.png)](https://files.realpython.com/media/lru_cache_1_1.2eb80a8b24a3.png)

Notice how the cache stores the article in the most recent slot before serving it to the user. The following figure shows what happens when the user requests a second article:

[![How are items inserted in the LRU Cache as they are accessed from the network](https://files.realpython.com/media/lru_cache_2_1.8c4f225e79d0.png)](https://files.realpython.com/media/lru_cache_2_1.8c4f225e79d0.png)

The second article takes the most recent slot, pushing the first article down the list.
The LRU strategy assumes that the more recently an object has been used, the more likely it will be needed in the future, so it tries to keep that object in the cache for the longest time.
