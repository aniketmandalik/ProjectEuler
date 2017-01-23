from timeit import default_timer as timer
from math import sqrt

def coded_triangle_numbers(file_name):
	name_list = []
	num_words = 0
	with open(file_name) as f:
		content = str(f.readlines())
		name_list = content[3:-3].split('","')
	for name in name_list:
		word_score = 0
		for letter in name:
			word_score += ord(letter) - (ord('A') - 1)
		if is_triangle_number(word_score):
			num_words += 1
	return num_words

def is_triangle_number(a):
	i = 0
	total = 0
	while total < a:
		total += i
		i += 1
	if total == a:
		return True
	return False

start = timer()
print(coded_triangle_numbers("p042_words.txt"))
end = timer()
print("Time: ", end - start)