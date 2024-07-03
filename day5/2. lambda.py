a = lambda x, y: x + y
print(a(4, 8))

# doubling our function
def double(num):
	return lambda x: x * num

doubled = double(2)
print(doubled(13))	