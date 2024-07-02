# practice problem 6
'''
Swap the first and last values in a list

Example usage:
print(swapFL(["hey", 2, 4, 8])) 
Output: [8, 2, 4, "hey"]
'''

# Write your code here






































# Solution

'''
from typing import List

def swapFL(values: List):
    if len(values) > 1:
        values[0], values[-1] = values[-1], values[0]
    return values

'''

