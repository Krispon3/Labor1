from math import *

proiz = 1
for n in range(1,11):
    proiz *= (3*(n**2) + 2*n + 1)/2*(n**2) + sin(2*(n**2))
    
print(proiz)
