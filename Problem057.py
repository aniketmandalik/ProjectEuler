from timeit import default_timer as timer
from MathStuff import digits

def converging_square_root(n):
	i = 1
	num = 3
	den = 2
	result = 0
	while i <= 1000:
		if len(digits(num)) > len(digits(den)):
			result += 1
		num, den = num+(2 * den), num+den
		i += 1
	return result

start = timer()
print(converging_square_root(1000))
end = timer()
print("Time: ", end - start)