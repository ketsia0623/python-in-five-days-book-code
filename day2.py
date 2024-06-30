# ** Our first print statement! **
print("Hello World!")


# ** Concept of indentation **
if 1 != 0: 
    print("1 doesn't equal 0")


# ** Comments in Python **
# this is a single line comment, it won't be executed when the code runs
print("Hello World")		# this is also a single-line comment

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


# ** Scope **
# local scope
def myFunction(): 
    localVar = "I am local" 
    print(localVar) 
myFunction()
# print(localVar)       # causes an error, since variable is only accessible inside the function

# global scope
global_var = "I am global" 
def my_function(): 
    print(global_var) 

my_function() 	
print(global_var) 	


# ** Variables **
# variable assignment
x = 10
variable = "you"
print(x)
print(variable)

# data type assignment to a variable
x = str(10) 
print(x)    
x = int(10) 
print(x) 
x = float(10) 
print(x)

# conventions
# camel case
myVariable = 1

# snake case
my_variable = 1

# pascal case 
MyVariable = 1


# ** Python datatypes **
y = "Hello World!"					             # str
print(y, "\n")
y = 10							                 # int
print(y, "\n")
y = 15.5						                 # float
print(y, "\n")
y = False						                 # bool
print(y, "\n")
y = ["pizza", "berries"]				         # list
print(y, "\n")
y = ("mango", "orange")				             # tuple
print(y, "\n")
y = {"fruit" : "mango", "type" : "sweet"}	     # dict
print(y, "\n")
y = {"apple", "berry", "mango"}			         # set
print(y, "\n")
y = None	                                     # NoneType
print(y, "\n")


# ** Escape characters **
# newline
print("Hello\nWorld!")

# tab
print("Hello\tWorld!")

# backslash
print("This is a backslash: \\")

# single quotes
print('It\'s a beautiful day!')

# double quotes
print("She said, \"Hello!\"") 

# raw strings
print(r"This is a raw string with a backslash: \\")

# ** integers ***
a = 12
b = -4
c = 0


# ** floats **
a = 12.5
b = -2.74
c = 2.2e2
d = 0.0

# converting from float to int
x = 5.5
y = 4

# float -> integer
a = int(y)

# integer -> float
b = float(x)

print(a)
print(b)

# **Casting**
# to integers:
a = int(4)		
b = int(4.2)	   
c = int("8")		

# to floats:
a = float(6)		
b = float(3.2)	
c = float("3.2")	
d = float("8")	

# to strings:
a = str(4)		
b = str(2.0)		
c = str("word")	


# ** Python Booleans **
# assigning a boolean value to a variable
is_active = True 
print(is_active, "\n")
is_logged_in = False
print(is_logged_in, "\n")

# returning a boolean value
print(8 == 6)					
print(4 > 0)	

# using the bool() function
print(bool(10))				
print(bool("well"))	

# truthy & falsy
print(bool(0))				    
print(bool(False))				    
print(bool("hello"))		    
print(bool(None))


# ** Strings **
# different string quote types
single_quote_string = 'Hello World!'  
print(single_quote_string)
double_quote_string = "Hello World!"
print(double_quote_string)
triple_quote_string = """Also known as 
as a multi-line string. """
print(triple_quote_string)

# example string
x = "Hello World!"
print(x[0])

# len()
x = "Hello World!"
print(len(x))	

# slicing string
x = "Hello World!"
print(x[6:12])

x = "Hello World!"
# gets all characters from start until the index 6(not including 6)
print(x[:7])		
# gets all characters from index 4 until the end of the string
print(x[4:])	

# negative indexing
x = "Hello World!"
# goes to the last index but does not include it(to do so just do: [-8:])
print(x[-8:-1])

# string concatenation, + operator
str1 = "Hello" 
str2 = "World" 
both_strs = str1 + " " + str2 
print(both_strs)

# '', += operator
str1 = "Hello" 
str1 += " World" 
print(str1) 

# '', join() method
str_list = ["Hello", "World"] 
result = " ".join(str_list) 
print(result) 

# '', str.format() method
str1 = "Hello" 
str2 = "World" 
result = "{} {}".format(str1, str2) 
print(result) 

# '', f-strings
str1 = "Hello" 
str2 = "World" 
result = f"{str1} {str2}" 
print(result)

# string methods
print("hello world".capitalize())    			
print("helloworld".endswith("orld")) 			
print("helloworld".startswith("hello"))			
print("helloworld".index("llo"))				 # returns the index of the first character's substring
print("HELLOworld".isupper())				
print("helloworld".islower())				
print("hello world".title())				
print("hELLO wORLD".lower())				
print("Hello World".upper())				
print(" hello world ".strip())				
print("1hello2world".isdigit())		

# string formatting
# using modulo
name = "Cassie"
age = 24
formattedS = "Name: %s, Age: %d" % (name, age)
print(formattedS)

# str.format() method
name = "Cassie"
age = 24
formattedS = "Name: {}, Age: {}".format(name, age) 
print(formattedS) 

# using positional and keyword arguments
name = "Cassie"
age = 24
formattedS = "Name: {0}, Age: {1}".format(name, age) 
print(formattedS) 			
formatted_string = "Name: {name}, Age: {age}".format(name="Cassie", age=24) 
print(formattedS) 

# formatting numbers
num = 684.9842 
formattedS = "Number: {:.2f}".format(num) 
print(formattedS) 		# Output: Number: 684.98

# f-strings
name = "Cassie"
age = 24
formattedS = f"Name: {name}, Age: {age}" 
print(formattedS) 

# formatting numbers using f-strings
number = 684.9842 
formattedS = f"Number: {number:.2f}"
print(formattedS) 

# using expressions with f-strings
name = "Cassie"
age = 24
formattedS = f"In five years, {name} will be {age + 5}."
print(formattedS)

# ** User Input **
fave = input("What is your favorite color: ")
print("Your favorite color is: " + fave)

# converting input to another datatype
age = input("Please enter your age: ")
age = int(age)
print("You are " + str(age) + "years old.")

# split()
info = input("Enter your name and age seperated by a space: ")
name, age = info.split()
print("Name: ", name)
print("Age:", age)

# hadnling invalid input
while True:
	try: 
		age = int(input("Enter your age: "))
		break
	except ValueError:
		print("You have entered an invalid input. Please enter a valid integer")

print("You are " + str(age) + " years old.")


# ** Error handling **
# try ... except
try:
    fave = int(input("Enter your favorite number:"))
    ans = 10 / fave
except ValueError as err:
	print("Not a valid number")
except ZeroDivisionError as err:
	print("You can't divide by zero")
else:
	print(f"Result is {ans}")
finally: 
	print("Calculation completed")
	
# raising exceptions
def checkPositive(number):
	if number <= 0:
		raise ValueError("Number must be positive.")
	return number

try: 
    num = int(input("Enter a positive number: "))
    checkPositive(num)
except ValueError as e:
    print("Error: ", e)

# custom exceptions
class customError(Exception):
	"""My own custom exception class"""
	pass
def trickyFunction(): 
	raise customError("Custom error message")
try:
	trickyFunction()
except customError as e:
	print("Caught a custom exception: ", e)
	
