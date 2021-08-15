import math as m

def countPrimes(n: int) -> int:
    if n < 2:
        return 0

    prime = 2
    sieve = [*range(0, n, 1)]

    primes = 0

    while prime < n:
        primes += 1
        for i in range(0, n, prime):
            sieve[i] = None
        while prime < n and sieve[prime] is None:
            prime += 1

    return primes


