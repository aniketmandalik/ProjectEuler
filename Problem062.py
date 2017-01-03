from timeit import default_timer as timer
from MathStuff import permutations, get_number, digits

def cubic_permutations(n):
	i = 0
	while True:
		num = i**3
		a = digits(num)
		lst_cubes = permutations(a)
		lst_cubes = map(get_number, lst_cubes)
		counter = 0
		for j in lst_cubes:
			if j**(1/3) == int(j**(1/3)):
				counter += 1
		if counter == n:
			return num
		print(i)
		i += 1

def is_cube(n):
	if n**(1/3) == int(n**(1/3)):
		return True
	return False

start = timer()
# print(cubic_permutations(2))
end = timer()
print("Time: ", end - start)