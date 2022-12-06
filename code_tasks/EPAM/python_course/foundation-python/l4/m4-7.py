"""Usage of lambda."""

l = [{'a':1}, {'a':2}, {'a':3}, {'a':4}]
f = lambda d: d.get('a')
f(l[1])

f = lambda d: d.get('a', 'No value')
[f(item) for item in l]


h = 1