import math
from useful_functions import  primesUpTo, isPrime
import math
import time

start = time.time()
n = 3
while True:
    if isPrime(n):
        n+=2
        continue
    conj = False
    for p in primesUpTo(n):
        if p==2:
            continue
        if math.sqrt((n-p)/2) == int(math.sqrt((n-p)/2)):
            conj = True
            break
    if not conj:
        print(n)
        break
    n+=2
    
print(time.time()-start)