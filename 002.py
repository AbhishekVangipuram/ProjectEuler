def evenFib(n):
    array=[]
    a=0
    b=1
    c=0
    while c<n:
        c=a+b
        a=b
        b=c
        if c%2==0:
            array.append(c)
    return array
total=0
for i in evenFib(4000000):
    total+=i
print(total)
