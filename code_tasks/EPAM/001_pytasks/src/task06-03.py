#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task06-03:
# Create metaclass which can add cache with common life time (cache expires after 10 sec, e.g.) to all user methods:

# Example:
# ```python
# from miscripts import CacheMeta
# from time import sleep
# class Foo(object):
#      __metaclass__ = CacheMeta
#      def __init__(self, x):
#          self.x = x
#      def mul(self, y):
#          # There is very long processing
#          sleep(10)
#          return self.x * y
# 
# foo = Foo(100)
# # First calculatin
# foo.mul(10)  # Tooks 10 sec to get result.
# 1000
# # Second call with the same values reutrn result from cache.
# foo.mul(10)  # Returns result immidiatelly.
# # Third call after 15 sec tooks again about 10 sec.
# foo.mul(10)  # Tooks 10 sec to get result again. Cache expired.
# 1000
# ```

# Addition info:

from time import sleep

from EPAM.miscripts import CacheMeta


class Foo(object):
     __metaclass__ = CacheMeta
     def __init__(self, x):
         self.x = x
     def mul(self, y):
         # There is very long processing
         sleep(10)
         return self.x * y

if __name__ == '__main__':
    foo = Foo(100)
    # First calculatin
    foo.mul(10)  # Tooks 10 sec to get result.
    # Second call with the same values reutrn result from cache.
    foo.mul(10)  # Returns result immidiatelly.
    # Third call after 15 sec tooks again about 10 sec.
    foo.mul(10)  # Tooks 10 sec to get result again. Cache expired.