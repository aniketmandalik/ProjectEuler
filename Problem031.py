from timeit import default_timer as timer

def coin_sums(n):
	coin_list = [200, 100, 50, 20, 10, 5, 2, 1]
	return find_coins(coin_list, n)

def find_coins(coin_list, n):
	if n <= 1 or len(coin_list) <= 1:
		return 1
	else:
		if coin_list[0] > n:
			return find_coins(coin_list[1:], n)
		else:
			return find_coins(coin_list[1:], n) + find_coins(coin_list, n - coin_list[0])

	
start = timer()
print(coin_sums(200))
end = timer()
print("Time: ", end - start)