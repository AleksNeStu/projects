import collections
import types

'''
Dictionaries in Python: Summary
All the Python dictionary implementations listed in this tutorial are valid implementations that are built into the Python standard library.

If you’re looking for a general recommendation on which mapping type to use in your programs, I’d point you to the built-in dict data type. It’s a versatile and optimized hash table implementation that’s built directly into the core language.

I would recommend that you use one of the other data types listed here only if you have special requirements that go beyond what’s provided by dict.

All the implementations are valid options, but your code will be clearer and easier to maintain if it relies on standard Python dictionaries most of the time.
'''

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


# 2) collections.OrderedDict: Remember the Insertion Order of Keys
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

# 3) collections.defaultdict: Return Default Values for Missing Keys
# The defaultdict class is another dictionary subclass that accepts a callable in its constructor whose return value will be used if a requested key cannot be found.
dd = collections.defaultdict(list)

# Accessing a missing key creates it and
# initializes it using the default factory,
# i.e. list() in this example:
dd["dogs"].append("Rufus")
dd["dogs"].append("Kathrin")
dd["dogs"].append("Mr Sniffles")

print(dd["dogs"])

# 4) collections.ChainMap: Search Multiple Dictionaries as a Single Mapping
dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four": 4}
chain = collections.ChainMap(dict1, dict2)
# ChainMap searches each collection in the chain
# from left to right until it finds the key (or fails):
print(chain["three"])
print(chain["one"])
# print(chain["missing"]) -> err


# collections

# 5) types.MappingProxyType: A Wrapper for Making Read-Only Dictionaries
# frozenset()
# frozendict()
# # Curiously, although we have the seldom useful frozenset, there's still no frozen mapping. The idea was rejected in PEP 416 -- Add a frozendict builtin type. This idea may be revisited in a later Python release, see PEP 603 -- Adding a frozenmap type to collections.
default_config = {'a': 1}
DEFAULTS = types.MappingProxyType(default_config)
# So changes in the default_config will update DEFAULTS as expected, but you can't write to the mapping proxy object
# itself.
default_config["b"] = 2
# DEFAULTS['b'] = 22 # TypeError: 'mappingproxy' object does not support item assignment

def foo(config=DEFAULTS):
    return dict(config)

# Now the default config can be updated dynamically, but remain immutable where you want it to be immutable by
# passing around the proxy instead.

# Admittedly it's not really the same thing as an "immutable, hashable dict", but it might be a decent substitute for
# some use cases of a frozendict.
f = foo()

'''
- MappingProxyType is a wrapper around a standard dictionary that provides a read-only view into the wrapped 
dictionary’s data. This class was added in Python 3.3 and can be used to create immutable proxy versions of dictionaries.
- MappingProxyType can be helpful if, for example, you’d like to return a dictionary carrying internal state from a class or module while discouraging write access to this object
- Using MappingProxyType allows you to put these restrictions in place without first having to create a full copy of the dictionary
'''
writable = {"one": 1, "two": 2}
read_only = types.MappingProxyType(writable)
# The proxy is read-only:
print(read_only["one"])
# read_only["one"] = 23 -> error
# Updates to the original are reflected in the proxy:
writable["one"] = 42
print(read_only)

# Alternative
# https://github.com/Marco-Sulla/python-frozendict
from frozendict import frozendict

fd = frozendict({"Guzzanti": "Corrado", "Hicks": "Bill"})
print(fd["Guzzanti"])
# Corrado
# fd["Brignano"] -> KeyError: 'Brignano'
assert len(fd) == 2
assert "Guzzanti" in fd
# True
# assert "Guzzanti" not in fd
# # False
# assert "Brignano" in fd
# # Falses
print(hash(fd))  #e.g. 5833699487320513741


fd_unhashable = frozendict({1: []})
# hash(fd_unhashable)
# TypeError: unhashable type: 'list'
fd | {1: 2}
# frozendict({'Guzzanti': 'Corrado', 'Hicks': 'Bill', 1: 2})

fd5 = frozendict(fd)
id_fd5 = id(fd5)
fd5 |= {1: 2}
fd5
# frozendict.frozendict({'Guzzanti': 'Corrado', 'Hicks': 'Bill', 1: 2})
id(fd5) != id_fd5
# True

fd.set(1, 2)
# frozendict.frozendict({'Guzzanti': 'Corrado', 'Hicks': 'Bill', 1: 2})

fd.set("Guzzanti", "Sabina")
# frozendict.frozendict({'Guzzanti': 'Sabina', 'Hicks': 'Bill'})

fd.delete("Guzzanti")
# frozendict.frozendict({'Hicks': 'Bill'})

fd.setdefault("Guzzanti", "Sabina")
# frozendict.frozendict({'Guzzanti': 'Corrado', 'Hicks': 'Bill'})

fd.setdefault(1, 2)
# frozendict.frozendict({'Guzzanti': 'Corrado', 'Hicks': 'Bill', 1: 2})

fd.key()
# 'Guzzanti'

fd.value(1)
# 'Bill'

fd.item(-1)
# (1, 2)
fd2 = fd.copy()
fd2 == fd
# True

fd3 = frozendict(fd)
fd3 == fd
# True

fd4 = frozendict({"Hicks": "Bill", "Guzzanti": "Corrado"})

print(fd4)
# frozendict({'Hicks': 'Bill', 'Guzzanti': 'Corrado'})

fd4 == fd
# True

import pickle
fd_unpickled = pickle.loads(pickle.dumps(fd))
print(fd_unpickled)
# frozendict({'Guzzanti': 'Corrado', 'Hicks': 'Bill'})
fd_unpickled == fd
# True

frozendict(Guzzanti="Corrado", Hicks="Bill")
# frozendict({'Guzzanti': 'Corrado', 'Hicks': 'Bill'}

frozendict((("Guzzanti", "Corrado"), ("Hicks", "Bill")))
# frozendict({'Guzzanti': 'Corrado', 'Hicks': 'Bill'})

fd.get("Guzzanti")
# 'Corrado'

print(fd.get("Brignano"))
# None

tuple(fd.keys())
# ('Guzzanti', 'Hicks')

tuple(fd.values())
# ('Corrado', 'Bill')

tuple(fd.items())
# (('Guzzanti', 'Corrado'), ('Hicks', 'Bill'))

frozendict.fromkeys(["Corrado", "Sabina"], "Guzzanti")
# frozendict({'Corrado': 'Guzzanti', 'Sabina': 'Guzzanti'})

iter(fd)
# <dict_keyiterator object at 0x7feb75c49188>

# fd["Guzzanti"] = "Caterina"
# TypeError: 'frozendict' object doesn't support item assignment