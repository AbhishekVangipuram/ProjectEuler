from num2words import num2words


def parseNum(s):
    s = s.replace(',', '')
    s = s.replace('-', '')
    s = s.replace(' ', '')
    return s


tot = 0
for i in range(1, 1001):
    tot += len(parseNum(num2words(i)))
print(tot)
