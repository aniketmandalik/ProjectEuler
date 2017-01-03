from timeit import default_timer as timer

from MathStuff import is_triangular, is_pentagonal

def triangular_pentagonal_hexagonal():
	i = 143
	result = 0
	while True:
		i += 1
		hex_num = i * (2 * i - 1)
		if is_triangular(hex_num) and is_pentagonal(hex_num):
			result = hex_num
			break
	return result

start = timer()
print(triangular_pentagonal_hexagonal())
end = timer()
print("Time: ", end - start)