from bigO import BigO
from random import randint
# from bigO import utils

# @utils.isSorted


def quick_sort(array):  # in-place | not-stable
    """
    Best : O(nlogn) Time | O(logn) Space
    Average : O(nlogn) Time | O(logn) Space
    Worst : O(n^2) Time | O(logn) Space
    """
    if len(array) <= 1:
        return array
    smaller, equal, larger = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for x in array:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quick_sort(smaller) + equal + quick_sort(larger)


lib = BigO()
print("test")
#     def test(function, array="random", limit=True, prtResult=True):
#         It will run only specified array test, returns Tuple[str, estimatedTime]
complexity_random = lib.test(quick_sort, "random")
complexity_sorted = lib.test(quick_sort, "sorted")
complexity_reversed = lib.test(quick_sort, "reversed")
complexity_partial = lib.test(quick_sort, "partial")
complexity_ksorted = lib.test(quick_sort, "Ksorted")
# Running quick_sort(random array)...
# Completed quick_sort(random array): O(nlog(n))
# Running quick_sort(sorted array)...
# Completed quick_sort(sorted array): O(nlog(n))
# Running quick_sort(reversed array)...
# Completed quick_sort(reversed array): O(nlog(n))
# Running quick_sort(partial array)...
# Completed quick_sort(partial array): O(nlog(n))
# Running quick_sort(Ksorted array)...
# Completed quick_sort(ksorted array): O(nlog(n))


print("runtime")
#     def test_all(function):
#         It will run all test cases, prints (best, average, worst cases), returns dict
complexity_run = lib.runtime(quick_sort, array="random", size=10, epoch=1)

print("test_all")
#  def runtime(function, array="random", size, epoch=1):
#         It will simply returns execution time to sort length of size of test array, returns Tuple[float, List[Any]]
complexity_all = lib.test_all(quick_sort)

print("compare")
#     def compare(function1, function2, array, size, epoch=3):
#         It will compare two functions on {array} case, returns dict


from bigO.algorithm import *
arr = lib.genRandomArray(22)
print(bubbleSort(arr))

# test all algorithms
lib.test_all(bubbleSort)
lib.test_all(brickSort)
lib.test_all(binarySearch)
lib.test_all(binaryInsertSort)
lib.test_all(countSort)
lib.test_all(combSort)
lib.test_all(selectionSort)
lib.test_all(introSort)
lib.test_all(introSortHelper)
lib.test_all(insertSort)
lib.test_all(insertSortOptimized)
lib.test_all(heapSort)
lib.test_all(heapSort2)
lib.test_all(timSort)
lib.test_all(quickSort)
lib.test_all(quickSortHoare)
lib.test_all(quickSortHeap)
lib.test_all(partition)
lib.test_all(gnomeSort)
lib.test_all(mergeSort)
lib.test_all(goSort)
lib.test_all(gravitySort)
lib.test_all(doubleSelectionSort)
lib.test_all(radixSort)