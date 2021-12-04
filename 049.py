import time
from itertools import permutations
from useful_functions import isPrime

start = time.time()

for i in range(1000, 10000):
    k = 1
    while i + 2*k < 10000:
        if sorted(str(i)) == sorted(str(i+k)) == sorted(str(i+2*k)):
            if isPrime(i) and isPrime(i+k) and isPrime(i+2*k):
                print(i, i+k, i+2*k)
                break
        k+=1

print(time.time() - start)