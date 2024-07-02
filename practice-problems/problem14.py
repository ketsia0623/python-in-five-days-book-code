# practice problem 14
'''
Create a function that consumes a list of integers and makes a new list with each number added to the previous number

Example usage:
print(previousAdded([12, 8, 4]))  
Output: [16, 20, 12]
'''

# Write your code here












































# Solution

'''
def previousAdded(ints: List[int]) -> List[int]:     
    new_list = []

    num = len(ints)

    for i in range(num):
        new_list.append(ints[i] + ints[i-1])
    return new_list
'''

