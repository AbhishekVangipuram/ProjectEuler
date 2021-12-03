import math
#for n>=2, primes up to n
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

def primeFactorize(n):
    i=2
    k=math.ceil(n**0.5)
    primeDivisors=[]
    for p in primes(k):
        if n%p==0:
            primeDivisors.append(p)
    return primeDivisors
def maxOfArray(array):
    max=array[0]
    for a in array:
        if a>max:
            max=a
    return max
print(maxOfArray(primeFactorize(600851475143)))
