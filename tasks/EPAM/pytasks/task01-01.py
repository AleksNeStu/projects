#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

#Task01-01: Create function factory `add_factory` using 5 different approaches like this:
# >>> add5 = add_factory(5)
# >>> print add5(10)
# 15

import operator
import functools
from functools import wraps


#Input
x = int(5)
y = int(10)

#Example #1 (Carrying)
def res1(x):
    def add(y):
        return x + y
    return add
print 'Example#1:', res1(x)(y)
# print add5.__closure__[0].cell_contents #x = 5


#Example #2 (Decorator)
def decorator(func):
    #Decorator
    def decorated_function(*args, **kwargs):
        #Modified function
        return func(*args, **kwargs)  #Call the original function
    return decorated_function
@decorator
def res2(x,y):
    return x + y
print 'Example#2:', res2(x,y) #Call the decorated function


#Example #3 (Decorator & Operator)
@decorator
def res3(x,y):
   return operator.add(x,y)
print 'Example#3:', res3(x,y)


#Example #4 (functools.wraps & basic decorator)
def decorator_n4(func):
    def decorated_function_n4(*args, **kwargs):
        #Do something before the func call
        input = func(*args, **kwargs)
        #Do something after the func call
        return input
    return wraps(func)(decorated_function_n4)
@decorator_n4
def res4(x,y):
    return x + y
print 'Example#4:', res4(x,y)


#Example #5 (functools.wraps & parameterized decorator)
def decorator_n5(extra_value=None):
    def decorator_n5_my(view_func):
        def decorated_function_n5(*args, **kwargs):
            input = view_func(*args, **kwargs)
            return input
        return wraps(view_func)(decorated_function_n5)
    return decorator_n5_my
@decorator_n5('Operation')
def res5(x,y):
    return x + y
print 'Example#5:', res5(x,y)

#Example #6 (functools.wraps & class decorator)
class decorator_n6(object):
    def __init__(self, func):
        self.func = func
        wraps(func)(self)
    def __call__(self, *args, **kwargs):
        input = self.func(*args, **kwargs)
        return input
@decorator_n6
def res6(x,y):
    return x + y
print 'Example#6:', res6(x,y)


#Example #7 (function as first class object)
#Saving references to the functions in the data structure
def add(x, y):
    return x + y
res7 = {
    '+': add,
}
print 'Example#7:', (res7['+'](x,y))

#Example #8 (lambda expression)
def res8(x,y):
    add = {
    '+': lambda x, y: x + y,
}
    return add['+'](x,y)
print 'Example#8:', res8(x,y)

#Example #9 (lambda expression2)
def res9(x):
    return lambda y: y + x
print 'Example#9:', res9(x)(y)

#Example #10(__call__)
# __call__( self[, args...])
# Called when the instance is ``called'' as a function; if this method is defined, x(arg1, arg2, ...) is a
# shorthand for x.__call__(arg1, arg2, ...).
class res10(object):
    def __init__(self, x):
        self.x = x
    def __call__(self, y):
        return y + self.x
print 'Example#10:', res10(x)(y)

#Example #11(New partial object which when called will behave like func called with the positional
#  arguments args and keyword arguments keywords.)
def res11(x):
    return functools.partial(operator.add, y)
print 'Example#11:', res11(x)(y)