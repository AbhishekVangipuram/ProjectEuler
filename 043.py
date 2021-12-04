import time
from itertools import permutations

start = time.time()

pandigitals = []
for tup in list(permutations("0123456789", 10)):
    if tup[0] != '0':
        pandigitals.append(int(''.join(tup)))

sum = 0
for n in pandigitals:
    d = lambda k : str(n)[k]
    c = lambda a, m : int(d(a-1)+d(a)+d(a+1)) % m == 0
    if c(2,2) and c(3,3) and c(4,5) and c(5,7) and c(6,11) and c(7, 13) and c(8, 17):
        sum += n

print(sum)
print(time.time() - start)