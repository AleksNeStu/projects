# 1) Dynamic typing
# 1.1) Statically typed
"3" + 5


# 1.2) Dynamic, Interpreted
def foo(a):
    if a > 0:
        print('Hi')
    else:
        print("3" + 5)
foo(2)


# 1.3) Type hints
def greeting(name: str) -> str:
    return 'Hello ' + name

# https://docs.python.org/3/library/typing.html



# 2)Automatic memory management
# https://docs.python.org/3/c-api/memory.html
# https://realpython.com/python-memory-management/

def foo(names):
    for name in names:
        print(name)

foo(["Eric", "Ernie", "Bert"])
foo(["Guthtrie", "Eddie", "Al"])


# 3) Complete introspection

# 3.1) type
# Python program showing
# a use of type function

import math

# print type of math
print(type(math))

# print type of 1
print(type(1))

# print type of "1"
print(type("1"))

# print type of rk
rk =[1, 2, 3, 4, 5, "radha"]

print(type(rk))
print(type(rk[1]))
print(type(rk[5]))


# 3.2) dir
# Python program showing
# a use of dir() function

import math
rk =[1, 2, 3, 4, 5]

# print methods and attributes of rk
print(dir(rk))
rk =(1, 2, 3, 4, 5)

# print methods and attributes of rk
print(dir(rk))
rk ={1, 2, 3, 4, 5}

print(dir(rk))
print(dir(math))


#  3.3) str
# Python program showing
# a use of str() function

a = 1
print(type(a))

# converting integer
# into string
a = str(a)
print(type(a))

s =[1, 2, 3, 4, 5]
print(type(s))

# converting list
# into string
s = str(s)
print(type(s))


# 3.4 id
# Python program showing
# a use of id() function

import math
a =[1, 2, 3, 4, 5]

# print id of a
print(id(a))
b =(1, 2, 3, 4, 5)

# print id of b
print(id(b))
c ={1, 2, 3, 4, 5}

# print id of c
print(id(c))


#  3.5 other code methods
# help()
# hasattr()
# getattr()
# repr()
# callable()
# issubclass()
# isinstance()
# sys()
# __doc__
# __name__


# 4 Errors and Exceptions

# 4.1 Syntax Errors
while True print('Hello world')
# File "<stdin>", line 1
# while True print('Hello world')
# ^
# SyntaxError: invalid syntax


#  4.2 Exceptions
10 * (1/0)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero

4 + spam*3
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# NameError: name 'spam' is not defined

'2' + 2
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: Can't convert 'int' object to str implicitly



#  5) Multi-thread computing
# Google:
# High-level data structures python