import time 

start = time.time()

sum = 0
for i in range(1, 1001):
    sum += (i**i) % 10**10
    sum %= 10**10

print(sum)
print(time.time()-start)
