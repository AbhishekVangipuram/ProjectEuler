max = 0
max_n = 0
n = 1
while n < 1000000:
    steps = 0
    k = n
    while k != 1:
        if k % 2 == 0:
            k /= 2
        else:
            k = 3*k+1
        steps += 1
    if steps > max:
        max = steps
        max_n = n

    n += 1

print(max_n, max)
