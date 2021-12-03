n=1
while True:
    for i in range(1,21):
        if n%i!=0:
            break
    else:
        break
    n+=1

print(n)
