from timeit import default_timer as timer

from MathStuff import digits

def self_powers(n):
	a = 0
	for i in range(1, n + 1):
		a += pow(i, i)
	a = str(a)
	return a[-10:]

print(self_powers(1000))