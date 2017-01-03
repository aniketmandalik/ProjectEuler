from timeit import default_timer as timer

def fibonacci_sum(n, d):
	"""
	Finds the sum of all fibonacci numbers less than n
	that are divisible by d
	"""
	x, y, sum = 1, 1, 0
	while x + y < n:
		x, y = y, x + y
		if y % d == 0:
			sum += y
	return sum

start = timer()
print(fibonacci_sum(4000000, 2))
end = timer()
print("Time: ", end - start)