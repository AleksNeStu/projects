#1.1
a = "aaa"
b = "bbb"
c = "ccc"
final = a + b + c
print(final)


objects = ('obj1', 'obj2')

#1.2
print(*objects, sep=' separator ')
print(*objects, 'separator')

#1.3
res = print(*objects)

#1.4
a = 5
print("a =", a, sep='00000', end='\n\n\n')
print("a =", a, sep='0', end='')

#1.5
with open ('.\python.txt', 'w') as file:
    print('Pretty cool, huh!', file = file)

#1.6
data = [ (i, { 'a':'A',
               'b':'B',
               'c':'C',
               'd':'D',
               'e':'E',
               'f':'F',
               'g':'G',
               'h':'H',
               })
         for i in range(3)
         ]
from pprint import pprint

print('print:\n', data , '\n')

print('print:\n')
pprint(data)