import time

start = time.time()

triangles = set([n*(n+1)/2 for n in range(285,1000000)])
pentagonals = set([n*(3*n-1)/2 for n in range(1,100000)])
hexagonlas = set([n*(2*n-1) for n in range(1, 100000)])

for t in triangles:
    if t in pentagonals and t in hexagonlas:
        print(t)

print(time.time()-start)