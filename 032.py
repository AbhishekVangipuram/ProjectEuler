import time

start = time.time()


def is_pandigital(s):
    if len(s) != 9:
        return False
    arr = list(s)
    arr.sort();
    if arr != ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return False
    else:
        return True


array = []
for i in range(5000):
    for j in range(5000):
        if i * j in array:
            continue
        s = str(i) + str(j) + str(i * j)
        if is_pandigital(s):
            array.append(i * j)

sum = 0
for a in array:
    sum += a

print(sum)
print(time.time() - start)
