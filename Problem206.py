from timeit import default_timer as timer
from math import sqrt
from MathStuff import digits

def concealed_square():
	bottom_num = int(sqrt(1020304050607080900))
	top_num = int(sqrt(1929394959697989990)) + 2
	while bottom_num % 10 != 0:
		bottom_num += 1
	while top_num % 10 != 0:
		top_num += 1
	print(bottom_num)
	print(top_num)
	for i in range(int(bottom_num/10) - 7, int(top_num/10) + 3, 10):
		num = i**2
		print(num)
		a = digits(num)[::2]
		k = 1
		match = True
		for i in a:
			if i != k:
				match = False
				break
			k += 1
		if match == True:
			return num


start = timer()
print(concealed_square())
end = timer()
print("Time: ", end - start)