import math
import os
os.system('clear||cls')
print("Решение квадратных уравнений")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
#(bxb = b*b )
#ac4= 4*(a*c)
print()
D = b * b - 4 * (a * c)
Ds = math.sqrt(D)
print("D=" + str(D)+",Корень D=" + str(Ds))

x1 = (-b + Ds) / (2 * a)
x2 = (-b - Ds) / (2 * a)
print("x1=" + str(x1), "x2=" + str(x2))
input()
