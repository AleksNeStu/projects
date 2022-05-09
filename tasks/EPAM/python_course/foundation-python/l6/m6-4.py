"""Hiding data."""

class JustCounter:
    """JustCounter docstring."""
    # class variables
    _count_var = 1 # for internal use (protected)
    count_var_ = 1 # to avoid naming conflicts
    __count_var = 1 # private
    __count_var__ = 1 # dunder (magic) methods


    def __init__(self):
        # instance variables
        self.count_var = 1

    def count(self):
        self.__count_var += 1
        print(self.__count_var)




counter = JustCounter()
c0 = counter.count_var
c1 = JustCounter._count_var
c2 = JustCounter.count_var_
c3 = JustCounter.__count_var__


counter.count()
counter.count()
c4 = counter.__count_var
c4_hack = counter._JustCounter__count_var

print("done")


k1 = counter._JustCounter__count_var