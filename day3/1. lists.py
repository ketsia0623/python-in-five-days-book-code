# sample list
my_list = ["blue", "green", "purple", "red"]
print(my_list)

# len() function
my_list = ["blue", "green", "purple", "red"]
print(len(my_list))			

# data types of lists
mylist1 = ["red", "green"]
print(mylist1)

mylist2 = [4, 2, 8, 6]
print(mylist2)

mylist3 = [False, True]
print(mylist3)

mylist4 = [18, False, "this", 2]
print(mylist4)

# accessing list items with index number
my_list = ["blue", "green", "purple", "red"]
print(my_list[0])

# negative indexing
my_list = ["blue", "green", "purple", "red"]
print(my_list[-3])	

# range of indexes
# both parts of the range is sepcified
my_list = ["blue", "green", "black", "purple", "red", "white"]
print(my_list[1:4])		

# specifying the start index(will return from specified start index until the last index)
my_list = ["blue", "green", "black", "purple", "red", "white"]
print(my_list[4:]) 		

# specifying the end index(returns the first index until(before) the specified end index)
my_list = ["blue", "green", "black", "purple", "red", "white"]
print(my_list[:3])	

# range of negative indexes
# both parts of the range is sepcified
my_list = ["blue", "green", "black", "purple", "red", "white"]
print(my_list[-5:-1])	

# specifying the start index(will return from specified start index until the last index)
my_list = ["blue", "green", "black", "purple", "red", "white"]
print(my_list[-3:])

# specifying the end index(returns the first index until the specified end index)
my_list = ["blue", "green", "black", "purple", "red", "white"]
print(my_list[:-4])	

# the in keyword
my_list = ["blue", "green", "black", "purple", "red", "white"]
print("red" in my_list)		    
print("orange" in my_list)	

# changing a list value by referring to index number
my_list = ["blue", "green", "black", "purple", "red", "white"]
my_list[2] = "navy"		
print(my_list)

# changing a range of list values
my_list = ["blue", "green", "black", "purple", "red", "white"]
my_list[2:4] = ["navy", "violet"]	     
print(my_list)

# inserting items
my_list = ["blue", "green", "black", "purple", "red", "white"]
my_list.insert(0, "navy")		     
print(my_list)	 

# list methods
mylist = [2, 4, 6, 8]

mylist.append(10)		
print(mylist)

print(mylist.count(4))

mylist.extend([12, 14, 16])	
print(mylist)

print(mylist.index(12))		

mylist.pop(2)				
print(mylist)

mylist.remove(2)			
print(mylist)

mylist.reverse()			
print(mylist)

mylist.sort()			
print(mylist)

print(mylist.copy())

'''
mylist.clear()
'''
print(mylist)