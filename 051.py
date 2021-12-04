import time

from useful_functions import isPrime

start = time.time()

n = 10

while True:
    s = str(n)
    break2 = False
    for i in range(len(s)):
        tot = 0
        for k in range(10):
            s = s[:i] + str(k) + s[i+1:]
            if isPrime(int(s)): tot+=1
        if tot == 8:
            print(n, i)
            break2 = True
            break
        for j in range(i+1, len(s)): # 2 digit replacements
            tot = 0
            for k in range(10):
                s = s[:i] + str(k) + s[i+1:]
                s = s[:j] + str(k) + s[j+1:]
                if isPrime(int(s)): tot+=1
            if tot == 8:
                print(n, i, j)
                break2 = True
                break
        if break2:
            break
    if break2:
        break
    # print(n)
    n+=1

print(time.time()-start)