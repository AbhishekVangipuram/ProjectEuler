a=[]
i=1
up_to=1000
while i<up_to:
    if i%3==0 or i%5==0:
        a.append(i)
    i+=1
total=0
for j in a:
    total+=j
print(total)
