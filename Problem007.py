from timeit import default_timer as timer

def prime_number(n):
	"""
	Finds the nth prime number.
	"""
	prime_list = [2]
	prime_candidate = 3
	while len(prime_list) < n:
		is_prime = True
		for i in prime_list:
			if i**2 > prime_candidate:
				break
			if prime_candidate % i == 0:
				is_prime = False
				break
		if is_prime == True:
			prime_list.append(prime_candidate)
		prime_candidate += 2
	return prime_list[-1]

start = timer()
print(prime_number(10001))
end = timer()
print("Time: ", end - start)