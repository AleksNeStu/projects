import httpx
import trio

url = 'https://www.example.com'


async def fetch_url(url):
    async with trio.open_nursery() as nursery:
        #  the requests library does not support asynchronous context management with async with.
        # async with requests.Session() as session:
        # Clients
        # cl1 = httpx.Client() and httpx.AsyncClient()
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response


# @Timer('lol')
async def main():
    response = await fetch_url(url)
    assert response.status_code == 200
