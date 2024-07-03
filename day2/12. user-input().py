fave = input("What is your favorite color: ")
print(f"Your favorite color is: {fave}")


# converting input to another datatype
age = input("Please enter your age: ")
age = int(age)
print("You are " + str(age) + "years old.")


# split()
info = input("Enter your name and age seperated by a space: ")
name, age = info.split()
print("Name: ", name)
print("Age:", age)


# handling invalid input
while True:
	try: 
		age = int(input("Enter your age: "))
		break
	except ValueError:
		print("You have entered an invalid input. Please enter a valid integer")

print("You are " + str(age) + " years old.")