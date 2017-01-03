from timeit import default_timer as timer

from MathStuff import digits

def digit_cancelling_functions():
	all_fracs = []
	for i in range(11, 100):
		for j in range(i + 1, 100):
			a = digits(i)
			b = digits(j)
			if (0 not in a) and (0 not in b) and a[0] != b[0] and a[1] != b[1]:
				if a[1] == b[0]:
					print(a)
					print(b)
					print(a.pop(1), b.pop(0))
				elif a[0] == b[1]:
					print(a)
					print(b)
					print(a.pop(0), b.pop(1))
				else:
					break
				if i * b[0] == j * a[0]:
					all_fracs.append((i, j))
	print(all_fracs)

digit_cancelling_functions()