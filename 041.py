from useful_functions import primesUpTo
import time

def is_pandigital(k, n):
    a=[]
    for i in range(1, n+1):
        a.append(str(i))
    return sorted(str(k)) == a

start = time.time()
primes = primesUpTo(int(1e7))
max = 0
for p in primes:
    if is_pandigital(p, len(str(p))):
        max = p
print(max)
print(time.time()-start)