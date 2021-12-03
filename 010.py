#Use primes function from Problem 3
import math
def primes(n):
    primes=[2]
    for i in range(2,n+1):
        for j in range(2,math.ceil(i**0.5)+1):
            #print(i,j)
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes

def sumOfArray(a):
    tot=0
    for i in a:
        tot+=i
    return tot

print(sumOfArray(primes(2000000)))
