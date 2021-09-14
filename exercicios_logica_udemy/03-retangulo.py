from math import sqrt

base = float(input("Base do retangulo: "))
alt = float(input("Altura do retangulo: "))

area = base * alt
perimetro = 2 * (base + alt)
diagonal = sqrt(pow(base, 2) + pow(alt, 2))

print(f"Area = {area:.4f}")
print(f"Perimetro = {perimetro:.4f}")
print(f"Diagonal = {diagonal:.4f}")
