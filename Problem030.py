from timeit import default_timer as timer
from MathStuff import digits

def digit_powers(n):
	can_be_represented = 0
	for i in range(2, n * pow(9, n)):
		all_digits = digits(i)
		total = 0
		for d in all_digits:
			total += pow(d, n)
		if total == i:
			can_be_represented += total
	return can_be_represented

start = timer()
print (digit_powers(5))
end = timer()
print("Time: ", end - start)