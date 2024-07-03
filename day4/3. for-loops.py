'''
basic syntax:
    for item in sequence:	
        code to be executed
'''

# iterating over a list
colors = ["green", "purple", "yellow", "red", "white"]
for color in colors:
    print(color)


# iterating voer a string
for letter in "Apple":
    print(letter)	


# iterating over a dict
my_dict = {
    "artist": "van Gogh",
    "painting": "the starry night",
    "year": 1889,
    "color": "black"
}
for value, key in my_dict.items():
    print (value, key)	


# break statement
colors = ["green", "purple", "yellow", "red", "white"]
# the break statement comes after the print; will print with red
for color in colors:
    print(color)
    if color == "red":
        break			


# the break statement comes before the print; will print without red
for color in colors: 
    if color == "red":
        break
    print(color)


# the continue statement
colors = ["green", "purple", "yellow", "red", "white"]
for color in colors:
    if color == "purple":
        continue
    print(color)


# the range() function
for i in range(5):
    print(i)	


# range() function with range of values
for i in range(4, 8):
    print(i)		


# else staement in for loop
for i in range(5):
    print(i)
else: 
    print("Looping is finished")


# pass statement
for i in [8, 6, 4, 2]:
    pass


# nested for loops
colors = ["green", "purple", "yellow", "red", "white"]
objects = ["ball", "bottle"]
for color in colors:
    for object in objects:
        print(color, object)

# SIMPLIER VERSION with less lines
for color in ["green", "purple", "yellow", "red", "white"]:
    for obj in ["ball", "chair", "bottle"]:
        print(color, obj)