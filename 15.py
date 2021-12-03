# 2x2 grid - 6 paths ddrr 4!/(2!*2!)
# 3x3 grid - 20 paths dddrrr 6!/(3!*3!)
from math import factorial as fac
print(fac(40)/(fac(20)**2))
