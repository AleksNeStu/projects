import datetime
import random
import time

import colorama


def main():
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)
    data = []
    generate_data(20, data)
    process_data(20, data)

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + f"App exiting, total time: {dt.total_seconds():,.2f} sec.", flush=True)


def generate_data(num: int, data: list):
    for idx in range(1, num + 1):
        v, t = (idx*idx, datetime.datetime.now())
        data.append((v, t))

        print(colorama.Fore.YELLOW + f" -- generated item {idx, v, t}", flush=True)
        time.sleep(random.random() + .5)


def process_data(num: int, data: list):
    idx = 0
    while idx < num:
        item = data.pop(0)
        if not item:
            time.sleep(.01)
            continue

        idx += 1
        v, t = item
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
              f" -- generated item {idx, v, t}, took {dt.total_seconds():,.2f} sec.", flush=True)
        time.sleep(.5)


if __name__ == '__main__':
    main()
