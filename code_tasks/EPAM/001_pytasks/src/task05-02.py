#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task05-02:
# Create simple threaded http server like in *task02-01.py* which can be extended using decorator-based plug-in model for handing requests.

# Example:
# ```python
# >>> from datetime import datetime
# >>> from server import run, get_handler
# >>> @get_handler('/date')
# ... def date():
# ...     return datetime.now()
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

from EPAM.task02 import Get_handler, Server


@Get_handler('/date')
def Date():
    return datetime.now()

if __name__ == '__main__':
     Server()