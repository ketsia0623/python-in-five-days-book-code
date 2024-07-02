# practice probem 13
'''
Make a function to return only positive numbers in a list

Example usage:
print(positive_numbers([-1, 2, -3, 4]))  
Output: [2, 4]
'''

# Write your code here












































# Solution

'''
from typing import List

def positive_numbers(int_list):
    return [num for num in int_list if num > 0]

# OR

def onlyPositives(ints: List[int]) -> List[int]:
    positives = []
    for num in ints:
        if num > 0:
            positives.append(num)
    return positives

'''
