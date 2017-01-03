from timeit import default_timer as timer

from math import factorial
def digit_factorial():
	total, i, num = 0, 3, 0
	while num < 2:
		a = i
		num_digits, digits = len(str(i)), []
		for _ in range(0, num_digits):
			digits.append(a % 10)
			a //= 10
		if i - sum([factorial(j) for j in digits]) == 0:
			total += i
			num += 1
		i += 1
	return total

start = timer()
print(digit_factorial())
end = timer()
print("Time: ", end - start)
