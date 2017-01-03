from timeit import default_timer as timer

def largest_grid_product(n, file_name):
	"""
	Taking a .txt file full of numbers with 2 digits, returns the product
	of n adjacent digits where the product is the highest
	of any other n adjacent digits in the file (horizontal, diagonal, or vertical).
	"""
	number_grid = []
	with open(file_name) as f:
		content = f.readlines()
		for row in content:
			row_clean = row[: -1].split()
			row_toInt = [int(elem) for elem in row_clean]
			number_grid.append(row_toInt)
	print(number_grid)
	max_product = 0
	candidate_product = 1
	count = 0
	height = len(number_grid)
	width = len(number_grid[0])
	for row in range(height):
		for col in range(width - n):
			candidate_product = 1
			for i in range(n):
				candidate_product *= number_grid[row][col + i]
			if candidate_product > max_product:
				max_product = candidate_product
	for row in range(height - n):
		for col in range(width):
			candidate_product = 1
			for i in range(n):
				candidate_product *= number_grid[row + i][col]
			if candidate_product > max_product:
				max_product = candidate_product
	for row in range(height - n):
		for col in range(width - n):		
			candidate_product = 1
			for i in range(n):
				candidate_product *= number_grid[row + i][col + i]
			if candidate_product > max_product:
				max_product = candidate_product
	for row in range(n, height):
		for col in range(width - n):		
			candidate_product = 1
			for i in range(n):
				candidate_product *= number_grid[row - i][col + i]
			if candidate_product > max_product:
				max_product = candidate_product
	return max_product

start = timer()
print(largest_grid_product(4, "NumberFile2.txt"))
end = timer()
print("Time: ", end - start)