def myfunction():
    print("Hello World")
myfunction()	


# returning a value
def myfunction(num): 
    return num * 4
print(myfunction(6))


# pass statement 
def myfunction():
    pass


# function arguments
def myfunction(firstname, lastname):
    print("Hello, " + firstname + " " + lastname)
myfunction("Sia", "Don")


# default arguments
def myfunction(firstname="John", lastname="Doe"):
    print("Hello, " + firstname + " " + lastname)
myfunction()
myfunction("Sia", "Don")


# args
def myfunction(*friends):
    print("My second-oldest friend is " + friends[1])
myfunction("Laina", "Faith", "Liv")


# positional arguments
def hello(name, age):
	print(f"Hello, I am {name}, and I'm {age} years old")
hello("Heather", 21)


# keyword arguments
def hello(name, age):
	print(f"Hello, I am {name}, and I'm {age} years old")
hello(age=21, name="Heather")


# arbitrary arguments, *args
def hello(*friends):
	for friend in friends:
		print(f"Hello {friend}!")
hello("Lance", "Rielle", "Lala", "James")


# keyword arbitrary arguments, **kwargs
def hello(**friend):
	print(f"Hello, {friend['name']}! You are {friend['age']} years old")
hello(name="James", age= 24)