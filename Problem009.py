from timeit import default_timer as timer

def pythagorean_triplet(total):
	"""
	Finds a pythagorean triplet a, b, and c such that a + b + c = sum
	Returns i * j * k
	"""
	for i in range(1, int(total/2)):
		for j in range(1, total - i):
			k = 1000 - i - j
			if k**2 == i**2 + j**2:
				return i * j * k

start = timer()
print(pythagorean_triplet(1000))
end = timer()
print("Time: ", end - start)