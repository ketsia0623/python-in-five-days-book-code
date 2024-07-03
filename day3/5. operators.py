# arithmetic operators
a = 12
b = 4

print(a + b)			# Addition (+) 

print(a - b)			# Substraction {-}

print(a * b)			# Multiplication {*}

print(a / b)			# Division {/}

print(a % b)			# Modulus {%}: remainder of a / b

print(a ** b)			# Exponentation {**}: a to the power of y

print(a // b)           # Floor division {//}: rounds answer to nearest whole #
	

# assignment operators
a = 12
b = 4

a = b				        # a = b
print(a, b)

a = 12
a += b				        # also:  a = a + b
print(a)

a = 12
a -= b      				# also:  a = a - b 
print(a)

a = 12	
a *= b      				# also:  a = a * b
print(a)

a = 12
a /= b				        # also:  a = a / b
print(a)

a = 12
a %= b				        # also:  a = a % b
print(a)

a = 12
a //= b			            # also:  a = a // b
print(a)

a = 12
a **= b			            # also:  a = a ** b
print(a)

# comparison operators
a = 12
b = 4

print(a == b)				# Equal (==)

print(a != b)				# Not equal (!=)

print(a > b)				# Greater than (>)

print(a < b)				# Less than (<)

print(a >= b)				# Greater than or equal to (>=)

print(a <= b)				# Less than or equal to (<=)


# logical operators
a = 12

print(a > 4 and a < 8)	
print(a > 4 or a > 2)	
print(not (a > 4 or a < 2))


# identity operators
a = 12
b = 4

print(a is b)		
print(a is not b)

# membership operators
a = 12
b = (4, 8, "twelve", 2, 0)

print(a in b)		
print(a not in b)