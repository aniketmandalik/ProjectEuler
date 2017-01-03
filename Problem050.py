from timeit import default_timer as timer
from MathStuff import find_primes

def consecutive_prime_sum(n):
	a = find_primes(n)
	max_primes = 0
	prime = 0
	min_num = 0
	for i in range(len(a) - 1, max_primes, -1):
		if a[i] < min_num:
			break
		for j in range(i - max_primes):
			prime_sum = 0
			k = 0
			while prime_sum + a[j + k] <= a[i]:
				prime_sum += a[j + k]
				k += 1
			if prime_sum == a[i] and k > max_primes:
				max_primes = k
				prime = prime_sum
				min_num = sum(a[:k])
	return max_primes, prime

start = timer()
print(consecutive_prime_sum(1000000))
end = timer()
print("Time: ", end - start)