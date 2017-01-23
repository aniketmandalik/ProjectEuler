from timeit import default_timer as timer
from functools import lru_cache
memoize = lru_cache(1000)

@memoize
def counting_summations(n, m):
	if n == 0:
		return 1
	if n < 0:
		return 0
	if m == 1:
		return 1
	return counting_summations(n - m, m) + counting_summations(n, m - 1)

start = timer()
print(counting_summations(100, 99))
end = timer()
print("Time: ", end - start)