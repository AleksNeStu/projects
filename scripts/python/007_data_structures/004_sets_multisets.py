'''
Sets and Multisets in Python: Summary
Sets are another useful and commonly used data structure included with Python and its standard library. Here are a few guidelines for deciding which one to use:

If you need a mutable set, then use the built-in set type.
If you need hashable objects that can be used as dictionary or set keys, then use a frozenset.
If you need a multiset, or bag, data structure, then use collections.Counter
'''
# 1) set: Your Go-To Set
# A set is an unordered collection of objects that doesn’t allow duplicate elements.
vowels = {"a", "e", "i", "o", "u"}
squares = {x * x for x in range(10)}
any_set = set()
# In a proper set implementation, membership tests are expected to run in fast O(1) time. Union, intersection, difference, and subset operations should take O(n) time on average.

vowels = {"a", "e", "i", "o", "u"}
assert "e" in vowels


letters = set("alice")
assert {'a', 'e', 'i'} == letters.intersection(vowels)

vowels.add("x")
assert {'i', 'a', 'u', 'o', 'x', 'e'} == vowels


assert 6 == len(vowels)

# 2) frozenset: Immutable Sets
# The frozenset class implements an immutable version of set that can’t be changed after it’s been constructed. frozenset objects are static and allow only query operations on their elements, not inserts or deletions

# Because frozenset objects are static and hashable, they can be used as dictionary keys
# as elements of another set, something that isn’t possible with regular (mutable) set objects:
vowels = frozenset({"a", "e", "i", "o", "u"})
try:
    vowels.add("p")
except AttributeError as err:
    assert str(err) == "\'frozenset\' object has no attribute \'add\'"
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'frozenset' object has no attribute 'add'

# Frozensets are hashable and can be used as dictionary keys:
d = {
    frozenset({1, 2, 3}): "hello"
}
assert 'hello' == d[frozenset({1, 2, 3})]


# 3) collections.Counter: Multisets
# The collections.Counter class in the Python standard library implements a multiset, or bag, type that allows elements in the set to have more than one occurrence.

# Dict subclass for counting hashable items.  Sometimes called a bag or multiset.
from collections import Counter
inventory = Counter()


loot = {"sword": 1, "bread": 3}
inventory.update(loot)
# inventory


more_loot = {"sword": 1, "apple": 1}
inventory.update(more_loot)
assert dict(inventory) == {'sword': 2, 'bread': 3, 'apple': 1}

# Unique elements
assert 3 == len(inventory)

# sum(inventory.keys())
