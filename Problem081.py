from timeit import default_timer as timer

def path_total(file_name, a, b):
	with open(file_name) as f:
		content = f.readlines()
		for i in range(len(content)):
			content[i] = content[i][:-1]
			content[i] = content[i].split(",")
	rows = len(content)
	cols = len(content[0])
	for i in range(rows):
		for j in range(cols):
			content[i][j] = int(content[i][j])
	pos_row, pos_col, total = a, b, content[a][b]
	a = {find_path(content, pos_row, pos_col, rows, cols, total)}

def find_path():
	pass

start = timer()
print(path_total("p081_matrix.txt", 0, 0))
end = timer()
print("Time: ", end - start)