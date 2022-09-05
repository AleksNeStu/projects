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


print("test_all")
#  def runtime(function, array="random", size, epoch=1):
#         It will simply returns execution time to sort length of size of test array, returns Tuple[float, List[Any]]
complexity_all = lib.test_all(quick_sort)

# print("compare")
# #     def compare(function1, function2, array, size, epoch=3):
# #         It will compare two functions on {array} case, returns dict
#
#
# from bigO.algorithm import *
# arr = lib.genRandomArray(22)
# print(bubbleSort(arr))
#
# # test all algorithms
# lib.test_all(bubbleSort)
# lib.test_all(brickSort)
# lib.test_all(binarySearch)
# lib.test_all(binaryInsertSort)
# lib.test_all(countSort)
# lib.test_all(combSort)
# lib.test_all(selectionSort)
# lib.test_all(introSort)
# lib.test_all(introSortHelper)
# lib.test_all(insertSort)
# lib.test_all(insertSortOptimized)
# lib.test_all(heapSort)
# lib.test_all(heapSort2)
# lib.test_all(timSort)
# lib.test_all(quickSort)
# lib.test_all(quickSortHoare)
# lib.test_all(quickSortHeap)
# lib.test_all(partition)
# lib.test_all(gnomeSort)
# lib.test_all(mergeSort)
# lib.test_all(goSort)
# lib.test_all(gravitySort)
# lib.test_all(doubleSelectionSort)
# lib.test_all(radixSort)