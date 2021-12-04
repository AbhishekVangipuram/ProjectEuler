import time
from useful_functions import primeFactors

start = time.time()
n = 1
while True:
    s = set()
    l = lambda x:len(primeFactors(x)) == 4
    if l(n) and l(n+1) and l(n+2) and l(n+3):
        print(n)
        break
    n += 1
print(time.time()-start)