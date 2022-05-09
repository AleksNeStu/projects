#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task03-04:
# Create multiprocessed function or generator `words_counter` to count occurrence of words in text files in specified path.

# Example:
# ```python
# if __name__ == "__main__":
#     exclude = ["if", "else", "on", "at"]
#     words = words_counter('/home/keda',
#                           ext=["py", "txt"],
#                           ignored=exclude,
#                           minlen=2)
#     pprint(words)
# ```
# Output:
# ```python
# {
#     "import", 33,
#     "print", 65,
#     ...
# }
# ```
# Notes:
# **NOTE:** Try to implement own words counter, link finder (do not just copy from examples above).
# **NOTE:** Try to implement tasks for multiprocessing using different aproches.

# Addition info:

import string
import collections
import itertools
import multiprocessing as mp
import operator
import glob
import sys
import functools
from pprint import pprint
import time

# Input
exclude = ['if', 'else', 'on', 'at'] # Exclude words from search for count occurrence
path = './temp/03/' # Path to text files (Must end in a symbol "/") (Сonditional/Unconditional)
extensions = ['py','txt'] # Text file extensions list
minlen = 13 # Minimum word length to search for count occurrence
files_grabbed = [] # Empty list of grabbed text files

def ms():
    # Get current time in milliseconds
    return int(round(time.time() * 1000))

def add_file_to_word_one(exclude, minlen):
    # (Refactoring) Add new argiments "ignored", "minlen" to function "file_to_word_one"
    new_function = functools.partial(file_to_word_one, exclude, minlen)
    return new_function

def file_to_word_one(exclude, minlen, file):
    # Read text file and return a sequence of [('word1',1),('word2',1),...] values without sum (used multiproccesing)
    output = []
    punctuation = string.maketrans(string.punctuation, ' ' * len(string.punctuation)) # For punctuation characters processing
    print mp.current_process().name, 'reading', file # Print the distribution of flows
    # Try to open file with error handling for get list [('word1',1),('word2',1),...]
    try:
        with open(file, 'rt') as f:
            for line in f:
                if line.lstrip().startswith('..'):  # Skip restructured text (comment lines)
                    continue
                line = line.translate(punctuation)  # Strip punctuation
                for word in line.split():
                    word = word.lower() # Convert string to lowercase
                    # Check string alphabetic characters only and not in exclude list and len >= minlen
                    if word.isalpha() and word not in exclude and len(word)>=minlen:
                        output.append((word, 1))
        return output # [('word1',1),('word2',1),...]
    except IOError as (errno, strerror):
        print "I/O error({0}): {1}".format(errno, strerror)
    except ValueError:
        print "No valid integer in line."
    except:
        print "Unexpected error:", sys.exc_info()[0]


def partitioned(values):
    # Organize the mapped values by their key.
    # Returns an unsorted sequence of tuples with a key and a sequence of values from result of "file_to_word_one"
    partitioned_data = collections.defaultdict(list)
    for key, value in values:
        partitioned_data[key].append(value)
    return partitioned_data.items()

def words_occurances(item):
    # Convert the partitioned data for a word to a tuple containing the word and the number of occurances
    word, occurances = item
    return (word, sum(occurances))

def words_counter(path,extensions, exclude=[], minlen=3):
    # Main function to count occurrence of words in text files in specified path
    cores = mp.cpu_count()  # Number of CPU cores
    pool = mp.Pool(processes=cores)  # Start the number of cores worker processes
    time1 = ms()  # Start time
    for ext in extensions:
        files_grabbed.extend(glob.glob(path+'*.'+ext)) # "Files_grabbed" - full list of grabbed text files
    print '\nWORK FLOWS TO SEARCH FOR COUNT OCCURRENCE:\n'  # Print work flows
    words_one_list = pool.map(add_file_to_word_one(exclude, minlen), files_grabbed) # [('word1',1),('word2',1),...]
    words_one_partitioned = partitioned(itertools.chain(*words_one_list)) # [('word1', [1, 1, 1]),('word2', [1, 1]),...]
    words_occuranced = pool.map(words_occurances,words_one_partitioned) # [('word1', 3),('word2', 2),...]
    words_occuranced.sort(key=operator.itemgetter(1)) # Sort like [('word2', 2),('word1', 3),...] from min to max
    words_occuranced.reverse() # Reverse [('word1', 3),('word2', 2),...] from max to min

    print '\nSEARCH PROCESSES TOOK TIME: ' + str(ms() - time1) + ' ms'

    print '\nALL WORDS BY FREQUENCY:\n' # Structured print finded values (word, count)
    longest = max(len(word) for word, count in words_occuranced) # Word with max length (used for crete indentation)
    print '%-*s %1s\n' % (longest + 1, 'WORD:', 'COUNT:')
    for word, count in words_occuranced:
        print '%-*s %1s' % (longest + 1, word, count)

if __name__ == '__main__':
    words = words_counter(path, extensions, exclude, minlen)
    pprint(words)