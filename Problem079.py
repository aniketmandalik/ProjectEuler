from timeit import default_timer as timer
from MathStuff import digits

def passcode_derivation(file_name):
	with open(file_name) as f:
		content = f.readlines()
		content = list(set(map(lambda i: int(i[:-1]), content)))
		content.sort()
	for i in range(len(content)):
		content[i] = digits(content[i])
	num_count_place = {}
	for j in range(3):
		for i in content:
			try:
				num_count_place[(i[j], j)] += 1
			except KeyError:
				num_count_place[(i[j], j)] = 1
	answer_string = ""
	first_characters = []
	second_characters = []
	third_characters = []
	for i, j in num_count_place.keys():
		if j == 0:
			first_characters += [[i, num_count_place[(i, j)]]]
		if j == 1:
			second_characters += [[i, num_count_place[(i, j)]]]
		if j == 2:
			third_characters += [[i, num_count_place[(i, j)]]]
	first_characters.sort(key=lambda i: i[1])
	second_characters.sort(key=lambda i: i[1])
	third_characters.sort(key=lambda i: -i[1])
	print(first_characters)
	print(second_characters)
	print(third_characters)

start = timer()
print(passcode_derivation("p079_keylog.txt"))
end = timer()
print("Time: ", end - start)