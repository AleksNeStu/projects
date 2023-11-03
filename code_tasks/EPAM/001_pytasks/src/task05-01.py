#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task05-01:
# Create simple threaded http server like in *task02-01.py* which can be extended using class-based plug-in model for handing requests.

# Example:
# ```python
# >>> from datetime import datetime
# >>> from server import run, Handler
# >>> class Date(Handler):
# ...     __url__ = '/date'
# ...     def get_handler(self):
# ...         return datetime.now()
# ...
# >>> run()
# ```
# And at the same time:
# ```bash
# $ curl -s 'http://192.168.1.2:8080/date'
# 2015-03-10 12:24:43.492631
# ```

# Addition info:

from datetime import datetime

from EPAM.task02 import Server, Handler


class Date(Handler):
    __url__ = '/date'
    @classmethod # have a reference to a class object as the first parameter
    # @staticmethod  # can have no parameters at all
    def Get_handler2(self):
    # def Get_handler2():
        return datetime.now()

if __name__ == '__main__':
     Server()