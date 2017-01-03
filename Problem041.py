from timeit import default_timer as timer

from MathStuff import is_prime, get_number, digits, permutations

def pandigital_prime():
	largest_prime = 0
	for i in range(5, 10):
		a = permutations(list(range(1, i + 1)))
		a = [lst for lst in a if could_be_prime(lst)]
		for num in a:
			cand_num = get_number(num)
			if is_prime(cand_num) and largest_prime < cand_num:
				largest_prime = cand_num
	return largest_prime

def could_be_prime(lst):
	if lst[len(lst) - 1] % 2 == 1 and lst[len(lst) - 1] != 5:
		return True
	return False

start = timer()
print(pandigital_prime())
end = timer()
print("Time: ", end - start)