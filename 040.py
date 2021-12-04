import time
start = time.time()
d = 0
k = 0
while d <= 1000000:
    k+=1
    d+=len(str(k))
    c = lambda i : d>=i and d-len(str(k)) < i 
    if c(1) or c(10) or c(100) or c(1000) or c(10000) or c(100000) or c(1000000):
        print(d, k)

d1 = 1
d10 = 1
d100 = 5
d1000 = 3
d10000 = 7
d100000 = 2
d1000000 = 1
ans = 1*1*5*3*7*2*1 # 210
print(ans)
print(time.time()-start)