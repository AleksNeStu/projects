#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task04-01:
# Create simple data descriptors like `BirthdayField`, `NameField`, `PhoneField` which can perform simple check of types and values.

# Example:
# ```python
# >>> from datetime import datetime
# >>> from fields import BirthdayField, NameField, PhoneField
# >>> class Person(object):
# ...     name = NameField()
# ...     birthday = BirthdayField()
# ...     phone = PhoneField()
# ...
# >>> Aleks = Person()
#
# >>> print Aleks.name
# None
# >>> Aleks.name = "Aleks Nestu"
# >>> print Aleks.name
# Aleks Nestu
# >>> Aleks.name = None
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Name must be string type
#
# >>> Aleks.birthday = datetime.strptime("1977-07-07", "%Y-%m-%d")
# >>> print Aleks.birthday
# 1984-05-09 00:00:00
# >>> Aleks.birthday = "May 05"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Birthday must be datetime type
#
# >>> Aleks.phone = "375 25 5443322"
# >>> print Aleks.phone
# 375 (25) 544-33-22
# >>> Aleks.phone = "375 (25) 5443322"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: Phone must be in format XXX XX XXXXXXX

# Addition info:
from datetime import datetime

from EPAM.fields import NameField, BirthdayField, PhoneField


class Person(object):
    name = NameField()
    birthday = BirthdayField()
    phone = PhoneField()

if __name__ == '__main__':
    Aleks = Person()

    # Manipulation (OK)
    Aleks.name
    Aleks.name = 'Aleks NeStu'
    Aleks.name
    Aleks.birthday
    Aleks.birthday = datetime.strptime('1977-07-07', '%Y-%m-%d')
    Aleks.birthday
    Aleks.phone
    Aleks.phone = '375 25 5443320'
    Aleks.phone

    # Manipulation (Error) (Need to uncomment)
    # Aleks.name = 'Aleks NeStu sd'
    # Aleks.name = None
    # Aleks.birthday = 'May 05'
    # Aleks.birthday = 'None'
    # Aleks.phone = '375 (25) 5443322'