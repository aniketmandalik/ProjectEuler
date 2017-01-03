from timeit import default_timer as timer

from MathStuff import find_next_odd_composite, find_primes
from math import sqrt

def goldbach_other_conjecture():
	cand_composite = find_next_odd_composite(33)
	prime_list = find_primes(cand_composite)
	prev = 33
	while True:
		found_combo = False
		for p in prime_list:
			a = (cand_composite - p)/2
			if sqrt(a) == int(sqrt(a)):
				found_combo = True
				break
		if found_combo == False:
			return cand_composite
		prev = cand_composite
		cand_composite = find_next_odd_composite(cand_composite)
		prime_list += range(prev + 2, cand_composite)
	return cand_composite

start = timer()
print(goldbach_other_conjecture())
end = timer()
print("Time: ", end - start)