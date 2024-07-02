# this is a single line comment, it won't be executed when the code runs
print("Hello World")

# This is a multi-line comment 
# that spans multiple lines  
# Each line starts with a hash (#)  
print("Hello, World!")

""" 
This is a multi-line comment using triple quotes.
Often used for docstrings, 
which describes the functionality of a piece of code  
""" 
print("Hello, World!")

def add(a, b): 
    """ This function adds two numbers and returns the result 

    Parameters: 
    a (int or float): The first number 
    b (int or float): The second number 

    Returns: int or float: The sum of a and b. 
    """ 
    return a + b 
print(add.__doc__)