from timeit import default_timer as timer
from MathStuff import is_prime, binary_form
from copy import deepcopy

def XOR_decryption(file_name):
	num_list = []
	best_key = []
	test_words = ['the', 'be', 'and', 'of', 'in', 'to', 'have', 'it', 'that', 'for', 'you', 'he']
	best_num_words = 0
	with open(file_name) as f:
		content = str(f.readlines())
		num_list = content[2:-2].split(',')
		# print(num_list)
		num_list = [int(i) for i in num_list]
		# print(num_list)
		# num_list = map(lambda x: binary_form(x), num_list)
		# num_list = [[0] * (8 - len(i)) + i for i in num_list]
		print(num_list)
	for i in range(ord('a'), ord('z') + 1):
		i_shift = binary_form(i)
		i_shift = [0] * (8 - len(i_shift)) + i_shift
		for j in range(ord('a'), ord('z') + 1):
			j_shift = binary_form(j)
			j_shift = [0] * (8 - len(j_shift)) + j_shift
			for k in range(ord('a'), ord('z') + 1):
				k_shift = binary_form(k)
				k_shift = [0] * (8 - len(k_shift)) + k_shift
				test_lst = []
				for i in num_list:
					test_lst.append(i[:])
				print(test_lst)



start = timer()
print(XOR_decryption("p059_cipher.txt"))
end = timer()
print("Time: ", end - start)