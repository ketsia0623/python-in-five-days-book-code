# practice problem 9

'''
Write a program that calculates and prints the factorial of a given number

Example usage:
print(factorial(5))  
Output: 120
'''

# Write your code here









































# Solution

'''
def factorial(num: int):
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

'''