from timeit import default_timer as timer

from MathStuff import is_prime, digits, find_next_prime

def truncatable_primes():
	num_truncatable_primes, total = 0, 0
	i = 11
	while num_truncatable_primes < 11:
		if is_truncatable_prime(i):
			total += i
			num_truncatable_primes += 1
		i = find_next_prime(i)
	return total

def is_truncatable_prime(n):
	num_length, all_digits = len(str(n)), digits(n)
	new_digits = all_digits[:]
	for i in range(0, num_length - 1):
		new_digits = new_digits[1:]
		num = 0
		for j in range(0, len(new_digits)):
			num += (pow(10, j) * new_digits[len(new_digits) - 1 - j])
		if not is_prime(num):
			return False
		num = 0
	new_digits = all_digits[:]
	for i in range(0, num_length - 1):
		new_digits = new_digits[:-1]
		num = 0
		for j in range(0, len(new_digits)):
			num += (pow(10, j) * new_digits[len(new_digits) - 1 - j])
		if not is_prime(num):
			return False
		num = 0
	return True

start = timer()
print(truncatable_primes())
end = timer()
print("Time: ", end - start)