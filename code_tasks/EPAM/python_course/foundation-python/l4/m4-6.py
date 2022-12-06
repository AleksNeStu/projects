"""Anonymous functions - lambda."""
#lambda [arg1 [,arg2,.....argn]]:expression

#!/usr/bin/python

# Function definition

# sum1 = lambda a, b: a + b
#
# # Sum as a function
# print("sum1 : ", sum(10, 20))
# print("sum1 : ", sum(20, 20))

def key1(x):
    return x[1]

a = [(1, 2), (3, 1), (5, 10), (11, -3)]
a.sort(key=key1)

