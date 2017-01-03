from timeit import default_timer as timer

from math import factorial

def lexicographic_permutations(ints, n):
	"""
	[0, 1, 2]
	[0, permutations(1, 2)]
	[1, permutations(0, 2)]
	[2, permutations(0, 1)]
	"""
	if len(ints) == 1:
		return ints
	else:
		fraction = (n - 1) / factorial(len(ints))
		for i in range(0, len(ints)):
			if (i / len(ints)) <= fraction and ((i + 1) / len(ints)) > fraction:
				return [ints.pop(i)] + lexicographic_permutations(ints, n - (factorial(len(ints)) * i))

start = timer()
print(lexicographic_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000))
end = timer()
print("Time: ", end - start)