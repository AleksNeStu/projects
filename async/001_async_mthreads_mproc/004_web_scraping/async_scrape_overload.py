import asyncio
import datetime

import aiohttp
import bs4
from colorama import Fore

global loop, data


async def get_html(episode_number: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {episode_number}", flush=True)

    url = f'https://talkpython.fm/{episode_number}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp.raise_for_status()

            return await resp.text()

async def get_htmls():
    for n in range(150, 160):
        await data.put((n, await get_html(n)))


def get_title(html: str, episode_number: int) -> str:
    print(Fore.CYAN + f"Getting TITLE for episode {episode_number}", flush=True)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return "MISSING"

    return header.text.strip()


async def get_titles():
    got = 0

    while got < 9:
        n, html = await data.get()
        got += 1
        title = get_title(html, n)
        print(Fore.WHITE + f"Title found: {title}", flush=True)

    print(Fore.WHITE + f"Title found: {title}", flush=True)







def main():
    t0 = datetime.datetime.now()

    global loop, data
    # DeprecationWarning: There is no current event loop, loop = asyncio.get_event_loop()
    data = asyncio.Queue()
    loop = asyncio.new_event_loop()

    tasks = asyncio.gather(loop.create_task(get_htmls()),
                           loop.create_task(get_titles()))

    loop.run_until_complete(tasks)

    dt = datetime.datetime.now() - t0
    print(f"Done in {dt.total_seconds():.2f} sec.")


if __name__ == '__main__':
    main()
