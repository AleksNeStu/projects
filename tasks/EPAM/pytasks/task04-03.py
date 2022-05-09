#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task04-03 (not mandatory):
# Create **very** simple [ORM] using data descriptors like in `Subtask 1` and [SQLite]3 python module to store fields in Data Base.
# After creating instances of model all fields mast be stored in SQLite DB.

# Example:
# ```python
# >>> from ormapi import Model, BirthdayField, NameField, PhoneField
# >>> class Person(Model):
#         __table__ = "persons"
# ...     name = NameField()
# ...     birthday = BirthdayField()
# ...     phone = PhoneField()
# ...
# >>> p = Person()  # New row in table *persons* are created with default values for fields.
# >>> p.name = "Aleks"  # Cell updated with new value.
# >>> # Or you can create special method to save (commit) the values to DB like bellow.
# >>> p.phone = "375 25 5443322"  # Not yet stored in DB.
# >>> p.save()  # All changes commited to DB.
# ```

# Addition info:
# [ORM]: https://en.wikipedia.org/wiki/Object-relational_mapping
# [SQLite]: https://en.wikipedia.org/wiki/SQLite

# Input

from EPAM.ormapi import Model, BirthdayField, NameField, PhoneField

class Person(Model):
    # [ORM] used data descriptors like in `Subtask 1` and [SQLite]3 python module to store fields in Data Base
    __table__ = "persons"
    name = NameField()
    birthday = BirthdayField()
    phone = PhoneField()

p = Person()  # New row in table *persons* are created with default values for fields
p.name = "Aleks"  # Cell updated with new value

# Create special method to save (commit) the values to DB like bellow
p.phone = "375 25 5443322"  # Not yet stored in DB
p.save()  # All changes commited to DB