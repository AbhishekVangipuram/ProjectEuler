import math


def coinSums(coins, target):
    coins.sort(reverse=True)
    if(len(coins) == 1):
        if(target % coins[0] == 0):
            return 1
        else:
            return 0
    c = coins[0]
    del coins[0]
    newCoinSum = 0
    for i in range(0, math.floor(target/c)+1):
        newtarget = target-i*c
        newCoinSum += coinSums(list(coins), newtarget)

    return newCoinSum


print(coinSums([1, 2, 5, 10, 20, 50, 100, 200], 200))
