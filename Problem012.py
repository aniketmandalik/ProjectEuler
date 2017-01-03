from timeit import default_timer as timer
from MathStuff import prime_factorize, count_elem
from math import sqrt
def divisible_triangle_number(n):
	"""
	Returns the first triangular number to have more than n factors.
	"""
	divisible_by_five_hundred_numbers = False
	next_num = 2
	candidate = 1
	total = 1
	while not divisible_by_five_hundred_numbers:
		candidate += next_num
		next_num += 1
		num_factors = 0
		p_factors = prime_factorize(candidate)
		factors = dict(zip(p_factors, [count_elem(n, p_factors) + 1 for n in p_factors]))
		num_factors = 1
		for p in factors:
			num_factors *= factors[p]
		if num_factors >= 500:
			divisible_by_five_hundred_numbers = True
	return candidate

start = timer()
print(divisible_triangle_number(500))
end = timer()
print("Time: ", end - start)