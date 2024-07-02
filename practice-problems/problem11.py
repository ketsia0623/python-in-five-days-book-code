# practice problem 11

'''
Given 2 lists of integers, add each number at each index together and return a new list of integers

Example usage:
print(addLists([1, 2, 3], [4, 5, 6]))  
Output: [5, 7, 9]
'''

# Write your code here









































# Solution
'''
from typing import List

def addLists(list1: List[int], list2: List[int]) -> List[int]:
    new_list = []
    for index in range(len(list1)):
        num3 = list1[index] + list2[index]
        new_list.append(num3)
    print(new_list)

# OR   

def addLists(list1: List[int], list2: List[int]):
    return [x + y for x, y in zip(list1, list2)]

'''

