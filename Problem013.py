from timeit import default_timer as timer

from math import log
def large_sum(n, file_name):
	"""
	Taking a .txt file full of numbers one line long, returns the first
	N digits of the sum
	"""
	number_list = []
	with open(file_name) as f:
		content = f.readlines()
		for row in content:
			row_clean = int(row)
			number_list.append(row_clean)
	total = sum(number_list)
	return total

start = timer()
print(large_sum(10, "NumberFile3.txt"))
end = timer()
print("Time: ", end - start)