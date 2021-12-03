import math


def primesUpTo(n):  # Sieve of Eratosthenes
    primes = []
    for i in range(2, n+1):
        primes.append(True)
    for i in range(2, math.ceil(n**0.5)):
        if primes[i-2]:
            k = 0
            while (i**2 + k*i) <= n:
                primes[i**2 + k*i - 2] = False
                k += 1
    realPrimes = []
    for i in range(0, len(primes)):
        if primes[i]:
            realPrimes.append(i+2)

    return realPrimes


def primeFactors(n):
    primeFactors = []
    for i in primesUpTo(n):
        if n % i == 0:
            primeFactors.append(i)
    primeFactors.sort()
    newPrimeFactors = []
    for i in primeFactors:
        a = n
        b = 0
        while a == round(a):
            a /= i
            b += 1
        newPrimeFactors.append([i, b-1])

    return newPrimeFactors


def factors(n):
    factors = []
    for i in range(1, math.ceil(n**0.5)):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))
    factors.sort()
    return factors


def numOfFactors(n):
    return len(factors(n))

def isPrime(n):
    if n<2:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7: 
        return True
    if n%2 == 0 or n%3 == 0: 
        return False

    r = int(n**0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6. 
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True   