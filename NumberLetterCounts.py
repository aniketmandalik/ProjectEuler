from timeit import default_timer as timer

def number_letter_counts(n):
	"""
	Returns the sum of the number of letters used to write all numbers
	from 1 to N, which is up to 1000, inclusive.
	"""
	str_sum = 0
	for i in range(1, n + 1):
		n, digit_list = i, []
		while n:
			digit_list.insert(0, n%10)
			n //= 10
		print(digit_list)
		if len(digit_list) == 1:
			for i in digit_list:
				if i == 1 or i == 2 or i == 6 or i == 10:
					str_sum += 3
				if i == 4 or i == 5 or i == 9:
					str_sum += 4
				if i == 3 or i == 7 or i == 8:
					str_sum += 5
		else:
			if digit_list[-2] == 1:
				
			


number_letter_counts(1000)