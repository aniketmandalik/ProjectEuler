from timeit import default_timer as timer

from MathStuff import digits

def pandigital_products():
	all_nums = []
	for i in range(1, 1000):
		for j in range(1, 1000):
			a = digits(i)
			b = digits(j)
			if (0 not in a and 0 not in b) and len(list(set(a) & set(b))) == 0:
				num = i * j
				c = digits(num)
				if (0 not in c) and len(list(set(a) | set(b) | set(c))) == len(a + b + c) and len(a + b + c) == 9:
					all_nums.append(num)
					print(i)
					print(j)
					print(num)
	return sum(set(all_nums))

print(pandigital_products())