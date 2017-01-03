from timeit import default_timer as timer
from MathStuff import find_primes

def sum_prime(n):
	"""
	Returns the sum of all primes below n.
	"""
	prime_list = find_primes(n)
	return sum(prime_list)

start = timer()
print(sum_prime(2000000))
end = timer()
print("Time: ", end - start)