
palindromes=[]

for i in range(100,1000):
    for j in range(100,1000):
        num=i*j
        s=str(num)
        l=len(s)
        for k in range(l):
            if (s[k] != s[l-k-1]):
                break
        else:
            palindromes.append(num)
print(max(palindromes))
