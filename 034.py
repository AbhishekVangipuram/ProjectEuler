import math
import time

start = time.time()
sum = 0
for i in range(10,100000000):
    tmp = 0
    x = i
    while x>0 and tmp <= i:
        tmp += math.factorial(int(x%10))
        x //= 10    
    if i == tmp:
        sum += i
    
print(sum)
print(time.time() - start)