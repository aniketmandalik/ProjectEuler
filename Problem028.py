from timeit import default_timer as timer

def spiral(n):
	total = 1
	diag = 1
	spiral_number = 1
	to_add = 2
	while spiral_number < n:
		spiral_number += 2
		for i in range(0, 4):
			diag += to_add
			total += diag
		to_add += 2
	return total

start = timer()
print(spiral(1001))
end = timer()
print("Time: ", end - start)