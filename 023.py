import time
import useful_functions as uf
start = time.time()


def isAbundant(n):
    if n <= 1:
        return False
    divisors = uf.factors(n)
    sum = 0
    for i in divisors:
        sum += i
    if sum > 2*n:
        return True
    else:
        return False


def abundantUpTo(n):
    abundant_nums = []
    for i in range(1, n+1):
        if isAbundant(i):
            abundant_nums.append(i)
    return abundant_nums


def sum2abundant(n):  # return list of numbers that are sums of 2 abundant numbers up to n
                    # Doesnt contain 1141, 1771, or 7621 even though it should
    abundant_nums = abundantUpTo(n)
    sum2abundant = []
    for x in abundant_nums:
        for y in abundant_nums:
            if x > y:
                continue
            z = x+y
            if z > n:
                continue
            sum2abundant.append(z)
    sum2abundant=set(sum2abundant)
    return sum2abundant


def notsum2abundant(n):
    notsum2abundant = []
    sumofabundant = sum2abundant(n)
    for i in range(1, n+1):
        if i not in sumofabundant:
            notsum2abundant.append(i)
    return notsum2abundant

'''
answer_list = notsum2abundant(30000)
tot = sum(answer_list)
print("%d\n%f" % (tot, time.time()-start))
'''
nums = open('not_sum_of_abundants.txt', 'r')
lines = nums.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].split(' ')
    lines[i] = lines[i][1]
    lines[i] = lines[i].split('\n')
    lines[i] = int(lines[i][0])
sum = sum(lines)
print(sum, time.time()-start)
