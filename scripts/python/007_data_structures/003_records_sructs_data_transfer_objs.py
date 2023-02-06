'''
Records, Structs, and Data Objects in Python: Summary
As you’ve seen, there’s quite a number of different options for implementing records or data objects. Which type should you use for data objects in Python? Generally your decision will depend on your use case:

If you have only a few fields, then using a plain tuple object may be okay if the field order is easy to remember or field names are superfluous. For example, think of an (x, y, z) point in three-dimensional space.

If you need immutable fields, then plain tuples, collections.namedtuple, and typing.NamedTuple are all good options.

If you need to lock down field names to avoid typos, then collections.namedtuple and typing.NamedTuple are your friends.

If you want to keep things simple, then a plain dictionary object might be a good choice due to the convenient syntax that closely resembles JSON.

If you need full control over your data structure, then it’s time to write a custom class with @property setters and getters.

If you need to add behavior (methods) to the object, then you should write a custom class, either from scratch, or using the dataclass decorator, or by extending collections.namedtuple or typing.NamedTuple.

If you need to pack data tightly to serialize it to disk or to send it over the network, then it’s time to read up on struct.Struct because this is a great use case for it!

If you’re looking for a safe default choice, then my general recommendation for implementing a plain record, struct, or data object in Python would be to use collections.namedtuple in Python 2.x and its younger sibling, typing.NamedTuple in Python 3.
'''
from dataclasses import dataclass

# 1)  dict: Simple Data Objects
# Dictionaries are also often called maps or associative arrays and allow for efficient lookup, insertion, and deletion of any object associated with a given key.
car1 = {
    "color": "red",
    "mileage": 3812.4,
    "automatic": True,
}
car2 = {
    "color": "blue",
    "mileage": 40231,
    "automatic": False,
}

# Dicts have a nice repr:
car2
# {'color': 'blue', 'automatic': False, 'mileage': 40231}

# Get mileage:
car2["mileage"]
# 40231

# Dicts are mutable:
car2["mileage"] = 12
car2["windshield"] = "broken"
car2
# {'windshield': 'broken', 'color': 'blue',
#  'automatic': False, 'mileage': 12}


# No protection against wrong field names,
# or missing/extra fields:
car3 = {
    "colr": "green",
    "automatic": False,
    "windshield": "broken",
}

# 2) tuple: Immutable Groups of Objects
# Python’s tuples are a straightforward data structure for grouping arbitrary objects. Tuples are immutable—they can’t be modified once they’ve been created.
# https://docs.python.org/3/library/dis.html
#
# Performance-wise, tuples take up slightly less memory than lists in CPython, and they’re also faster to construct.
import dis
tup = (23, 'a', 'b', 'c')
tuple_des = dis.dis(compile("(23, 'a', 'b', 'c')", "", "eval"))
#       0 LOAD_CONST           4 ((23, "a", "b", "c"))
#       3 RETURN_VALUE


dis.dis(compile("[23, 'a', 'b', 'c']", "", "eval"))

'''
- Performance difference will often be negligible, and trying to squeeze extra performance out of a program by
# switching from lists to tuples will likely be the wrong approach.!!!
- A potential downside of plain tuples is that the data you store in them can only be pulled out by accessing it 
through integer indexes. You can’t give names to individual properties stored in a tuple. This can impact code readability.
- tuple is always an ad-hoc structure: it’s difficult to ensure that two tuples have the same number of fields and the same properties stored in them.
- slip-of-the-mind bugs, such as mixing up the field order.
'''
# Fields: color, mileage, automatic
car1 = ("red", 3812.4, True)
car2 = ("blue", 40231.0, False)

# Tuple instances have a nice repr:
assert car1 == ('red', 3812.4, True)
assert car2 == ('blue', 40231.0, False)


# Get mileage:
assert car2[1] == 40231.0

# Tuples are immutable:
# car2[1] = 12
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment



# No protection against missing or extra fields
# or a wrong order:
car3 = (3431.5, "green", True, "silver")

# 3) Write a Custom Class: More Work, More Control
# Classes allow you to define reusable blueprints for data objects to ensure each object provides the same set of fields.

class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic

car1 = Car("red", 3812.4, True)
car2 = Car("blue", 40231.0, False)

# Get the mileage:
car2.mileage


# Classes are mutable:
car2.mileage = 12
car2.windshield = "broken"

# String representation is not very useful
# (must add a manually written __repr__ method):
car1

# 4) dataclasses.dataclass: Python 3.7+ Data Classes
# Data classes are available in Python 3.7 and above. They provide an excellent alternative to defining your own data storage classes from scratch.

'''
The syntax for defining instance variables is shorter, since you don’t need to implement the .__init__() method.
Instances of your data class automatically get nice-looking string representation via an auto-generated .__repr__() method.
Instance variables accept type annotations, making your data class self-documenting to a degree. Keep in mind that type annotations are just hints that are not enforced without a separate type-checking tool.
'''

@dataclass
class Car:
    color: str
    mileage: float
    automatic: bool

car1 = Car("red", 3812.4, True)

# Instances have a nice repr:
car1
# Car(color='red', mileage=3812.4, automatic=True)

# Accessing fields:
car1.mileage
# 3812.4


# Fields are mutable:
car1.mileage = 12
car1.windshield = "broken"

# Type annotations are not enforced without
# a separate type checking tool like mypy:
Car("red", "NOT_A_FLOAT", 99)


# 5) collections.namedtuple: Convenient Data Objects
# namedtuple objects are immutable, just like regular tuples. This means you can’t add new fields or modify existing fields after the namedtuple instance is created.

from collections import namedtuple
from sys import getsizeof

p1 = namedtuple("Point", "x y z")(1, 2, 3)
p2 = (1, 2, 3)

print(getsizeof(p1))
print(getsizeof(p2))

from collections import namedtuple
Car = namedtuple("Car" , "color mileage automatic")
car1 = Car("red", 3812.4, True)

# Instances have a nice repr:
print(car1)
# Car(color="red", mileage=3812.4, automatic=True)

# Accessing fields:
print(car1.mileage)
# 3812.4

# Fields are immtuable:
# car1.mileage = 12
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute

#car1.windshield = "broken"
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'Car' object has no attribute 'windshield'

# 6) typing.NamedTuple: Improved Namedtuples
#  similar to namedtuple, with the main difference being an updated syntax for defining new record types and added support for type hints.
from typing import NamedTuple

class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool

car1 = Car("red", 3812.4, True)

# Instances have a nice repr:
car1


# Accessing fields:
car1.mileage


# Fields are immutable:
# car1.mileage = 12


# car1.windshield = "broken"

# Type annotations are not enforced without
# a separate type checking tool like mypy:
Car("red", "NOT_A_FLOAT", 99)

# 7) struct.Struct: Serialized C Structs
# The struct.Struct class converts between Python values and C structs serialized into Python bytes objects. For example, it can be used to handle binary data stored in files or coming in from network connections.

from struct import Struct
MyStruct = Struct("i?f")
data = MyStruct.pack(23, False, 42.0)

# All you get is a blob of data:
data


# Data blobs can be unpacked again:
MyStruct.unpack(data)

# In some cases, packing primitive data into structs may use less memory than keeping it in other data types.


# 8) types.SimpleNamespace: Fancy Attribute Access
# Here’s one more slightly obscure choice for implementing data objects in Python:
import types

car_new = types.SimpleNamespace(color="red", mileage=3812.4, automatic=True)

# The default repr:
car_new


# Instances support attribute access and are mutable:
car1.mileage = 12
car1.windshield = "broken"
del car1.automatic
car1
