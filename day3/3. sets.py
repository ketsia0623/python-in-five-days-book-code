my_set = {"red", "white", "purple", "black"}
print(my_set)

my_set = {1, "purple", False, "pineapple", 0, True}
print(my_set) 

# len() function
my_set = {"purple", 8, False, "pineapple", 0, True}
print(len(my_set))	

# data type composition of sets
car_set = {2000, "maybach", "red", False}
print(car_set)

# adding new items
my_set = {"red", "white", "purple", "black"}
my_set.add("yellow")
print(my_set)

# adding another collection to a set
my_set = {"red", "white", "purple", "black"}
newColors = {"green", "navy"}
my_set.update(newColors)
print(my_set)

# removing an item
my_set = {"red", "white", "purple", "black"}
my_set.remove("red")
print(my_set)

# discard() method
my_set = {"red", "white", "purple", "black"}
my_set.discard("red")
print(my_set)

# pop() method
my_set = {"red", "white", "purple", "black"}
color = my_set.pop()
print(color)			
print(my_set)		

# clear() and del methods
my_set = {"red", "white", "purple", "black"}
'''
my_set.clear()
del my_set
'''