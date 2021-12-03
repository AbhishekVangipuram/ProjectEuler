import useful_functions as uf


def triangle(n):
    return n*(n+1)/2

x = 0
for i in range(1, 1000000000):
    if uf.numOfFactors(triangle(i)) > 500:
        x = triangle(i)
        break
print(x)
