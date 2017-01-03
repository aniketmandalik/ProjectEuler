from timeit import default_timer as timer

from MathStuff import prime_factorize

def distinct_prime_factors(a):
	i = 647
	while True:
		checks = [0] * a
		to_add = 1
		for j in range(0, a):
			if len(set(prime_factorize(i + j))) == 4:
				checks[j] = 1
			else:
				to_add += j
				break
		if min(checks) == 1:
			return i
		else:
			i += to_add


start = timer()
print(distinct_prime_factors(4))
end = timer()
print("Time: ", end - start)