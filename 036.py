import math
import time

def is_palindrome(s):
    return s == s[::-1] # reverses string

def change_base(n, orig_b=10, new_b=2):
    pass

start = time.time()

count = 0
for i in range(1, 1000000):
    if is_palindrome(str(i)) and is_palindrome(change_base(str(i))):
        count+=1

print(count)
print(time.time()-start)
    