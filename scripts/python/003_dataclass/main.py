from dataclasses import dataclass


# 1) Dataclass
# # comes with basic functionality already implemented:
# # - instantiate, print, and compare data class instances straight out of the box:
# Seems like data classes are helping us out behind the scenes. By default, data classes implement a .__repr__() method to provide a nice string representation and an .__eq__()
@dataclass
class DataClassCard:
    rank: str
    suit: str


queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts.rank)
print(queen_of_hearts)

#2) Compare that to a regular class. A minimal regular class would look something like this:
class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)

queen_of_hearts = RegularCard('Q', 'Hearts')
print(queen_of_hearts.rank)
print(queen_of_hearts)

# 3) Alternatives to Data Classes
queen_of_hearts_tuple = ('Q', 'Hearts')
queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Hearts'}
# You need to remember that the queen_of_hearts_... variable represents a card.
# For the tuple version, you need to remember the order of the attributes. Writing ('Spades', 'A') will mess up your program but probably not give you an easily understandable error message.
# If you use the dict version, you must make sure the names of the attributes are consistent. For instance {'value': 'A', 'suit': 'Spades'} will not work as expected.

# a)
a1 = queen_of_hearts_tuple[0]  # No named access
a2 = queen_of_hearts_dict['suit']  # Would be nicer with .suit


# b)
# A better alternative is the namedtuple.
from collections import namedtuple

NamedTupleCard = namedtuple(
    'NamedTupleCard', ['rank', 'suit'], defaults={'rank': 1, 'suit': 'Lol1'})

named_tuple_card = NamedTupleCard()
print(named_tuple_card)

from typing import NamedTuple

# Create a named tuple with field names 'name', 'age', and 'gender'
# and field types str, int, and str, respectively
class Person(NamedTuple):
    name: str
    age: int
    gender: str

    # Set default values for the fields
    #  __defaults__ attribute is not part of the public API of NamedTuple and should be used with caution, as it may not work in future versions of Python.
    __defaults__ = ('John Doe', 0, 'unknown')


# Create an instance of the named tuple
p1 = Person('Alice', 26, 'female')
print(p1)
# Access the fields of the named tuple using dot notation or by index
print(p1.name)  # Output: 'Alice'
print(p1[0])    # Output: 'Alice'

# Alternatively, you can define default values for the fields in a NamedTuple by defining a default value for the corresponding argument in the field's type annotation. Here is an example of how to do this:
class Person2(NamedTuple):
    name: str = 'John Doe'
    age: int = 0
    gender: str = 'unknown'



p2 = Person2(age=11)
print(type(p2))
print(p2)

# Pros
# Data classes will not replace all uses of namedtuple. For instance, if you need your data structure to behave like a tuple, then a named tuple is a great alternative!

# Cons of namedtuple:
# namedtuple has some other features that are not necessarily desirable.
# lack of awareness about its own type can lead to subtle and hard-to-find bugs, especially since it will also happily compare two different namedtuple classes:
#  hard to add default values to some of the fields in a namedtuple. A namedtuple is also by nature immutable.
card = NamedTupleCard('7', 'Diamonds')
# card.rank = '9' # AttributeError: can't set attribute

# c)
# Another alternative, and one of the inspirations for data classes, is the attrs project. With attrs installed (pip install attrs), you can write a card class as follows:

import attr

@attr.s
class AttrsCard:
    rank = attr.ib()
    suit = attr.ib()

# pros
# However, as attrs is not a part of the standard library, it does add an external dependency to your projects.

# cons
# This can be used in exactly the same way as the DataClassCard and NamedTupleCard examples earlier. The attrs project is great and does support some features that data classes do not, including converters and validators.
# Furthermore, attrs has been around for a while and is supported in Python 2.7 as well as Python 3.4 and up.

# d) In addition to tuple, dict, namedtuple, and attrs, there are many other similar projects, including typing.NamedTuple, namedlist, attrdict, plumber, and fields.

#  if you need compatibility with a specific API expecting tuples or need functionality not supported in data classes.
from attrdict import AttrDict

attr = AttrDict({'foo': {'bar': 'baz'}})
# issue in legacy lib:
# cannot import name 'Mapping' from 'collections'
# if sys.version_info >= (3, 10):
#     from collections.abc import Mapping, MutableMapping, Sequence
# else:
#     from collections import Mapping, MutableMapping, Sequence


print(attr.foo.bar)

# 4) How to add default values to data class fields
# similarly to how named tuples are created.
from dataclasses import make_dataclass

Position = make_dataclass('Position', ['name', 'lat', 'lon'])

# This works exactly as if you had specified the default values in the definition of the .__init__() method of a regular class:
@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0
# Later you will learn about default_factory, which gives a way to provide more complicated default values.
#  However, if you do not want to add explicit types to your data class, use typing.Any:

from typing import List

@dataclass
class PlayingCard:
    rank: str
    suit: str

@dataclass
class Deck:
    cards: List[PlayingCard]

queen_of_hearts = PlayingCard('Q', 'Hearts')
ace_of_spades = PlayingCard('A', 'Spades')
two_cards = Deck([queen_of_hearts, ace_of_spades])
print(two_cards)

# Advanced Default Values
RANKS = 'Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

print(make_french_deck())

from typing import List
from dataclasses import field

@dataclass
class Deck:  # Will NOT work
    # cards: List[PlayingCard] = make_french_deck()
    cards: List[PlayingCard] = field(default_factory=make_french_deck)
    # ValueError: mutable default <class 'list'> for field cards is not allowed: use default_factory

# The argument to default_factory can be any zero parameter callable. Now it is easy to create a full deck of playing cards:
print(Deck())

# Don’t do this! This introduces one of the most common anti-patterns in Python: using mutable default arguments. The problem is that all instances of Deck will use the same list object as the default value of the .cards property. This means that if, say, one card is removed from one Deck, then it disappears from all other instances of Deck as well. Actually, data classes try to prevent you from doing this, and the code above will raise a ValueError.

# 5) field
# default: Default value of the field
# default_factory: Function that returns the initial value of the field
# init: Use field in .__init__() method? (Default is True.)
# repr: Use field in repr of the object? (Default is True.)
# compare: Include the field in comparisons? (Default is True.)
# hash: Include the field when calculating hash()? (Default is to use the same as for compare.)
# metadata: A mapping with information about the field
# In the Position example, you saw how to add simple default values by writing lat: float = 0.0. However, if you also want to customize the field, for instance to hide it in the repr, you need to use the default parameter: lat: float = field(default=0.0, repr=False). You may not specify both default and default_factory.

from dataclasses import dataclass, field

@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})
from dataclasses import fields
# The metadata (and other information about a field) can be retrieved using the fields() function (note the plural s):
print(fields(Position))

lat_unit = fields(Position)[2].metadata['unit']
print(lat_unit)

# 6) Representation
print(Deck())
# Let us add a more concise representation. In general, a Python object has two different string representations:

# repr(obj) is defined by obj.__repr__() and should return a developer-friendly representation of obj. If possible, this should be code that can recreate obj. Data classes do this.

# str(obj) is defined by obj.__str__() and should return a user-friendly representation of obj. Data classes do not implement a .__str__() method, so Python will fall back to the .__repr__() method.

from dataclasses import dataclass

@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'


ace_of_spades = PlayingCard('A', '♠')

print(ace_of_spades)

print(Deck())

from dataclasses import dataclass, field
from typing import List

@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'
print(Deck())
# This is a nicer representation of the deck. However, it comes at a cost. You’re no longer able to recreate the deck by executing its representation. Often, you’d be better off implementing the same representation with .__str__() instead.

# 7) How data classes allow for ordering of objects
# For PlayingCard to use this sort index for comparisons, we need to add a field .sort_index to the class. However, this field should be calculated from the other fields .rank and .suit automatically. This is exactly what the special method .__post_init__() is for. It allows for special processing after the regular .__init__() method is called:
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'

# Note that .sort_index is added as the first field of the class. That way, the comparison is first done using .sort_index and only if there are ties are the other fields used. Using field(), you must also specify that .sort_index should not be included as a parameter in the .__init__() method (because it is calculated from the .rank and .suit fields). To avoid confusing the user about this implementation detail, it is probably also a good idea to remove .sort_index from the repr of the class.
queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')
print(ace_of_spades > queen_of_hearts)
print(Deck(sorted(make_french_deck())))
from random import sample
print(Deck(sample(make_french_deck(), k=10)))

# 8) How to represent immutable data
# To make a data class immutable, set frozen=True when you create it. For example, the following is an immutable version of the Position class you saw earlier:
from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

pos = Position('Oslo', 10.8, 59.9)
print(pos.name)

# pos.name = 'Stockholm'
# dataclasses.FrozenInstanceError: cannot assign to field 'name'

from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str

@dataclass(frozen=True)
class ImmutableDeck:
    cards: List[ImmutableCard]
# Even though both ImmutableCard and ImmutableDeck are immutable, the list holding cards is not. You can therefore still change the cards in the deck:
queen_of_hearts = ImmutableCard('Q', '♡')
ace_of_spades = ImmutableCard('A', '♠')
deck = ImmutableDeck([queen_of_hearts, ace_of_spades])
print(deck)

deck.cards[0] = ImmutableCard('7', '♢')
print(deck)
# To avoid this, make sure all fields of an immutable data class use immutable types (but remember that types are not enforced at runtime). The ImmutableDeck should be implemented using a tuple instead of a list.

# 9) How data classes handle inheritance
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

@dataclass
class Capital(Position):
    country: str = 'Unknown' # Does NOT work need def val
    lat: float = 40.0
    # TypeError: non-default argument 'country' follows default argument
# Then the order of the fields in Capital will still be name, lon, lat, country. However, the default value of lat will be 40.0.

# However, this is not valid Python. If a parameter has a default value, all following parameters must also have a default value. In other words, if a field in a base class has a default value, then all new fields added in a subclass must have default values as well.

# 10) Optimizing Data Classes
# I’m going to end this tutorial with a few words about slots. Slots can be used to make classes faster and use less memory. Data classes have no explicit syntax for working with slots, but the normal way of creating slots works for data classes as well. (They really are just regular classes!)

@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float

@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float

# Essentially, slots are defined using .__slots__ to list the variables on a class. Variables or attributes not present in .__slots__ may not be defined. Furthermore, a slots class may not have default values.

from pympler import asizeof
simple = SimplePosition('London', -0.1, 51.5)
slot = SlotPosition('Madrid', -3.7, 40.4)
res = asizeof.asizesof(simple, slot)
print(res)

# Similarly, slots classes are typically faster to work with. The following example measures the speed of attribute access on a slots data class and a regular data class using timeit from the standard library.
from timeit import timeit
r1 = timeit('slot.name', setup="slot=SlotPosition('Oslo', 10.8, 59.9)", globals=globals())
print(r1)
r2 = timeit('simple.name', setup="simple=SimplePosition('Oslo', 10.8, 59.9)", globals=globals())
print(r2)

from codetiming import Timer
t = Timer(text="Elapsed time22: {:.9f} ms")
with t:
    simple = SimplePosition('London', -0.1, 51.5)
with t:
    slot = SlotPosition('Madrid', -3.7, 40.4)
