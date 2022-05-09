#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task03-03:
# Create multiprocessed function or generator `grep` to produce search in a file using regular expression

# Example:
# ```pythosn
#
# if __name__ == "__main__":
#     lines = grep(r"error", "/var/log/messages")
#     pprint(lines)
# ```
# Output:
# ```python
# [
#     (355, "Error message1"),
#     (534, "Error message2"),
#     ...
# ]
# ```
# Notes:
# **NOTE:** Try to implement tasks for multiprocessing using different aproches.

# Addition info:

import sys
import re
from pprint import pprint
import multiprocessing as mp
import time

# Input
file = 'task02.py' # text file for string search
txt = r'def' # string for searching in text file

# Find txt in file used (multiprocessing)
def grep(txt,file):
    cores = mp.cpu_count()  # Number of CPU cores
    pool = mp.Pool(processes=cores)  # Start the number of cores worker processes
    time1 = ms()  # Start time
    pool.apply_async(Search, args=(txt, file, ), callback=Search_collect) # Data parallelism using Pool
    pool.close()
    pool.join()
    print '\nSearch "'+txt+'" in the file "'+file+'" took time: ' + str(ms() - time1) + ' ms\n'
    return greps

# Find txt in file used (parsing txt)
def Search(txt, file):
    grep = []
    pattern = re.compile(txt)  # Compile a regular expression pattern for search
    # File open error handling python
    try:
        with open(file, 'r') as file_target:
            for num, item in enumerate(file_target):
                if pattern.search(item) is not None:
                    grep.append(((num + 1), item))  # add (line_number........txt)
        return grep
    except IOError as (errno, strerror):
        print "I/O error({0}): {1}".format(errno, strerror)
    except ValueError:
        print "No valid integer in line."
    except:
        print "Unexpected error:", sys.exc_info()[0]
    raise
    pass

# Collect finded txt afte parsing
greps = [] # empty list of greps (line_number........txt)
def Search_collect(res):
    greps.extend(res)

# Get current time in milliseconds
def ms():
    return int(round(time.time() * 1000))

if __name__ == "__main__":
    lines = grep(txt, file)
    pprint(lines)