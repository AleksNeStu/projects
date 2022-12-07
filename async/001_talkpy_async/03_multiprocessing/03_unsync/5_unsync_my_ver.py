import datetime
import math
import time

import aiohttp
import requests
import uvloop
from unsync import unsync
import asyncio

uvloop.install()


def main():
    t0 = datetime.datetime.now()

    loop = asyncio.new_event_loop()

    tasks = [
        loop.create_task(compute_some()),
        loop.create_task(compute_some()),
        loop.create_task(compute_some()),
        loop.create_task(download_some()),
        loop.create_task(download_some()),
        loop.create_task(download_some_more()),
        loop.create_task(download_some_more()),
        loop.create_task(wait_some()),
        loop.create_task(wait_some()),
        loop.create_task(wait_some()),
        loop.create_task(wait_some()),
    ]


    dt = datetime.datetime.now() - t0
    print(f"Synchronous version done in {dt.total_seconds():,.2f} seconds.")


@unsync(cpu_bound=True)
def compute_some():
    print("Computing...")
    for _ in range(1, 10_000_000):
        math.sqrt(25 ** 25 + .01)


@unsync()
def get_url_txt_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            return resp.text()



@unsync()
async def download_some():
    print("Downloading...")
    url = 'https://talkpython.fm/episodes/show/174/coming-into-python-from-another-industry-part-2'
    await text = get_url_txt_async(url)

    print(f"Downloaded (more) {len(text):,} characters.")


def download_some_more():
    print("Downloading more ...")
    url = 'https://pythonbytes.fm/episodes/show/92/will-your-python-be-compiled'
    resp = requests.get(url)
    resp.raise_for_status()

    text = resp.text

    print(f"Downloaded {len(text):,} characters.")


def wait_some():
    print("Waiting...")
    for _ in range(1, 1000):
        time.sleep(.001)


if __name__ == '__main__':
    from codetiming import Timer
    with Timer():
        main()
