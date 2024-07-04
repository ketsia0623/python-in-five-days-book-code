import json 

# Python object 
data = {  'name': 'Alice', 
          'age': 30, 'city': 
          'New York' } 

# Serialization: Python object to JSON string 
jsonString= json.dumps(data) 
print(jsonString) 

# Deserialization: JSON string to Python object 
parsedData = json.loads(jsonString) 
print(parsedData) 

# Writing JSON to a file 
with open('data.json', 'w') as file: 
    json.dump(data, file) 

# Reading JSON from a file 
with open('data.json', 'r') as file: 
    file_data = json.load(file) 
print(file_data) 