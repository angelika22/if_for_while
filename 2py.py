import math
a=int(input("dati numarul "))
s=0
for b in range (1, a+1):
    s+=math.factorial(b)
print("suma este", s)