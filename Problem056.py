from timeit import default_timer as timer
from MathStuff import digits

def powerful_digit_sum(n):
	max_sum = 0
	for i in range(n, 0, -1):
		for j in range(n, 0, -1):
			a = sum(digits(i**j))
			if a > max_sum:
				max_sum = a
				print(i, j)
	return max_sum

start = timer()
print(powerful_digit_sum(100))
end = timer()
print("Time: ", end - start)