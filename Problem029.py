from timeit import default_timer as timer

def distinct_powers(a, b):
	all_numbers = set({})
	for i in range(2, a + 1):
		for j in range(2, b + 1):
			all_numbers.add(pow(i, j))
	return len(all_numbers)

start = timer()
print(distinct_powers(100, 100))
end = timer()
print("Time: ", end - start)