import itertools as it

p = list(it.permutations('0123456789', 10))

s = ''
for i in p[999999]:
    s += i
print(int(s))
