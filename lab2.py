from math import *
for x in range(10,95,5):
    x = x/100
    y = sin(4**(x-log(3*x))) + log(3*x,4)
    print("x =", x, "  y =", y)
