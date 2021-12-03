import time
import math

start = time.time()

arr = []
for i in range(10, 100):
    for j in range(10, 100):
        if not (j % 10 == 0 and i % 10 == 0):
            if i / j == math.floor(i / 10) / (j % 10):
                arr.append((i, j))
            elif i / j == (i % 10) / math.floor(j / 10):
                arr.append((i, j))
num = 1
den = 1
for (a, b) in arr:
    num *= a
    den *= b

print(den / math.gcd(num, den))

print(time.time() - start)
