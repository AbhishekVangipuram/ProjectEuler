import time
import math

start = time.time()

arr = []
for i in range(10, 100):
    for j in range(10, 100):
        if i >= j:
            continue
        if not (j % 10 == 0 and i % 10 == 0):
            a1, a2, b1, b2 = math.floor(i/10), i%10, math.floor(j/10), j%10
            if a1 == b1 and b2!=0:
                if i/j == a2/b2:
                    arr.append((i,j))
            if a1 == b2:
                if i/j == a2/b1:
                    arr.append((i,j))
            if a2 == b1 and b2!=0:
                if i/j == a1/b2:
                    arr.append((i,j))
            if a2 == b2:
                if i/j == a1/b1:
                    arr.append((i,j))
num = 1
den = 1
for (a, b) in arr:
    num *= a
    den *= b

print(den / math.gcd(num, den))

print(time.time() - start)
