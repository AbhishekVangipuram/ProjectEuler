import time

start = time.time()

nums = []
for i in range(2, 1000000):
    digits = list(str(i))
    sum = 0
    for d in digits:
        sum += int(d) ** 5
    if sum == i:
        nums.append(i)

sum = 0
for i in nums:
    sum += i

print(nums, sum)
print(time.time() - start)
