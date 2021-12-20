from math import sqrt

coefA = float(input("Coeficiente A: "))
coefB = float(input("Coeficiente B: "))
coefC = float(input("Coeficiente C: "))

x = (pow(coefB, 2)) - (4 * coefA * coefC)

if x < 0:
    print("Esta equiação não possui raizes reais.")
else:
    raizX = sqrt(x)
    x1 = (- coefB + raizX) / (2 * coefA)
    x2 = (- coefB - raizX) / (2 * coefA)

if x > 0:
    print(f"X1 = {x1:.4f}")
    print(f"X2 = {x2:.4f}")

