from timeit import default_timer as timer
from MathStuff import digits, get_number

def lychrel_numbers(n):
	total = 0
	for i in range(n):
		num = i
		lychrel = True
		for _ in range(50):
			new_num = num + get_number(digits(num)[::-1])
			a = digits(new_num)
			if a == a[::-1]:
				lychrel = False
				break
			num = new_num
		if lychrel:
			total += 1
	return total

start = timer()
print(lychrel_numbers(10000))
end = timer()
print("Time: ", end - start)