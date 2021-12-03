import math
#primes up to the nth prime, n>=1
def primes(n):
    primes=[2]
    i=3
    while len(primes)<n:
        for j in range(2,math.ceil(i**.5)+1):
            if i%j==0:
                break
        else:
            primes.append(i)
        i+=1
    return primes
print(primes(10001)[-1])
