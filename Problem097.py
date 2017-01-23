from timeit import default_timer as timer
from MathStuff import digits, get_number, prime_factorize

def non_mersenne_prime():
	num1 = 28433*2**7830457 + 1
	i = 0
	while 2**i < 7830457


start = timer()
print(non_mersenne_prime())
end = timer()
print("Time: ", end - start)