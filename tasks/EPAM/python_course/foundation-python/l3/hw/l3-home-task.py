""" LIST

1. Write a Python program to check if all dictionaries in a list are empty or not.
Go to the editor
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
"""
# simple solution
is_list_w_empty_dicts1 = lambda l_dicts: not any(d for d in l_dicts)


# faster solution
def is_list_w_empty_dicts2(l_dicts):
    for d in l_dicts:
        if d:
            return False
    return True

LIST_DICTS1 = [{},{},{}]
LIST_DICTS2 = [{1,2},{},{}]

print(is_list_w_empty_dicts1(LIST_DICTS1))
print(is_list_w_empty_dicts1(LIST_DICTS2))
print(is_list_w_empty_dicts2(LIST_DICTS1))
print(is_list_w_empty_dicts2(LIST_DICTS2))


"""
2. Write a Python program to remove duplicates from a list of lists. Go to the
editor
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
"""
def rem_redundant_el_from_list1(l_of_lists):
    return [list(t) for t in set(tuple(l) for l in l_of_lists)]


def rem_redundant_el_from_list2(l_of_lists):
    return [l for n, l in enumerate(l_of_lists) if l not in l_of_lists[:n]]


def rem_redundant_el_from_list3(l_of_lists):
    filtered_l_of_lists = []
    for l in l_of_lists:
        if l not in filtered_l_of_lists:
            filtered_l_of_lists.append(l)
    return filtered_l_of_lists


LIST_OF_LISTS = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print(rem_redundant_el_from_list1(LIST_OF_LISTS))
print(rem_redundant_el_from_list2(LIST_OF_LISTS))
print(rem_redundant_el_from_list3(LIST_OF_LISTS))


"""
3. Write a Python program to find the list in a list of lists whose sum of
elements is the highest. Go to the editor
Sample lists: [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
Expected Output: [10, 11, 12]
"""
def get_l_w_max_sum(l_of_lists):
    return max([(l, sum(l)) for l in l_of_lists], key=lambda x: x[1])[0]


LIST3 = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

print(get_l_w_max_sum(LIST3))


"""
4. Write a Python program to compute the similarity between two lists. Go to the editor
Sample data: ["red", "orange", "green", "blue", "white"],
["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']
"""

def lists_similarity(l1, l2):
    return list(set(l1) - set(l2)), list(set(l2) - set(l1))

LIST4_1 = ["red", "orange", "green", "blue", "white"]
LIST4_2 = ["black", "yellow", "green", "blue"]

print(lists_similarity(LIST4_1, LIST4_2))

"""
5. Write a Python program to change the position of every n-th value with the (n+1)
th in a list. Go to the editor
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]
"""

def change_positions(ls):
    for n, _ in enumerate(ls):
        if n % 2 == 0:
            ls[n+1], ls[n] = ls[n], ls[n+1]
    return ls

LIST5 = [0,1,2,3,4,5]
print(change_positions(LIST5))


"""
6. Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

def sort_list_of_tuples(l_of_tuples):
    return sorted(l_of_tuples, key=lambda t: t[1])


LIST6 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_list_of_tuples(LIST6))


"""
7. Write a Python program to count the number of strings where the string length
 is 2 or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""
def count_strs(l_of_str):
    return len([s for s in l_of_str if len(s) >= 2 and s[0] == s[-1]])

LIST7 = ['abc', 'xyz', 'aba', '1221']
print(count_strs(LIST7))


"""
---
TUPLE
8. Write a Python program to print a tuple with string formatting. Go to the editor
Sample tuple : (100, 200, 300)
Output : This is a tuple (100, 200, 300)
"""

print('This is a tuple {}'.format((100, 200, 300)))


"""
9. Write a Python program to replace last value of tuples in a list. Go to the editor
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""
def replace_els(l_of_tuples, new_el):
    return [t[:-1] + (new_el,) for t in l_of_tuples]


LIST9 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(replace_els(LIST9, 100))


"""
10. Write a Python program to remove an empty tuple(s) from a list of tuples. Go to the editor
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
"""

def rem_empty_tuples(l_of_tuples):
    return [t for t in l_of_tuples if t]


LIST10 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(rem_empty_tuples(LIST10))



"""
11. Write a Python program to sort a tuple by its float element. Go to the editor
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
"""

def sort_list_of_tuples2(l_of_tuples):
    return sorted(l_of_tuples, key=lambda t: t[1], reverse=True)


LIST11 = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sort_list_of_tuples2(LIST11))


"""
SET
12. Write a Python program to create a shallow copy of sets. Go to the editor

Note : Shallow copy is a bit-wise copy of an object. A new object is created
that has an exact copy of the values in the original object.
"""

def shallow_copy_of_set(origin_set):
    return origin_set.copy()

print(shallow_copy_of_set({"Green", "Red"}))

"""
13. Write a Python program to remove an item from a set if it is present in the set.
"""

def rem_el_from_set(origin_set, el_to_del):
    origin_set.discard(el_to_del)
    return origin_set


SET13 = {1, 2, 3, 3, 5, 6, 6, 9}
print(rem_el_from_set(SET13, 3))


"""
---
DICT
14. Write a Python program to print all unique values in a dictionary. Go to the editor
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

import itertools

def get_uniq_vals1(l_of_dicts):
    set_of_values = set(itertools.chain(*[d.values() for d in l_of_dicts]))
    return 'Unique Values: {}'.format(set_of_values)

def get_uniq_vals2(l_of_dicts):
    set_of_values = {v for d in l_of_dicts for v in d.values()}
    return 'Unique Values: {}'.format(set_of_values)


LIST14 = [
    {"V":"S001", "VII":"S007"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
    {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"},
]
print(get_uniq_vals1(LIST14))
print(get_uniq_vals2(LIST14))


"""
15. Write a Python program to create and display all combinations of letters,
 selecting each letter from a different key in a dictionary. Go to the editor
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
"""

import itertools

def get_vals_combinations(dic):
    for c in itertools.product(*dic.values()):
        print(''.join(c))


DICT15 = {'1':['a','b'], '2':['c','d', 'e'], '3':['g']}
get_vals_combinations(DICT15)


"""
16. Write a Python program to create a dictionary from a string. Go to the editor
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""
from collections import Counter

def str_to_dict1(string):
    return {k: string.count(k) for k in set(string)}

def str_to_dict2(string):
    return dict(Counter(string))


STRING16 = 'w3resource'
print(str_to_dict1(STRING16))
print(str_to_dict2(STRING16))


"""
17. Write a Python program to get the top three items in a shop. Go to the editor
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3
"""
def sort_list_of_tuples3(dic):
    for t in sorted(dic.items(), key=lambda t: t[1], reverse=True)[:3]:
        print('{} {}'.format(t[0], t[1]))


DICT17 = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
sort_list_of_tuples3(DICT17)


"""
18. Write a Python program to create a dictionary from two lists without losing
duplicate values. Go to the editor
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2},
'Class-VIII': {3}, 'Class-V': {1}})
"""
def get_def_dict(l1, l2):
    return {k: {v} for k, v in (zip(l1, l2))}


LIST18_1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
LIST18_2 = [1, 2, 2, 3]
print(get_def_dict(LIST18_1, LIST18_2))

"""
19. Write a Python program to match key values in two dictionaries. Go to the editor
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y
"""
def get_match(dic1, dic2):
    set_items1 = set(dic1.items())
    set_items1.intersection_update(set(dic2.items()))
    for same_item in set_items1:
        print('{0}: {1} is present in both x and y'.format(*same_item))



DICT19_1 = {'key1': 1, 'key2': 3, 'key3': 2}
DICT19_2 = {'key1': 1, 'key2': 2, 'key3': 2}
get_match(DICT19_1, DICT19_2)


"""
FUNC
---
20. Write a Python function to sum all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""

def sum_list_els(l):
    return sum(l)


LIST20 = [8, 2, 3, 0, 7]
print(sum_list_els(LIST20))


"""
21.Write a Python function to sum all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""




"""
22.Write a Python program that accepts a hyphen-separated sequence of words as
input and prints the words in a hyphen-separated sequence after sorting them
alphabetically. Go to the editor
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
"""
def convert_str(string):
    return '-'.join(sorted(string.split('-')))


STR22 = 'green-red-yellow-black-white'
print(convert_str(STR22))


"""
23. Write a Python function to check whether a number is perfect or not.
According to Wikipedia : In number theory, a perfect number is a positive integer
 that is equal to the sum of its proper positive divisors, that is, the sum of
 its positive divisors excluding the number itself (also known as its aliquot sum).
 Equivalently, a perfect number is a number that is half the sum of all of its positive
 divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper
positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to
half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next
perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect
numbers 496 and 8128.
"""
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

print(perfect_number(6))


"""
24
Write a Python program to print the even numbers from a given list. Go to the editor
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
Click me to see the sample solution
"""

def get_even(l):
    return [n for n in l if n % 2 == 0]

LIST24 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_even(LIST24))