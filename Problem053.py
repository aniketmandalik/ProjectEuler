from timeit import default_timer as timer
from math import factorial

def combinatoric_selections(n, a):
	total = 0
	for i in range(1, n + 1):
		for j in range(1, i + 1):
			options = factorial(i)/factorial(j)/(factorial(i - j))
			if options > a:
				total += 1
	return total

start = timer()
print(combinatoric_selections(100, 1000000))
end = timer()
print("Time: ", end - start)