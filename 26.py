import time
import math

start = time.time()


def recurring_cycle(d):
    while math.floor(d) == d:
        d /= 2
    d *= 2
    while math.floor(d) == d:
        d /= 5
    d *= 5
    n = long_divison(1, d)
    if n == 0:
        return 0

    k = 0
    n=long_divison(n,d)
    while n!=long_divison(1,d):
        n=long_divison(n,d)
        k += 1
    return k+1


def long_divison(n, k):
    if (k == 1):
        return 0
    m = 0
    while 10 ** m * n < k:
        m += 1
    if (10 ** m * n) % k == 0:
        return 0
    i = 0
    while ((10 ** m * n) % k * 10 ** i) < k:
        i += 1
    return ((10 ** m * n) % k * 10 ** i)

d=0
max=0
for i in range(2,1000):
    if recurring_cycle(i)>max:
        d=i
        max=recurring_cycle(d)

print(d,recurring_cycle(d))
print(d,time.time()-start)
