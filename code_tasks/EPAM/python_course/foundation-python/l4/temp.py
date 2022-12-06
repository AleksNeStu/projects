l = [{'a':1}, {'a':2}, {'a':3}, {'a':4}]
# f = lambda d: d.get('a')
# print (f(l[1]))

f = lambda d: d.get('', 'No value')
print([f(item) for item in l])