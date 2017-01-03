from timeit import default_timer as timer

from MathStuff import permutations, get_number

def sub_string_divisbility():
	total = 0
	a = permutations(list(range(0, 10)))
	for i in a:
		if (fits_criteria(i)):
			total += get_number(i)
	return total

def fits_criteria(lst):
	if lst[0] == 0:
		return False
	primes = [2, 3, 5, 7, 11, 13, 17]
	for i in range(1, 8):
		j = get_number(lst[i: i + 3])
		if j % primes[i - 1] != 0:
			return False
	return True

start = timer()
print(sub_string_divisbility())
end = timer()
print("Time: ", end - start)