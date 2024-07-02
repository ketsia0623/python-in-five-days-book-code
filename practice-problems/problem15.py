# practice problem 15
'''
Create a program that will generate a multiplication table for a number that the user has entered

Example usage:
number = int(input("Enter a number: "))
multiplication_table(number)

If input is 5, output will be:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''

# Write your code here








































# Solution

'''
def multiTable(num):
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

number = int(input("Enter a number: "))
multiTable(number)
'''