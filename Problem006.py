from timeit import default_timer as timer

def sum_square_difference(n):
	"""
	Finds the difference between the square of the sum of
	natural numbers 1 to n inclusive and and sum of the squares
	of natural numbers 1 to n inclusive.
	"""
	square_sum, sum_square = 0, 0
	for i in range(1, n + 1):
		square_sum += pow(i, 2)
	for i in range(1, n + 1):
		sum_square += i
	sum_square = pow(sum_square, 2)
	return sum_square - square_sum

start = timer()
print(sum_square_difference(100))
end = timer()
print("Time: ", end - start)