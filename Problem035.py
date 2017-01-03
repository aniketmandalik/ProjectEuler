from timeit import default_timer as timer
from MathStuff import find_primes
from math import sqrt

def is_circular_prime(n):
	num_digits, digits = len(str(n)), []
	for _ in range(0, num_digits):
		digits.insert(0, n % 10)
		n //= 10
	for _ in range(num_digits):
		digits, new_num = shift(digits), 0
		for i in range(num_digits):
			new_num += (pow(10, i) * digits[num_digits - 1 - i])
		if not is_prime(new_num):
			return False
		new_num = 0
	return True

def shift(lst):
	return lst[1:] + [lst[0]]

def circular_primes(n):
	num_circular_primes = 0
	a = find_primes(n)
	for i in a:
		if is_circular_prime(i):
			num_circular_primes += 1
	return num_circular_primes

start = timer()
print(circular_primes(1000000))
end = timer()
print("Time: ", end - start)