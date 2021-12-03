import math
import time
from useful_functions import isPrime

def rotations(n):
    # if n < 10:
    #     return list({n})
    s = str(n)
    rots = []
    for d in range(0, len(s)):
        ns = s[-d:] + s[0:-d]
        rots.append(int(ns))
    return rots

start = time.time()
count = 0
for i in range(1, 1000000):
    bad = False
    
    for n in rotations(i):
        if not isPrime(n):
            bad = True
            break
    if not bad:
        count+=1

print(count)
print(time.time()-start)