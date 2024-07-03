myList = [2, 4, 6, 8] 
myIterator = iter(myList) 
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

# our own iterator
class MyIterator: 
	def __init__(self, start, end): 
		self.current = start 			# keep track of current iteration
		self.end = end 

	def __iter__(self): return self 
	def __next__(self): 
		if self.current > self.end: 
			raise StopIteration 
		else: 
			self.current += 1 
			return self.current - 1 
		
# Using the custom iterator 
my_iter = MyIterator(1, 5) 
for value in my_iter: 
	print(value)