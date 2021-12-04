import time
from useful_functions import primeFactors, primesUpTo

start = time.time()

n = 1
while True:
    s = set()
    l = lambda x:len(primeFactors(x)) == 4
    if l(n) and l(n+1) and l(n+2) and l(n+3):
        print(n)
        break
    if n % 1000 == 0:
        print(f'{n}\t\t\t{time.time()-start}')
    n += 1
print(time.time()-start)