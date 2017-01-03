from timeit import default_timer as timer

def multiple_sum(x, y, n):
	"""
	Finds the sum of all numbers between m inclusive and n exclusive
	that are divisible by x and y.
	"""
	total = 0
	for i in range(x, n):
		if i % x == 0 or i % y == 0:
			total += i
	return total

start = timer()
print(multiple_sum(3, 5, 1000))
end = timer()
print("Time: ", end - start)