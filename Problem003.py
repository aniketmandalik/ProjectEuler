from timeit import default_timer as timer
from MathStuff import prime_factorize

def largest_prime_factor(n):
	"""
	Finds the largest prime factor of n.
	"""
	return prime_factorize(n)[-1]

start = timer()
print(largest_prime_factor(600851475143))
end = timer()
print("Time: ", end - start)