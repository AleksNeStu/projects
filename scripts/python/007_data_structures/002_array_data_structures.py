'''
Array Data Structures
    list: Mutable Dynamic Arrays
    tuple: Immutable Containers
    array.array: Basic Typed Arrays
    str: Immutable Arrays of Unicode Characters
    bytes: Immutable Arrays of Single Bytes
    bytearray: Mutable Arrays of Single Bytes
'''
# Array Data Structures


# Arrays consist of fixed-size data records that allow each element to be efficiently located based on its index
# Performance-wise, it’s very fast to look up an element contained in an array given the element’s index. A proper array implementation guarantees a constant O(1) access time for this case.


# 1) list: Mutable Dynamic Arrays

'''
Python lists can hold arbitrary elements—everything is an object in Python, including functions. Therefore, you can mix and match different kinds of data types and store them all in a single list.
This can be a powerful feature, but the downside is that supporting multiple data types at the same time means that data is generally less tightly packed. As a result, the whole structure takes up more space:
'''
arr = ["one", "two", "three"]
arr[0]
# Lists have a nice repr:
print(arr)
# Lists are mutable:
arr[1] = "hello"
del arr[1]
# Lists can hold arbitrary data types:
arr.append(23)

# 2) tuple: Immutable Containers
# Just like lists, tuples are part of the Python core language. Unlike lists, however, Python’s tuple objects are immutable. This means elements can’t be added or removed dynamically—all elements in a tuple must be defined at creation time
arr = ("one", "two", "three")
arr[0]
# Tuples have a nice repr:
arr
# Tuples are immutable:
try:
    arr[1] = "hello"
except Exception:
    pass
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

try:
    del arr[1]
except Exception:
    pass
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object doesn't support item deletion

# Tuples can hold arbitrary data types:
# (Adding elements creates a copy of the tuple)
new_arr = arr + (23,)

g = 1

# 3) array.array: Basic Typed Arrays
'''
Python’s array module provides space-efficient storage of basic C-style data types like bytes, 32-bit integers, floating-point numbers, and so on.
Arrays created with the array.array class are mutable and behave similarly to lists except for one important difference: they’re typed arrays constrained to a single data type.
Because of this constraint, array.array objects with many elements are more space efficient than lists and tuples. 
'''

# Can be useful if you need to store many elements of the same type!
import array
arr = array.array("f", (1.0, 1.5, 2.0, 2.5))
arr[1]
# Arrays have a nice repr:
arr
# Arrays are mutable:
arr[1] = 23.0
arr
del arr[1]
arr
arr.append(42.0)
arr
# Arrays are "typed":
# arr[1] = "hello"
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: must be real number, not str

# 4) str: Immutable Arrays of Unicode Characters
# Python 3.x uses str objects to store textual data as immutable sequences of Unicode characters. Practically speaking, that means a str is an immutable array of characters. Oddly enough, it’s also a recursive data structure—each character in a string is itself a str object of length 1.

# Because strings are immutable in Python, modifying a string requires creating a modified copy. The closest equivalent to a mutable string is storing individual characters inside a list:
arr = "abcd"
arr[1]
arr


# Strings are immutable:
# arr[1] = "e"
# TypeError: 'str' object does not support item assignment


# del arr[1]
# TypeError: 'str' object doesn't support item deletion


# Strings can be unpacked into a list to
# get a mutable representation:
list("abcd")
"".join(list("abcd"))


# Strings are recursive data structures:
type("abc") # "<class 'str'>"
type("abc"[0]) # "<class 'str'>"


# 5) bytes: Immutable Arrays of Single Bytes
# bytes objects are immutable sequences of single bytes, or integers in the range 0 ≤ x ≤ 255. Conceptually, bytes objects are similar to str objects, and you can also think of them as immutable arrays of bytes.

# Like strings, bytes have their own literal syntax for creating objects and are space efficient. bytes objects are immutable, but unlike strings, there’s a dedicated mutable byte array data type called bytearray that they can be unpacked into:

arr = bytes((0, 1, 2, 3))
arr[1]


# Bytes literals have their own syntax:
arr

arr2 = b"\x00\x01\x02\x03"
assert arr == arr2

# Only valid `bytes` are allowed:
# bytes((0, 300))
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ValueError: bytes must be in range(0, 256)


# Bytes are immutable:
# arr[1] = 23
# TypeError: 'bytes' object does not support item assignment


# del arr[1]
# TypeError: 'bytes' object doesn't support item deletion

# 6) bytearray: Mutable Arrays of Single Bytes
# The bytearray type is a mutable sequence of integers in the range 0 ≤ x ≤ 255. The bytearray object is closely related to the bytes object, with the main difference being that a bytearray can be modified freely—you can overwrite elements, remove existing elements, or add new ones.


# 6) bytearray: Mutable Arrays of Single Bytes
# The bytearray type is a mutable sequence of integers in the range 0 ≤ x ≤ 255. The bytearray object is closely related to the bytes object, with the main difference being that a bytearray can be modified freely—you can overwrite elements, remove existing elements, or add new ones. The bytearray object will grow and shrink accordingly.
arr_ = (0, 1, 2, 3)
arr = bytearray(arr_)
arr[1]

# The bytearray repr:
arr
# Bytearrays are mutable:
arr[1] = 23
arr

arr[1]

# Bytearrays can grow and shrink in size:
del arr[1]
arr
arr.append(42)
arr

# Bytearrays can only hold `bytes`
# (integers in the range 0 <= x <= 255)
# arr[1] = "hello"
# TypeError: 'str' object cannot be interpreted as an integer
# arr[1] = 300
# ValueError: byte must be in range(0, 256)


# Bytearrays can be converted back into bytes objects:
# (This will copy the data)
b_arr = bytes(arr)

# hen third-party packages like NumPy and pandas offer a wide range of fast array implementations for scientific computing and data science.