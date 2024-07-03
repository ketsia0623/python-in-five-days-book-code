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