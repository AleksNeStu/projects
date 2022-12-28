# Python and Objects
# Allocs
# Deallocs
#
#
#
# The Leak○with confirmed existence
#
# Hunting!Explore:sanket.plus
# Python2
import os, psutil, gc, time
l = [i for i in range(100000000)]

curr_process = psutil.Process(os.getpid())

print(curr_process.memory_info())

# pmem(rss=4059226112, vms=4689965056, shared=20520960, text=4096, lib=0, data=4395610112, dirty=0)

# https://www.baeldung.com/linux/resident-set-vs-virtual-memory-size

# Resident Set Size (RSS)
# This is a measure of how much memory a process is consuming in our physical RAM, to load all of its pages after its execution.
#
# This includes memory allocated from shared libraries, given they are still present in memory. Also, it includes all heap and stack memory.


# Virtual Memory Size (VSZ)
# This is a measure of much memory a process can access after its execution.
#
# This includes swapped memory, the memory from external libraries, and allocated memory that’s not used.
# VSZ is not an accurate measure of how much memory is being consumed, but rather an estimation of the total amount of memory a process can consume within its life cycle.

del l
print(curr_process.memory_info())
# pmem(rss=48517120, vms=617717760, shared=20574208, text=4096, lib=0, data=323362816, dirty=0)

# C language
# typedef struct_object {
#      PyObject_HEAD      // contains ref_count
# } PyObject;


# typedef struct {
#       PyObject_HEAD
#       long ob_ival;
# } PyIntObject;


# Free lists
def release_list(a):
    del a[:]
    del a
# Do not ever do this. Python automatically frees all objects that are not referenced any more, so a simple del a ensures that the list's memory will be released if the list isn't referenced anywhere else. If that's the case, then the individual list items will also be released (and any objects referenced only from them, and so on and so on), unless some of the individual items were also still referenced.

# That means the only time when del a[:]; del a will release more than del a on its own is when the list is referenced somewhere else. This is precisely when you shouldn't be emptying out the list: someone else is still using it!!!

# static PyListObject *free_list[PyList_MAXFREELIST];
# static PyDictObject *free_list[PyDict_MAXFREELIST];
# tatic PyFrameObject *free_list = NULL;
# staticint numfree = 0;         /* number of frames currently in free_list */
# #definePyFrame_MAXFREELIST200

# Garbage Collection
# Garbage Collection●Generation based○A linked list for each generation
#
# When run in last generation (= 2)
# Clear free lists as well/
# Clear free list only during the collection of the highest
# * generation */if (generation == NUM_GENERATIONS-1) {clear_freelists();    }

# Allocation1.If free_list has space○Use last slot from free_list2.Else: allocate memory○Initialize the object○Register object with GC (ie: add in linked list)*

# Immutables○long,  float, string2.containers○list, dictnot every object gets GC tracked