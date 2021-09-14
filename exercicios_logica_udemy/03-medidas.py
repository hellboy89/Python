valorA = float(input("Digite a medida A: "))
valorB = float(input("Digite a medida B: "))
valorC = float(input("Digite a medida C: "))

areaQuad = valorA * valorA
areaTri = (valorA * valorB) / 2
areaTrap = ((valorA + valorB) * valorC) / 2

print(f"Area do quadrado = {areaQuad:.4f}")
print(f"Area do triangulo = {areaTri:.4f}")
print(f"Area do trapezio = {areaTrap:.4f}")
