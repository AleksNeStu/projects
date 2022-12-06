#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task03-02:
# Create multiprocessed frunction or generator `links_finder` to find links on sites using HTML parser or regular expression

# Example:
# ```python
# if __name__ == "__main__":
#     links = links_finder(["http://www.goole.com", "http://www.github.com"])
#     pprint(links)
# ```
# Output:
# ```python
# {
#     "http://www.goole.com": ["link1", "link2", "link3"],
#     "http://www.github.com": ["link1", "link2", "link3"]
# }
# ```
# Notes:
# **NOTE:** Try to implement own words counter, link finder (do not just copy from examples above).
# **NOTE:** Try to implement tasks for multiprocessing using different aproches.

# Addition info:

import re
import urllib2
import time
from multiprocessing import Process, Pool
from pprint import pprint
from urllib2 import URLError

# Input
urls = ['http://www.goole.com', 'http://www.github.com', 'http://www.python.org'] # list of URLs
def ms(): return int(round(time.time() * 1000)) # Get current time in milliseconds

# Get all urls (parsing) from HTML (text)
def get_urls(url):
    req = urllib2.Request(url)
    time1 = ms() # start time
    try:
        html = urllib2.urlopen(req).read()  # Connect to a URL and read HTML code as text
        links = re.findall('"(https?://.*?)"', html) # v1 Get all URLs (list) from text used regular expressions
        # links = re.findall("(?P<url>https?://[^\s]+)", html)  # v2 -//-
        # links = re.findall(r'(https?://[^\s]+)', html)  # v3 -//-
        print url + ' opening and parsing took time: ' + str(ms() - time1) + ' ms'
        result = ['Source URL:', url, 'Finded URLs:', links] # result list to pretty print
        return result
    except URLError as err: # Use URLError when cannot handle a response
        if hasattr(err, 'reason'):
            print 'Failed to reach a server :('
            print 'Reason: ', err.reason
        elif hasattr(err, 'code'):
            print 'The server couldn\'t fulfill the request :('
            print 'Error code: ', err.code

# Example1 - Find links from HTML page used multiprocessing
def links_finder1(urls):
    pool = Pool(processes=len(urls))  # start len(urls) worker processes
    time1 = ms() # start time
    result = pool.map(get_urls, urls) # Data parallelism using Pool to get urls
    print "\nTotal took time: " + str(ms() - time1) + " ms\n"
    return result

# Example2 - Find links from HTML page used generator
def links_finder2(urls):
    def wrapper():
        for url in urls:
            yield get_urls(url)
    return list(wrapper())

# Example3 - Find links from HTML page used generator
def links_finder3(urls):
    # links = []
    for url in urls:
        # links.append(get_urls(url))
        print get_urls(url)
    # return links

if __name__ == '__main__':
    print '\nExample#1:\n'
    pprint(links_finder1(urls))
    print '\nExample#2:\n'
    pprint(links_finder2(urls))
    print '\nExample#3:\n'
    pprint(links_finder3(urls))