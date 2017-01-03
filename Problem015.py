from timeit import default_timer as timer

from functools import lru_cache
memoize = lru_cache(1000)

@memoize
def lattice_paths(l, w):
	"""
	Find the number of paths available to go from the top left to the bottom right
	corner of an l * w grid, where you can only move right or down.
	"""
	if l + w == 0:
		return 0
	if l == 0 or w == 0:
		return 1
	if l == 1:
		return w + 1
	if w == 1:
		return l + 1
	return lattice_paths(l - 1, w) + lattice_paths(l, w - 1)

start = timer()
print(lattice_paths(20, 20))
end = timer()
print("Time: ", end - start)