from timeit import default_timer as timer
from MathStuff import find_primes, prime_factorize, count_elem

def smallest_multiple(n):
    """
    Returns the smallest number perfectly divisible by 1 through n inclusive.
    """
    all_primes = find_primes(n + 1)
    common_multiples = dict(zip(all_primes, [1]*len(all_primes)))
    for i in range(2, n + 1):
        a = prime_factorize(i)
        for j in a:
            count = count_elem(j, a)
            if count > common_multiples[j]:
                common_multiples[j] = count
    total = 1
    for i in common_multiples:
        total *= pow(i, common_multiples[i])
    return total

start = timer()
print(smallest_multiple(20))
end = timer()
print("Time: ", end - start)