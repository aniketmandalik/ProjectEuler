from timeit import default_timer as timer
from functools import reduce
from MathStuff import digits

def champernownes_constant():
	num_digits = 0
	check_digits = [1, 10, 100, 1000, 10000, 100000, 1000000]
	i = 1
	all_digits = []
	while len(all_digits) <= check_digits[-1]:
		all_digits += digits(i)
		i += 1
	to_mul = []
	for x in check_digits:
		to_mul += [all_digits[x - 1]]
	return reduce((lambda x, y: x * y), to_mul)

start = timer()
print(champernownes_constant())
end = timer()
print("Time: ", end - start)