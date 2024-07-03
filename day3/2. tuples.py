# tuple example
mytuple = ("blue", "red", "white", "purple")
print(mytuple)

# len() function on tuples
mytuple = ("blue", "red", "white", "purple")
print(len(mytuple))

# tuple with 1 value
mytuple = ("black",)
print(type(mytuple))

# data types in tuples
tuple1 = ("red", "white", "yellow")
print(tuple1)

tuple2 = (False, True)
print(tuple1)

tuple3 = (4, 6, 2, 8, 6)
print(tuple1)

tuple4 = (5.3, "car", 4, False, 8)
print(tuple1)

# tuple methods
mytuple = ("blue", "red", "white", "purple", "black", "red")
print(mytuple.count("red"))	
print(mytuple.index("red"))

# accessing tuple items
mytuple = ("blue", "red", "white", "purple", "black", "red")
print(mytuple[4])

# joining 2 tuples
first_tuple = ("apple", "pineapple", "cantaloupe")
second_tuple = ("green", "yellow", "orange")
entire_tuple = first_tuple + second_tuple 
print(entire_tuple)