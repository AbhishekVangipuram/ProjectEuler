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
