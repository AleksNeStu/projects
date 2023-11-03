"""Garbage collection."""

import sys


class A:
    pass

a = A()
b = a
l = [a, ]
print(sys.getrefcount(a))
# 4

del a
print(sys.getrefcount(l[0]))
# 3