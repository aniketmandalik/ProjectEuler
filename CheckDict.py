from timeit import default_timer as timer

def check_dict(file_name):
	with open(file_name) as f:
		content = str(f.read())
	a = eval(content)
	print(a)

start = timer()
check_dict("NAS-GOOG1.txt")
end = timer()
print(end - start)