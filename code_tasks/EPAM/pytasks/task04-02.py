#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task04-02:
# Create non-data descriptor like `DocAPI` which can provide class-level and instance-level documentation about methods and attributes.

# Example:
# ```python
# >>> from miscripts import DocAPI
# >>> class Foo(object):
# ...     __doc__ = API()
# ...     def __init__(self, x):
# ...         self.x = x
# ...     def meth(self, y):
# ...         """Multiplies two values self.x and y."""
# ...         return self.x * y
# ...
# >>> print Foo.__doc__
# meth : Multiplies two values self.x and y.
# >>> foo = Foo(10)
# >>> print foo.__doc__
# x : int
# meth : Multiplies two values self.x and y.

# Addition info:

import os

from EPAM.miscripts import DocAPI


class Foo(object):
    __doc__ = DocAPI() # docstrings to non-data descriptor "DocAPI"
    __path__ = os.path.realpath(__file__) # return the abspath of the current script to transfer "DocAPI"
    def __init__(self, x):
        self.x = x
    def meth(self, y):
        """Multiplies two values self.x and y."""
        return self.x * y

if __name__ == '__main__':
     print Foo.__doc__
     foo = Foo(7777)
     print foo.__doc__