### Abstract data types are built into the Python standard library

### Most common abstract data types map to Python’s naming scheme


### Put abstract data types to practical use in various algorithms

## Collections
+ namedtuple   factory function for creating tuple subclasses with named fields
+ deque        list-like container with fast appends and pops on either end
+ ChainMap     dict-like class for creating a single view of multiple mappings
+ Counter      dict subclass for counting hashable objects (Multisets, Bag)
+ OrderedDict  dict subclass that remembers the order entries were added
+ defaultdict  dict subclass that calls a factory function to supply missing values
* UserDict     wrapper around dictionary objects for easier dict subclassing
* UserList     wrapper around list objects for easier list subclassing
* UserString   wrapper around string objects for easier string subclassing


## Types
* FunctionType = type(_f)
* LambdaType = type(lambda: None)
* CodeType = type(_f.__code__)
+ MappingProxyType = type(type.__dict__)
+ SimpleNamespace = type(sys.implementation)


## Typing
+ NamedTuple


## Queue
+ LifoQueue
* SimpleQueue
* Empty
* Full
* Queue
* PriorityQueue


## Dictionaries, Maps, and Hash Tables
    dict: Your Go-To Dictionary
    collections.OrderedDict: Remember the Insertion Order of Keys
    collections.defaultdict: Return Default Values for Missing Keys
    collections.ChainMap: Search Multiple Dictionaries as a Single Mapping
    types.MappingProxyType: A Wrapper for Making Read-Only Dictionaries

## Array Data Structures
    list: Mutable Dynamic Arrays
    tuple: Immutable Containers
    array.array: Basic Typed Arrays
    str: Immutable Arrays of Unicode Characters
    bytes: Immutable Arrays of Single Bytes
    bytearray: Mutable Arrays of Single Bytes

## Records, Structs, and Data Transfer Objects
    dict: Simple Data Objects
    tuple: Immutable Groups of Objects
    Write a Custom Class: More Work, More Control
    dataclasses.dataclass: Python 3.7+ Data Classes
    collections.namedtuple: Convenient Data Objects
    typing.NamedTuple: Improved Namedtuples
    struct.Struct: Serialized C Structs
    types.SimpleNamespace: Fancy Attribute Access

## Sets and Multisets
    set: Your Go-To Set
    frozenset: Immutable Sets
    collections.Counter: Multisets


## Stacks (LIFOs)
    list: Simple, Built-In Stacks
    collections.deque: Fast and Robust Stacks
    queue.LifoQueue: Locking Semantics for Parallel Computing

## Queues (FIFOs)
    list: Terribly Sloooow Queues
    collections.deque: Fast and Robust Queues
    queue.Queue: Locking Semantics for Parallel Computing
    multiprocessing.Queue: Shared Job Queues

## Priority Queues
    list: Manually Sorted Queues
    heapq: List-Based Binary Heaps
    queue.PriorityQueue: Beautiful Priority Queues