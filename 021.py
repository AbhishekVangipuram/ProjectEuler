import useful_functions as uf


def d(n):
    if n <= 1:
        return 0
    tot = 0
    for i in uf.factors(n):
        tot += i
    tot -= n
    return tot


sum = 0
for i in range(1, 10000):
    if i == d(d(i)) and i != d(i):
        sum += i
print(sum)
