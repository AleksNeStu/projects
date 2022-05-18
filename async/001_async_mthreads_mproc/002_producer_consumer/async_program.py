import asyncio
import datetime
import random

import colorama


def main():
    # DeprecationWarning: There is no current event loop, loop = asyncio.get_event_loop()
    loop = asyncio.new_event_loop()

    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)

    data = asyncio.Queue()

    task1 = loop.create_task(generate_data(20, data))
    task2 = loop.create_task(generate_data(20, data))
    task3 = loop.create_task(process_data(40, data))

    final_task = asyncio.gather(task1, task2, task3)
    loop.run_until_complete(final_task)

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + f"App exiting, total time: {dt.total_seconds():,.2f} sec.", flush=True)


async def generate_data(num: int, data: asyncio.Queue):
    for idx in range(1, num + 1):
        v, t = (idx*idx, datetime.datetime.now())
        await data.put((v, t))

        print(colorama.Fore.YELLOW + f" -- generated item {idx, v, t}", flush=True)
        await asyncio.sleep(random.random() + .5)


async def process_data(num: int, data: asyncio.Queue):
    idx = 0
    while idx < num:
        item = await data.get()

        idx += 1
        v, t = item
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
              f" -- generated item {idx, v, t}, took {dt.total_seconds():,.2f} sec.", flush=True)
        await asyncio.sleep(.5)


if __name__ == '__main__':
    main()
