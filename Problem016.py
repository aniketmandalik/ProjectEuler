from timeit import default_timer as timer
from MathStuff import digits

def power_digit_sum(number, power):
	"""
	Returns the sum of all the digits of the exponent number ^ power
	"""
	a = digits(number**power)
	return sum(a)

start = timer()
print(power_digit_sum(2, 1000))
end = timer()
print("Time: ", end - start)