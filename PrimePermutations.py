from timeit import default_timer as timer

from MathStuff import find_primes, digits

def prime_permutations():
	prime_list = find_primes(1000, 10000)
	prime_digits = list(map(lambda x : digits(x), prime_list))
	prime_4_digits = list(filter(lambda x: True if len(set(x)) == 4 else False, prime_digits))
	same_digits = []
	for i in prime_4_digits:
		to_add = [prime_4_digits.pop(prime_4_digits.index(i))]
		for j in prime_4_digits:
			if set(i) == set(j):
				to_add.append(prime_4_digits.pop(prime_4_digits.index(j)))
		same_digits.append(to_add)
	for i in same_digits:
		

prime_permutations()