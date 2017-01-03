from math import sqrt, log2
from timeit import default_timer as timer

def is_prime(n):
	if n == 2:
		return True
	if n < 2 or n % 2 == 0:
		return False
	for i in range(3, int(sqrt(n)//1) + 2, 2):
		if n % i == 0:
			return False
	return True

# def find_primes(n):
# 	start = timer()
# 	prime_list = [2]
# 	prime_candidate = 3
# 	while prime_candidate < n:
# 		is_prime = True
# 		for i in prime_list[1:]:
# 			if i**2 > prime_candidate:
# 				break
# 			if prime_candidate % i == 0:
# 				is_prime = False
# 				break
# 		if is_prime:
# 			prime_list.append(prime_candidate)
# 		prime_candidate += 2
# 	end = timer()
# 	print("Time: ", end - start)
# 	# return prime_list

def find_primes(n):
	prime_list = []
	prime_candidates = list(range(2, n))
	while prime_candidates[0]**2 < n:
		i = prime_candidates.pop(0)
		prime_list += [i]
		prime_candidates = list(filter(lambda a: True if a % i != 0 else False, prime_candidates))
	prime_list += prime_candidates
	return prime_list

# def find_primes_3(n):
# 	prime_list = [2, 3, 5]
# 	prime_dict = dict(zip(list(range(5, n)), [False] * (n - 1)))
# 	a_list = [1, 13, 17, 29, 37, 41, 49, 53]
# 	b_list = [7, 19, 31, 43]
# 	c_list = [11, 23, 47, 59]
# 	for i in candidate_primes:
# 		r = i % 60
# 		if r in a_list:
# 			for j in range(1, int(sqrt((n - 1)/4)) + 2):
# 				for k in range(1, sqrt(n - 4 * j**2)):
# 					flip = 4 * j**2 + k**2
# 					if flip <= n:
# 						prime_dict[flip] = not(prime_dict[flip])
# 		if r in b_list:
# 			for j in range(1, int(sqrt((n - 1)/3)) + 2):
# 				for k in range(1, sqrt(n - 4 * j**2)):
# 					flip = 4 * j**2 + k**2
# 					if flip <= n:
# 						prime_dict[flip] = not(prime_dict[flip])
# 		if r in c_list:

def find_divisors(n):
	divisors = [1]
	for i in range(2, int(pow(n, .5)//1) + 1):
		if n % i == 0:
			divisors += [i]
			if n // i != i:
				divisors += [n // i]
	return divisors

# def find_sum_divisors(n):
# 	total = 1
# 	for i in range(2, int(pow(n, .5)//1) + 1):
# 		if n % i == 0:
# 			total += i
# 			if n // i != i:
# 				total += n // i
# 	return total

def find_next_prime(n):
	i = 0
	if n % 2 == 1:
		i = n + 2
	else:
		i = n + 1
	while True:
		if is_prime(i):
			return i
		i += 2

def prime_factorize(a):
	factor_list = []
	while a % 2 == 0:
		factor_list.append(2)
		a /= 2
	i = 3
	while a != 1:
		while a % i == 0:
			factor_list.append(i)
			a /= i
		i += 2
	return factor_list

def find_odd_composites(n):
	composite_list = []
	for i in range(3, n, 2):
		if not (is_prime(i)):
			composite_list.append(i)
	return composite_list

def find_next_odd_composite(n):
	i = 0
	if n % 2 == 1:
		i = n + 2
	else:
		i = n + 1
	while True:
		if not (is_prime(i)):
			return i
		i += 2

def digits(n):
	num_digits, digits = len(str(n)), []
	for _ in range(0, num_digits):
		digits.insert(0, n % 10)
		n //= 10
	return digits

def count_elem(n, lst):
	count = 0
	for i in lst:
		if i == n:
			count += 1
	return count

def counter(lst):
	elems = {}
	for i in lst:
		try:
			elems[i] += 1
		except KeyError:
			elems[i] = 1
	return elems

def factorial(n):
	total = 1
	for i in range(1, n + 1):
		total *= 1
	return total

def is_ascending(lst):
	prev = lst[0]
	for i in lst[1:]:
		if i <= prev:
			return False
	return True

def is_descending(lst):
	prev = lst[0]
	for i in lst[1:]:
		if i >= prev:
			return False
	return True

def is_non_descending(lst):
	prev = lst[0]
	for i in lst[1:]:
		if i < prev:
			return False
	return True

def is_non_ascending(lst):
	prev = lst[0]
	for i in lst[1:]:
		if i < prev:
			return False
	return True

def get_number(lst):
	new_lst = lst[::-1]
	total = 0
	exp = 0
	for i in new_lst:
		total += (i * pow(10, exp))
		exp += 1
	return total

def binary_form(n, binary = []):
	if binary == []:
		if n == 0:
			return [0]
		if n == 1:
			return [1]
		i = int(log2(n))
		return binary_form(n - 2**i, [1] + [0] * i)
	if n == 0:
		return binary
	i = int(log2(n))
	a = binary
	a[-(i + 1)] = 1
	return binary_form(n - 2**i, a)

def decimal_form(lst):
	new_lst = lst[::-1]
	total = 0
	exp = 0
	for i in new_lst:
		total += (i * pow(2, exp))
		exp += 1
	return total

def permutations(lst):
    if not lst:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            for j in permutations(lst[:i] + lst[i+1:]):
                yield [lst[i]] + list(j)

def is_triangular(a):
	inv = (sqrt(8 * a + 1) - 1)/2
	if inv == int(inv):
		return True
	return False

def is_pentagonal(a):
	inv = (sqrt(24 * a + 1) + 1)/6
	if inv == int(inv):
		return True
	return False

def is_hexagonal(a):
	inv = (sqrt(24 * a + 1) + 1)/4
	if inv == int(inv):
		return True
	return False