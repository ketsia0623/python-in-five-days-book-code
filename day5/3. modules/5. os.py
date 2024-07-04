# be careful when running these commands, as they may lead to unexpected changes in your files

import os 

# Get the current working directory 
current_directory = os.getcwd() 
print(current_directory) 			

# List files in a directory 
files = os.listdir('.') 
print(files) 					

# Create a directory 
os.mkdir('new_directory') 

# Remove a file 
os.remove('file1.txt') 

# Get environment variables 
path = os.environ.get('PATH') 
print(path)