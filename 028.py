import time

start = time.time()
sum=1
a=1
for i in range(1,501):
    for j in range(1,5):
        a+=2*i
        sum+=a

print(sum)
print(time.time()-start)