from timeit import default_timer as timer

from math import sqrt
from MathStuff import is_pentagonal

def pentagon_numbers():
	i = 1
	min_diff = 0
	while True:
		num = i * (3 * i - 1) / 2
		for j in range(i - 1, 0, -1):
			comp_num = j * (3 * j - 1) / 2
			if is_pentagonal(num - comp_num) and is_pentagonal(num + comp_num):
				min_diff = num - comp_num
				break
		if min_diff != 0:
			break
		i += 1
	return int(min_diff)

start = timer()
print(pentagon_numbers())
end = timer()
print("Time: ", end - start)