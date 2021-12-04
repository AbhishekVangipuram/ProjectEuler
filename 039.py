import time

start = time.time()
max = 0
maxp = 0
for p in range(10, 1001):
    num = 0
    c = p//2
    while c > p * 0.414: # extreme is at isosceles rigth tirangle when c = p * 0.414
        for a in range(1, int(c * 0.71)): # extreme is at isosceles when a = c * 0.71
            if a**2 + (p-c-a)**2 == c**2:
                num+=1
        c-=1
    if num > max:
        max = num
        maxp = p
print(maxp, max)
print(time.time() - start)