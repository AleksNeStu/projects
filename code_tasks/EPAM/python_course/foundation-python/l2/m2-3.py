# 1) Multiple assignment
# Multiple assignment for sting
x, y = 'hi'
# >>> x
# 'h'
# >>> y
# 'i'


# An alternative to slicing
numbers = [1, 2, 3, 4, 5, 6]
first, *rest = numbers
# >>> rest
# [2, 3, 4, 5, 6]
# >>> first
# 1


# 2) del

# del x


# or you can remove them from the globals() object:

for name in dir():
    if not name.startswith('_'):
        del globals()[name]



# 3 convertion
# tuple()
# set()
# list()
int('1', 10)


g = set
g = {}