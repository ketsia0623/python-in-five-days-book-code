# if statement
x = 500
y = 220
if x > y:
   print("x is greater than y")


# elif
x = 500
y = 220
if x == y:
   print("x is equal to y")
elif x > y:
   print("x is greater than y")


# else
x = 500
y = 220
if x == y:
   print("x is equal to y")
elif x < y:
   print("x is less than y")
else:
   print("x is greater than y")


# if an else on only one line
x = 500
y = 220
if y < x: print("y is less than x")

print("x") if x < y else print("y")


# using logical operators to combine conditional statements
x = 500
y = 220
z = 150
if x > y and y > z:					        # and keyword
    print("Both conditions are True!")
if x > y or y < z:					        # or keyword
    print("One or more of the conditions are True!")
if not y < z:
    print("z is not less than y!")		    # not keyword


# nested if statements
a = 50

if a > 100: 
    print("greater than 100!")
    if a > 50:
        print(" also greater than 50!")
else:
    print("50 or less!")


# the pass statement
x = 20
y = 35

if x < y: 
    pass