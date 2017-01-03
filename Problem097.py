from timeit import default_timer as timer
from MathStuff import digits

def non_mersenne_prime():
	return digits(28433*(2**7830457)+1)[-10:]

start = timer()
print(non_mersenne_prime())
end = timer()
print("Time: ", end - start)