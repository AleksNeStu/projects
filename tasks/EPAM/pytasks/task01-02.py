#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task01-02:
# Create function `reddit` for downloading popular topics from www.reddir.org using closure and generator.
# E.g. `reddit` returns function which returns generator over titles from reddit page:
# ```python
# >>> python = reddit(“http://www.reddit.com/r/python.json”)
# >>> golang = reddit(“http://www.reddit.com/r/golang.json”)
# >>> for title in python():  # here json data is fetched
# ...    print repr(title)
# u'Porting to Python 3 book is on github'
# u'An Overview of using WebSockets in Python'
# - // -
# >>> for title in golang():  # here json data is fetched
# ...     print title
# - // -
# ```

# Addition info:
# https://www.reddit.com/r/python - Python (most popular topics)
# https://www.reddit.com/r/golang - The Go Programming Language (most popular topics)

import requests   # Requests HTTP library
# import json       # JSON (JavaScript Object Notation)
import urllib2

# Input date:
url1 = 'https://www.reddit.com/r/python.json'
url2 = 'https://www.reddit.com/r/golang.json'

# Functions
def reddit(url):   # Parsing titles from JSON file from site
    req = requests.get(url, headers = {'User-agent': 'Chrome'})   # Send a GET request
    JSON = req.json()   # Returns the json-encoded content of a response <type 'dict'> - file python.json
    # JSON = json.loads(r.text)
    Children = JSON['data']['children'] # To descend lower in the hierarchy
    # title_list = []                   # Create list of titles (used append)
    # for title in Children:
    #     title_list.append(title['data']['title'])
    # return title_list
    def yielding():                     # Create list of titles (used yield)
        for title in Children:
            yield title['data']['title']
    return list(yielding())

def reddit2(url):   # Parsing titles from JSON file from site
    # Download file (JSON) from reddit.com to local store
    req = urllib2.Request(url, headers={'User-agent': 'Chrome'})
    with open('./input/'+url[-11:], 'w') as f:
        try:
            f.write(urllib2.urlopen(req).read())
            f.close()
        except ValueError as ex:
            print  ex
    # file to list
    txt = open('./input/'+url[-11:]).readlines()  # not formated list (one str)
    l = str(txt).replace(',', ':').split(': ')  # formated str
    title = [l[i + 1].replace('"', '') for i in xrange(0, len(l)) if 'title' in l[i]]  # generator of list
    return title

# Example #1 (GET JSON file (dict type) via HTTP library, parsing data used closure)
python = reddit(url1)
print '[EXAMPLE #1]'
print '[The Python programming language page on reddit.com:',len(python),'titles]'
for title in python: print title
print
golang = reddit(url2)
print '[The Go programming language page on reddit.com:', len(golang), 'titles]'
for title in golang: print title
print

# Example #2 (Download JSON file (dict type) to local dir, convert to type list, parsing data, used  generator)
python2 = reddit2(url1)
print '[EXAMPLE #2]'
print '[The Python programming language page on reddit.com:',len(python2),'titles]'
for title in python2: print title
print
golang2 = reddit2(url2)
print '[The Go programming language page on reddit.com:', len(golang2), 'titles]'
for title in golang2: print title