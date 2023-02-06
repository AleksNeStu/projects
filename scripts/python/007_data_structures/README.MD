### Abstract data types are built into the Python standard library

### Most common abstract data types map to Python’s naming scheme


### Put abstract data types to practical use in various algorithms

## Collections
+ namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
+ ChainMap     dict-like class for creating a single view of multiple mappings
* Counter      dict subclass for counting hashable objects
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
* SimpleNamespace = type(sys.implementation)


## Typing
* NamedTuple
...
