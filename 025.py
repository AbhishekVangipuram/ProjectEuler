import time
start = time.time()


def fib(n):
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(n-1):
        c = a+b
        a = b
        b = c
    return c


n = 0
i = 0
while n < 1000:
    i += 1
    n = len(str(fib(i)))

print(i, time.time()-start)
