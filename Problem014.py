from timeit import default_timer as timer
from math import log2

def collatz_sequence_length(n):
	"""
	Finds the length of all Collatz sequences starting with numbers less than n
	"""
	longest_sequence, number = 0, 1
	for i in range(1, n):
		j, candidate_sequence = i, 0
		while j != 1:
			if j % 2 == 0:
				j /= 2
				candidate_sequence += 1
			else:
				j = (3 * j + 1) / 2
				candidate_sequence += 2
		if candidate_sequence > longest_sequence:
			longest_sequence, number = candidate_sequence, i
	return number

start = timer()
print(collatz_sequence_length(1000000))
end = timer()
print("Time: ", end - start)