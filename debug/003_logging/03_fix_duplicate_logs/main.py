# The problem
# The problem is immediately apparent when running module.py:
#
#
# 2021-06-24 00:38:02,055 |  WARNING | module.py: 7 | This is from class A
# 2021-06-24 00:38:02,055 |  WARNING | module.py:13 | This is from class B
# 2021-06-24 00:38:02,055 |  WARNING | module.py:13 | This is from class B
# 2021-06-24 00:38:02,055 |  WARNING | module.py:19 | This is from class C
# 2021-06-24 00:38:02,055 |  WARNING | module.py:19 | This is from class C
# 2021-06-24 00:38:02,055 |  WARNING | module.py:19 | This is from class C

# Instead of one log record for each of the three classes, we get one for class A as expected, but two for class B and three for class C. :confounded:

# Why does this happen?
# The logging documentation ensures us that logging.getLogger() returns the same logger instance each time this function is called:
#
# All calls to this function with a given name return the same logger instance. This means that logger instances never need to be passed between different parts of an application.
#
# So why does this happen? The answer is that although we get the same logger, each time we call our get_logger() function from logger.py we are actually attaching distinct handlers to it.

# 1) Import the same logger every time
# We can simply create the logger in logger.py and import it directly in our module, without ever having to call get_logger(). Here is how logger.py changes:

import logging
import datetime


def get_logger():
    ...
    return logger


logger = get_logger()

# We just use the same variable in each of the three classes and the problem goes away, since no unnecessary handlers are created. However, this solution is not ideal since it involves (potentially many) modifications, and furthermore we can’t be sure that in two months from now we’ll still remember that we were not supposed to call get_logger() directly.


# 2) Check if handlers are present
# The best solution is to check whether any handlers are already attached before adding them to the logger. This fix only involves changing logging.py:

import logging
import datetime


# def get_logger():
#     ...
#
#     if not logger.hasHandlers():
#         logger.addHandler(stdout_handler)
#         logger.addHandler(file_handler)
#
# return logger
