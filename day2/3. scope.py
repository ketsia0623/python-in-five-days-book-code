# local scope
def myFunction(): 
    localVar = "I am local" 
    print(localVar) 
myFunction()
# print(localVar)       # causes an error, since variable is only accessible inside the function


# global scope
global_var = "I am global" 
def my_function(): 
    print(global_var) 

my_function() 	
print(global_var) 