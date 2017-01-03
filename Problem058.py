from timeit import default_timer as timer
from MathStuff import is_prime

def spiral_primes(n):
	side_length = 3
	diag_list = [1, 3, 5, 7, 9]
	a = [3, 5, 7]
	while True:
		for _ in range(4):
			diag_list.append(diag_list[-1] + side_length + 1)
		a += filter(lambda x: True if is_prime(x) else False, diag_list[-4:])
		side_length += 2
		if len(a) / len(diag_list) < n:
			return side_length

start = timer()
print(spiral_primes(.1))
end = timer()
print("Time: ", end - start)