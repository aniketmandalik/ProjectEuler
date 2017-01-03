from timeit import default_timer as timer

from MathStuff import find_primes

def consecutive_prime_sum(n):
	prime_list = find_primes(1000000)
	sequence_found = False
	for i in range(len(prime_list), 21, -1):
		for j in range()