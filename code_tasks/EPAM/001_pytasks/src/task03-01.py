#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task03-01:
# - Create `Fake` object which does not rise any exception for calling non-existing methods, keys, indexes.
# - Can return `Fake` object after calling non-existing method.
# - It allows any name of method, attribute, index, key, etc.
# - Don't use `try/catch`.

# Example:
# ```python
# >>> fake = Fake()
# >>> fake.non_existing_method('asdfa')
# >>> fake.attribute
# >>> fake[4]
# >>> fake['non existing key']
# >>> fake2 = fake.blablabla()
# >>> fake2.some_name()
# >>> fake2.whatever.again_whatever().and_again['aleks'][1]
# etc.
# ```
# Notes:
# **NOTE:** Try to implement tasks for multiprocessing using different aproches.

# Addition info:

class Fake(object):

    # Called when an attribute lookup has not found the attribute in the usual places
    def __getattr__(self, name):
        if name is not None and format(name) == "non_existing_method":
            def wrap(*args, **kwargs):
                print '"{0}" was called'.format(name)
                return Fake()
            return wrap
        else:
            print '"{0}" was called'.format(name)
            return Fake()

    # Called to implement evaluation of self[key]
    def __getitem__(self, name):
        print '"{0}" was called'.format(name)
        return Fake()

    # Called when the instance is “called” as a function
    def __call__(self, *args, **kwargs):
        return Fake()

if __name__ == '__main__':
    fake = Fake()
    fake.non_existing_method('asdfa')
    fake.attribute
    fake[4]
    fake['non existing key']
    fake2 = fake.blablabla()
    fake2.some_name()
    fake2.whatever.again_whatever().and_again['Aleks'][1]