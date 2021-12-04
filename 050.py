import time
from useful_functions import primesUpTo

start = time.time()

primes = primesUpTo(1000000)
maxp = primes[-1]
bestp = 0
maxnums = 0
print(maxp)
for start in range(1000000):
    for num in range(21, 10000):
        sum = 0
        break2 = False
        # print(primes[start], num, "-------------------------")
        for i in range(num):
            sum += primes[start+i]
            # print(sum)
            if sum > maxp:
                break2 = True
                break 
        if sum in primes and num > maxnums:
            bestp = sum
            maxnums = num
            print(bestp,"\t\t\t", maxnums)
        if break2:
            break   

print(bestp, maxnums)
print(time.time() - start)