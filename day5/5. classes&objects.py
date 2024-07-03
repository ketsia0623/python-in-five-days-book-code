# creating a class
class myClass:
	a = 10

# instance of a class
my_instance = myClass("an instance attribute")

# __init__ basic syntax
class myClass:
	def __init__(self, parameter):
		self.attribute = parameter

# __init__ example
class Student:
	def __init__(self, name, classification):
		self.name = name
		self.classification = classification
	def display_students(self):
		print(f"Name: {self.name}, Age: {self.age}")
# instance of the class:
student01 = Student("Christie", 30) 

# the self parameter
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def getAge(self):
		return self.age
	
# __str__ function
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return f"Person(name={self.name}, age={self.age})"
	
# object methods
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def birthday(self):
		self.age += 1
		return f"Happy Birthday {self.name}! You're {self.age} now!"   

# instance:
person1 = Person("Lia", 14)

# calling object methods:
print(person1.birthday())

# the pass statement
class Person:
    pass