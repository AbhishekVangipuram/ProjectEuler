import time 

def str_to_num(s):
    sum = 0
    for c in s:
        sum += ord(c) - ord('A') + 1
    return sum

start = time.time()

triangles = set()
for n in range(1, 1000000):
    triangles.add(n*(n+1) / 2)

f = open('p042_words.txt', 'r')
names = f.readline().split(',')
count = 0
for i, name in enumerate(names):
    names[i] = name[1:-1]
    if str_to_num(names[i]) in triangles:
        count+=1

print(count)
print(time.time() - start)
