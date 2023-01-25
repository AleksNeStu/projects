import collections

# called maps, hashmaps, lookup tables, or associative arrays
# 1) Example
phonebook = {
    "bob": 7387,
    "alice": 3719,
    "jack": 7052,
}

squares = {x: x * x for x in range(6)}

print(phonebook["alice"])
print(squares)

'''
- Python’s dictionaries are indexed by keys that can be of any hashable type. A hashable object has a hash value that 
never changes during its lifetime (see __hash__), and it can be compared to other objects (see __eq__).
Hashable objects that compare as equal must have the same hash value.
- Immutable types like strings and numbers are hashable and work well as dictionary keys. You can also use tuple 
objects as dictionary keys as long as they contain only hashable types themselves.
- Class attributes and variables in a stack frame are both stored internally in dictionaries.
- hash table implementation that provides the performance characteristics you’d expect: O(1) time complexity for lookup, insert, update, and delete operations in the average case.
- third-party dictionary implementations exist, such as skip lists or B-tree–based dictionaries.
'''


# 2) collections.OrderedDict
# if key order is important for your algorithm to work, then it’s best to communicate this clearly by explicitly using the OrderedDict class:
d_or = collections.OrderedDict(one=1, two=2, three=3)
d_simple = dict(one=1, two=2, three=3)
d_or["four"] = 4
d_simple["four"] = 4
print(d_or.keys())
print(d_simple.keys())

# Until Python 3.8, you couldn’t iterate over dictionary items in reverse order using reversed()
# Python reversed() with Built-In Sequence Objects
assert list(reversed(d_or)) == list(reversed(d_simple)) == ['four', 'three', 'two', 'one']
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
# reverse of a tuple object
print(list(reversed(seq_tuple)))

# reversed() with Custom Objects
class Vowels:
    vowels = ['v', 'o', 'l', 'v', 'o']

    def __reversed__(self):
        return reversed(self.vowels)
v = Vowels()
# reverse a custom object v
print(list(reversed(v)))

# Reordering Items With .move_to_end()
#  This method allows you to move existing items to either the end or the beginning of the underlying dictionary, so it’s a great tool for reordering a dictionary.
d_or.move_to_end(key='one', last=True) #  True -> to the end, False -> to the beginning
# key holds the key that identifies the item you want to move. If key doesn’t exist, then you get a KeyError.
