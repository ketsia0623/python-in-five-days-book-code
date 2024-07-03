import array
 
# Creating an array of integers 
my_array = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements 
print(my_array[0]) 

# Modifying elements 
my_array[1] = 20 
print(my_array) 	

# Appending elements 
my_array.append(6) 
print(my_array)   

# Removing elements 
my_array.remove(20) 
print(my_array)  

# numpy arrays
# install numpy if not already installed by typing this command on terminal: pip install numpy

import numpy as np

# creating a numPy array
my_array = np.array([2, 4, 6, 8])

# accessing elements
print(my_array[2])

# modifying elements
my_array[0] = 10
print(my_array)	

# appending elements, creates a new array
my_array = np.append(my_array, 20)	
print(my_array)		

#removing elements, creates a new array
my_array = np.delete(my_array, 0)	
print(my_array)		