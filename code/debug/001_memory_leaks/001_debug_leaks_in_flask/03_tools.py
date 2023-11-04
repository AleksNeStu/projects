# 1) objgraph
# https://pypi.org/project/objgraph/
x = []
y = [x, [x], dict(x=x)]
import objgraph
objgraph.show_refs([y], filename='sample-graph.png')

#2) memory_profiler
# https://github.com/pythonprofilers/memory_profiler
from memory_profiler import profile


@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

my_func()

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     13     67.4 MiB     67.4 MiB           1   @profile
#     14                                         def my_func():
#     15     74.9 MiB      7.5 MiB           1       a = [1] * (10 ** 6)
#     16    227.5 MiB    152.6 MiB           1       b = [2] * (2 * 10 ** 7)
#     17     75.1 MiB   -152.4 MiB           1       del b
#     18     75.1 MiB      0.0 MiB           1       return a
#
#
#
# Process finished with exit code 0

# Time-based memory usage
# mprof run <executable>
# mprof plot


# 3) guppy3
# https://github.com/zhuyifei1999/guppy3/

from guppy import hpy

h=hpy()
print(h.heap())


print(h.heap().byid[0].sp)

print(h.iso(1,[],{}))

