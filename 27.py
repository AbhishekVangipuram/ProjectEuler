import time
import math
start = time.time()
#from problem 3
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
primes = primes(100000)
max=0
a1=0
b1=0
product=0
for a in range(-999,1000):
    for b in range(-1000,1001):
        n=0
        while (n**2 + a*n + b) in primes:
            n+=1
        if n>max:
            a1=a
            b1=b
            product=a1*b1
            max=n
print(max,a,b,product)
print(time.time()-start)