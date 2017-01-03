from timeit import default_timer as timer
from MathStuff import digits

def factorial_digit_sum(n):
	"""
	Finds the sum of all the individual digits in n factorial.
	"""
	factorial = 1
	for i in range(n, 1, -1):
		factorial *= i
	a = digits(factorial)
	return sum(a)

start = timer()
print(factorial_digit_sum(100))
end = timer()
print("Time: ", end - start)