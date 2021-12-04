import math


def primesUpTo(n):
    """ Input n>=0, Returns a list of primes, 2 <= p < n """
    # By Robert William Hanks, from https://stackoverflow.com/a/3035188/4014959
    if n <= 1: return []
    if n == 2: return [2]
    if n <= 4: return [2,3]
    if n <= 6: return [2,3,5] 
    
    n += 1
    x, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (x//3)
    for i in range(1,int(x**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((x//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((x//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,x//3-correction) if sieve[i]]



def primeFactors(n):
    primeFactors = []
    x = n
    if x > 100:
        if n%7 == 0:
            x //= 7
        if n%5 ==0:
            x //= 5
        if n%3 == 0:
            x //= 3
        if x == n:
            x //= 2
    for i in primesUpTo(x):
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