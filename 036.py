import time

def is_palindrome(s):
    return s == s[::-1] # reverses string

def change_base(n, orig_b=10, new_b=2):
    if orig_b != 10:
        t = 0
        for i, c in enumerate(n):
            t += int(c) * orig_b**(len(n)-1-i)
        n = t
    n = int(n)
    x = int(n)
    count = 0
    while x>0:
        x //= new_b
        count+=1
    s = ''
    x = n
    exp = count-1
    while len(s) < count:
        tmp=0
        while n >= new_b**exp:
            n -= new_b**exp
            tmp+=1
        exp-=1
        s+=str(tmp)
        while n < new_b**exp and len(s)<count:
            exp-=1
            s+='0'

    return s

start = time.time()

sum = 0
for i in range(1, 1000000):
    if is_palindrome(str(i)) and is_palindrome(change_base(str(i))):
        sum+=i

print(sum)
print(time.time()-start)
    