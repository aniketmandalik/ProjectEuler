from timeit import default_timer as timer
from MathStuff import binary_form

def double_base_palindromes(n):
	total = 0
	for i in range(0, n):
		if check_palindrome(i):
			if check_palindrome(binary_form(i)):
				total += i
	return total

def check_palindrome(n):
	if type(n) == list:
		return n == n[::-1]
	return str(n) == str(n)[::-1]

start = timer()
print(double_base_palindromes(1000000))
end = timer()
print("Time: ", end - start)