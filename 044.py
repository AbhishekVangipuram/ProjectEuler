import time

start = time.time()

pentagonals = set([n*(3*n-1)/2 for n in range(1, 10000)])
D = 9999999999999

for j in pentagonals:
    for k in pentagonals:
        if j+k in pentagonals and abs(j-k) in pentagonals:
            if abs(j-k) < D:
                D = abs(j-k)
                print(D)
print(D)
print(time.time()-start)