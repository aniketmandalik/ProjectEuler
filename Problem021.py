from timeit import default_timer as timer
from MathStuff import find_divisors

def amicable_numbers(n):
	"""
	Finds all amicable numbers under n, where the sum of the proper divisors of a
	is equal to b, and vice-versa.
	"""
	total = 0
	for a in range(2, n):
		b = sum(find_divisors(a))
		c = sum(find_divisors(b))
		if c == a and a != b:
			total += a
	return total

start = timer()
print(amicable_numbers(10000))
end = timer()
print("Time: ", end - start)