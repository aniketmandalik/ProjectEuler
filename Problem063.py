from timeit import default_timer as timer
from MathStuff import digits

def powerful_digit_counts():
	total_nums = 0
	for i in range(1, 10):
		j = 1
		while len(digits(i**j)) == j:
			total_nums += 1
			j += 1
	return total_nums


start = timer()
print(powerful_digit_counts())
end = timer()
print("Time: ", end - start)