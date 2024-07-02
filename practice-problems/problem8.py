# practice problem 8
'''
Make a function to convert all Fahrenheit temperatures in a list to Celsius
To convert from fahrenheit -> celsius: subtract by 30 then divide by 2

Example usage:
print(fahrenToCel([32, 68, 100]))
Output: [1.0, 19.0, 35.0]

'''

# Write your code here




































# Solution
'''
from typing import List

def fahrenToCelc(ftemp: List[float]) -> List[float]:
    return [(temp - 30) / 2 for temp in ftemp]

# OR

def fahrenToCelc(ftemp: List[float]) -> List[float]:
    for temp in ftemp:
        return (ftemp - 30) / 2
'''