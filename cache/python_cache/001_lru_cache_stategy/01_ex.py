# Expand the functionality of the @lru_cache decorator and make it expire after a specific time

import requests

cache = dict()

def get_article_from_server(url):
    print("Fetching article from server...")
    response = requests.get(url)
    return response.text

def get_article(url):
    print("Getting article...")
    if url not in cache:
        cache[url] = get_article_from_server(url)

    return cache[url]

art1 = get_article("https://realpython.com/sorting-algorithms-python/")
art2 = get_article("https://realpython.com/sorting-algorithms-python/")
assert art1 == art2