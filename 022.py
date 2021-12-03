txt = open("p022_names.txt", 'r')
raw_names = txt.readlines()
raw_names = raw_names[0].split(",")

names = []
for i in raw_names:
    names.append(i[1:len(i)-1])
names.sort()

name_scores = []
for i in names:
    place = names.index(i)+1
    name_sum = 0
    for j in i:
        name_sum += (ord(j)-64)
    name_scores.append(place*name_sum)

tot = 0
for i in name_scores:
    tot += i
    
print(tot)
