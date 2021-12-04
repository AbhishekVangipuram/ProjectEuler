import time

def is_pandigital(s):
    return sorted(s) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

start = time.time()
max = 0
for n in range(1,10):
    for k in range(1000000):
        s = ''
        for i in range(1, n+1):
            s += str(k*i)
        if len(s) > 9:
            break
        # print(s)
        if int(s) > max and is_pandigital(s):
            max = int(s)
print(max)
print(time.time() - start)
