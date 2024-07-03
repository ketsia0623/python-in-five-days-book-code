# basic inheritance example
class Device:
	def __init__(self, name):
		self.name = name
	
	def size(self):
		pass

class Laptop(Device):
	def size(self):
		return f'A {self.name} has a size of ~14"'
class Phone(Device):
	def size(self):
		return f'A {self.name} has a size of ~6.5"'

# creating instances
laptop = Laptop("HP Envy")
my_phone = Phone("Iphone")

print(laptop.size())
print(my_phone.size())

# overriding class methods
class Device:
	def __init__(self, name):
		self.name = name
	def size(self):
		return f"A {self.name} has a size"
class Phone(Device):
	def size(self):
		return f'A {self.name} has a size of ~6.5"'
my_phone = Phone("Iphone")
print(my_phone.size())

# super() function
class Device:
	def __init__(self, name):
		self.name = name
	def size(self):
		return f"A {self.name} has a size"

class Phone(Device):
	def __init__(self, name, company):
		super().__init__(name)	
		self.company = company

	def size(self):
		return f'A {self.name}, from {self.company}, has a size of ~6.5"'  
my_phone = Phone("Iphone", "Apple") 
print(my_phone.size())

# multiple inheritance
class Tablet:
	def touchscreen(self):
		return "Is touchscreen"

class Laptop:
	def large(self):
		return "Is large"
class twoinOne(Tablet, Laptop):
	pass
hpEnvy = twoinOne()
print(hpEnvy.touchscreen())
print(hpEnvy.large())

# isinstance() and issubclass()
class Device:
	pass

class Laptop(Device):
	pass

laptop = Laptop()
print(isinstance(laptop, Laptop))
print(isinstance(laptop, Device))
print(issubclass(Laptop, Device))
print(issubclass(Device, Laptop))
