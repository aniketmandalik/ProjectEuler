from timeit import default_timer as timer
from MathStuff import digits
from math import log2

def square_digit_chains(n):
	i = 1
	ends_at_one = {1}
	ends_at_eighty_nine = {85, 89, 145, 42, 20, 4, 16, 37, 58}
	num_eighty_nine = 0
	number_path = []
	while i < n:
		a = i
		while a not in ends_at_one and a not in ends_at_eighty_nine:
			number_path += [a]
			a = sum(list(map(lambda x: x**2, digits(a))))
		if a in ends_at_one:
			while number_path:
				ends_at_one.add(number_path.pop())
		if a in ends_at_eighty_nine:
			num_eighty_nine += 1
			while number_path:
				ends_at_eighty_nine.add(number_path.pop())
		i += 1
	return num_eighty_nine

start = timer()
print(square_digit_chains(10000000))
end = timer()
print("Time: ", end - start)