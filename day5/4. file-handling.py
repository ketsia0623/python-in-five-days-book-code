# **File handling **
# opening a file
#new_file = open(filename, mode)

# reading from a file
file = open("samplepython.txt", "r")
contents = file.read()
print(contents)
file.close()

# writing to a file
file = open("samplepython.txt", "w")
file.write("Hello World")
file.close()

# with() statement
# to read
with open("samplepython.txt", "r") as file:
	contents = file.read()
	print(contents)
# to write
with open("samplepython.txt", "w") as file:
	file.write("Hello world")

# deleting a file
import os
os.remove("samplepython.txt")
