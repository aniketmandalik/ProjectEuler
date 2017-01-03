from timeit import default_timer as timer

def integer_right_triangles(n):
	max_solutions = 0
	max_solutions_p = 0
	for i in range(3, n + 1):
		num_solutions = 0
		for c in range(1, int(i/2 + 1)):
			for a in range(1, c):
				b = i - a - c
				if pow(c, 2) == pow(a, 2) + pow(b, 2):
					num_solutions += 1
		if num_solutions > max_solutions:
			max_solutions = num_solutions
			max_solutions_p = i
	return max_solutions_p

start = timer()
print(integer_right_triangles(1000))
end = timer()
print("Time: ", end - start)