"""Function as the prime class object."""

a = 10
a = sum
a([1,2])

help(a)
def mul(iterable):
    if iterable:
        res = iterable[0]
        for i in iterable[1:]: res *= i
        return res

a = mul
a([1,2])
help(a)