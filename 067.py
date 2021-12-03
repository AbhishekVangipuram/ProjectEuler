f = open("p067_triangle.txt", "r")
lines = []
for i in range(0, 100):
    line = f.readline()
    line = line.replace("\n", "")
    line = line.split(" ")
    for j in range(i+1):
        line[j] = int(line[j])
    lines.append(line)
f.close()
triangle = lines
# from problem 18
# start from bottom and go to top
triangle.reverse()
for i in range(0, 99):
    for j in range(0, len(triangle[1])):
        triangle[1][j] += max(triangle[0][j], triangle[0][j+1])
    triangle.pop(0)
print(triangle)
