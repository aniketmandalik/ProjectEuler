from timeit import default_timer as timer
from MathStuff import digits, counter

def permuted_multiples(n):
	i = 1
	n_pow = 1
	while True:
		a = counter(digits(i))
		checks = [0] * (n - 1)
		for j in range(2, n + 1):
			if counter(digits(i*j)) == a:
				checks[j - 2] = 1
			else:
				break
		if min(checks) == 1:
			return i
		if 6 * i > pow(10, n_pow):
			n_pow += 1
			i = pow(10, n_pow - 1)
		i += 1

start = timer()
print(permuted_multiples(6))
end = timer()
print("Time: ", end - start)