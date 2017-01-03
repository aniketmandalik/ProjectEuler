from timeit import default_timer as timer

def digit_fibonacci_number(n):
	index = 1
	a, b = 1, 1
	while len(str(a)) < n:
		a, b = b, a + b
		index += 1
	return index

start = timer()
print(digit_fibonacci_number(1000))
end = timer()
print("Time: ", end - start)