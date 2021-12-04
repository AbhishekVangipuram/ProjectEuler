from useful_functions import primesUpTo, isPrime
import time

start = time.time()

primes = primesUpTo(1000000)[4:]

def check(n):
    # check truncation from right to left
    x = n
    while x > 0:
        if not isPrime(x):
            return False
        x //= 10
    # check truncation from left to right
    x = n
    while x > 0:
        if not isPrime(x):
            return False
        if str(x)[1:] == '':
            break
        x = int(str(x)[1:])
    return True

good = []
sum = 0
for p in primes:
    if check(p):
        good.append(p)
        sum += p

print(good, sum)
print(time.time() - start)