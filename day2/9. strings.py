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


# string concatenation, += operator
str1 = "Hello" 
str1 += " World" 
print(str1) 


# string concatenation, join() method
str_list = ["Hello", "World"] 
result = " ".join(str_list) 
print(result) 

# string concatenation, str.format() method
str1 = "Hello" 
str2 = "World" 
result = "{} {}".format(str1, str2) 
print(result) 

# string concatenation, f-strings
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
print(formattedS) 		

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