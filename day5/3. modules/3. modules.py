# math module
import math 

# Basic mathematical operations 
print(math.sqrt(16)) 		
print(math.pow(2, 3))	

# Trigonometric functions 
print(math.sin(math.pi / 2)) 

# random module
import random 

# Generating random numbers 
print(random.randint(1, 10))  
print(random.random()) 	     

# Shuffling a list 
my_list = [1, 2, 3, 4, 5] 
random.shuffle(my_list) 
print(my_list) 	

# datetime module
from datetime import datetime, timedelta 

# Current date and time 
now = datetime.now() 
print(now) 

# Date arithmetic 
tmr = now + timedelta(days=1) 
print(tmr) 

# Formatting dates 
formattedDate = now.strftime('%Y-%m-%d %H:%M:%S') 
print(formattedDate) 

# Parsing dates 
parsedDate = datetime.strptime('2023-06-11', '%Y-%m-%d') 
print(parsedDate)

# time module
import time 

# Current time in seconds since the Epoch(the epoch is the point where the time starts, the return value of time.gmtime(0)) 
current_time = time.time() 
print(current_time)

# Sleep for 2 seconds 
time.sleep(2) 

# Measure time interval 
start_time = time.time() 
# Some code execution 
end_time = time.time() 
print(f"Elapsed time: {end_time - start_time} seconds") 

'''
import os 

# Get the current working directory 
current_directory = os.getcwd() 
print(current_directory) 			# Output: /home/user (example) 

# List files in a directory 
files = os.listdir('.') 
print(files) 					# Output: ['file1.txt', 'file2.txt', 'directory'] 

# Create a directory 
os.mkdir('new_directory') 

# Remove a file 
os.remove('file1.txt') 

# Get environment variables 
path = os.environ.get('PATH') 
print(path) # Output: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin (example)
'''

'''
import json 

# Python object 
data = {  'name': 'Alice', 
          'age': 30, 'city': 
          'New York' } 

# Serialization: Python object to JSON string 
jsonString= json.dumps(data) 
print(jsonString) # Output: {"name": "Alice", "age": 30, "city": "New York"} 

# Deserialization: JSON string to Python object 
parsedData = json.loads(json_string) 
print(parsedData) # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'} 

# Writing JSON to a file 
with open('data.json', 'w') as file: 
json.dump(data, file) 

# Reading JSON from a file 
with open('data.json', 'r') as file: 
file_data = json.load(file) 
print(file_data) 			# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

'''
