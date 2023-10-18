import trio

"""
`producer` task that generates a sequence of numbers and puts them in a queue, and a `consumer` task that reads items
from the queue and prints them. The `producer` task uses Trio’s `sleep` function to pause for one second between each 
iteration, while the `consumer` task runs indefinitely until the queue is empty.
"""

async def producer(queue):
    for i in range(10):
        await queue.put(i)
        print(f'Produced {i}')
        await trio.sleep(1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f'Consumed {item}')

async def main():
    async with trio.open_nursery as main_nursery:
        queue = trio.Queue()
        # Trio’s `Queue` and `Channel` objects are similar to those found in other concurrent programming languages, such as the `Queue` class in Python’s `multiprocessing` module. They allow tasks to send and receive data asynchronously, which can be useful for coordinating the behavior of multiple concurrent tasks.

        await main_nursery.start(producer, queue)
        await main_nursery.start(consumer, queue)

trio.run(main)