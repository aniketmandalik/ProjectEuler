from timeit import default_timer as timer
from MathStuff import find_primes

def quadratic_primes(a, b):
	primes = find_primes(100^2 + 1000 * 100 + 1000)
	max_primes = 0
	for i in range(-a + 1, a):
		for j in range(0, b + 1):
			num_primes = 0
			n = 0
			while (n**2 + i * n + j) in primes:
				num_primes += 1
				n += 1
			if num_primes > max_primes:
				max_primes = num_primes
				prime_set = [i, j]
	return prime_set[0] * prime_set[1]

start = timer()
print(quadratic_primes(1000, 1000))
end = timer()
print("Time: ", end - start)