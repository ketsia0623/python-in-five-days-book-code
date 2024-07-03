# dict example
my_dict = {
    "artist": "van Gogh",
    "painting": "the starry night",
    "year": 1889
}
print(my_dict) 

# accessing dict items by using key name
my_dict = {
    "artist": "van Gogh",
    "painting": "the starry night",
    "year": 1889
}
print(my_dict["year"])

# datatypes in dicts
my_dict = {
    "artist": "van Gogh",					
    "oil painting": True,					
    "painting": "the starry night",		
    "year": 1889,				
    "colors": ["blue, yellow, white, black"]	
}

# deleting dict values
my_dict.pop("oil painting")
del my_dict["colors"]

# the get() method
my_dict = {
    "artist": "van Gogh",
    "painting": "the starry night",
    "year": 1889
}
x = my_dict.get("artist")	

# getting all dictionary keys
x = my_dict.keys()		
print(x)

# getting all the dictionary values
x = my_dict.values()	
print(x)

# getting all the dictionary items
x = my_dict.items()
print(x)

# in keyword
my_dict = {
    "artist": "van Gogh",
    "painting": "the starry night",
    "year": 1889
}
if "painting" in my_dict:
    print("Yes it is!")
print("painting" in my_dict)

# chaning a value by referring to its key
my_dict = {
    "artist": "van Gogh",
    "painting": "the starry night",
    "year": 1889
}
my_dict["year"] = 1890
print(my_dict["year"])

# update() method
my_dict = {
    "artist": "van Gogh",
    "painting": "the starry night",
    "year": 1889
}
my_dict.update({"year": 1900})

# new index key
my_dict = {
    "artist": "van Gogh",
    "painting": "the starry night",
    "year": 1889
}
my_dict["color"] = "black"