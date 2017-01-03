from timeit import default_timer as timer
from MathStuff import digits
from math import log2

def non_mersenne_prime():
	num1 = 28433
	a = log2(7830457)
	b = a - 22
	a = int(a)
	num2 = 2.0
	for _ in range(a):
		num2 **= 2
	num2 **= b
	num = num1 * num2 + 1
	return num

start = timer()
print(non_mersenne_prime())
end = timer()
print("Time: ", end - start)