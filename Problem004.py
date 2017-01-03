from timeit import default_timer as timer
from MathStuff import digits

def largest_palindrome(n):
	"""
	Returns the largest palindrome found by multiplying together
	n-digit numbers.
	"""
	biggest_palindrome = 0
	for i in range(pow(10, n) - 1, pow(10, n-1) - 1, -1):
		for j in range(i, pow(10, n-1) - 1, -1):
			candidate_palindrome = i * j
			if candidate_palindrome < biggest_palindrome:
				break
			a = digits(candidate_palindrome)
			if a == a[::-1] and candidate_palindrome > biggest_palindrome:
				biggest_palindrome = candidate_palindrome
	return biggest_palindrome

start = timer()
print (largest_palindrome(3))
end = timer()
print("Time: ", end - start)