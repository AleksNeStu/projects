#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task06-02:
# Create simple linter metaclass wich can produce following checks:
#  - All attrubutes have snake-case style.
#  - All user methods do not empty docstrings.
#  - All docstrings have one space delimeter between words.
#  - Any additinal checks you would like to add.

# Example:
# ```python
# from miscripts import LinterMeta
# class Creature(object):
#     __metaclass__ = LinterMeta
#     def __init__(self, genus):
#         self.genus = genus
#     def sound(self, msg):
#         print "{0}: {1}".format(self.genus, msg)
# ...
# man = Creature('man')
# Traceback (most recent call last):
#   File "...", line 20, in <module>
#     man.sound
# AttributeError: 'sound' has no documentation sting.
# ```

# Addition info:

from EPAM.miscripts import LinterMeta

class Creature(object):
    __metaclass__ = LinterMeta
    def __init__(self, genus):
        self.genus = genus
    def sound_2016(self, msg):
        '''docstring for method (def) sound'''
        print '{0}: {1}'.format(self.genus, msg)

if __name__ == '__main__':
    man = Creature("man")