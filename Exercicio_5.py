import math

x2 = int(input("Qual seu valor de X2 : "))
x1 = int(input("Qual seu valor de X1 : "))

y2 = int(input("Qual seu valor de Y2 : "))
y1 = int(input("Qual seu valor de Y1 : "))

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(d)
