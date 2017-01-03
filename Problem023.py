from timeit import default_timer as timer
from MathStuff import find_divisors

from math import sqrt
def non_abundant_sums(a):
	abundant_numbers = []
	abundant_numbers_range = set()
	for i in range(12, a - 11):
		if sum(find_divisors(i)) > i:
			abundant_numbers += [i]
	for i in abundant_numbers:
		for j in abundant_numbers:
			abundant_numbers_range.add(i + j)
	abundant_numbers_total = 0
	for i in range(1, a + 1):
		if i not in abundant_numbers_range:
			abundant_numbers_total += i
	return abundant_numbers_total

start = timer()
print(non_abundant_sums(20161))
end = timer()
print("Time: ", end - start)