from timeit import default_timer as timer
from MathStuff import prime_factorize, find_next_prime

def totient_maximum(n):
	max_ratio = 2
	max_num = 2
	num = 2
	next_factor = 3
	while num * next_factor < n:
		# print(num)
		# a = set(prime_factorize(num))
		# relative_primes = 0
		# for i in range(1, num):
		# 	b = set(prime_factorize(i))
		# 	if len(a & b) == 0:
		# 		relative_primes += 1
		# ratio = num / relative_primes
		# if ratio > max_ratio:
		# 	max_ratio = ratio
		# 	max_num = num
		num *= next_factor
		next_factor = find_next_prime(next_factor)
		# print(ratio)
	return num

start = timer()
print(totient_maximum(1000000))
end = timer()
print("Time: ", end - start)