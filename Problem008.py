from timeit import default_timer as timer

def largest_product(n, file_name):
	"""
	Taking a .txt file full of numbers, returns the product
	of n adjacent digits where the product is the highest
	of any other n adjacent digits in the file.
	"""
	with open(file_name) as f:
		content = f.readlines()
	number_string = "0"
	for i in content:
		number_string += i
	number_list = []
	for i in number_string:
		if i.isdigit():
			number_list.append(int(i))
	i = 0
	highest_product = 0
	candidate_product = 1
	while i < len(number_list) - n:
		for j in range(i, i + n):
			candidate_product *= number_list[j]
			if candidate_product == 0:
				break
		if candidate_product > highest_product:
			highest_product = candidate_product
		candidate_product = 1
		i += 1
	print (highest_product)

start = timer()
largest_product(13, "NumberFile.txt")
end = timer()
print("Time: ", end - start)