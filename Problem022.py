from timeit import default_timer as timer

def names_scores(file_name):
	name_list = []
	with open(file_name) as f:
		content = str(f.readlines())
		name_list = content[3:-3].split('","')
	name_list.sort()
	total_score = 0
	for i in range(len(name_list)):
		word_score = 0
		for char in name_list[i]:
			word_score += ord(char) - (ord('A') - 1)
		total_score += word_score * (i + 1)
	return total_score

start = timer()
print(names_scores("names.txt"))
end = timer()
print("Time: ", end - start)