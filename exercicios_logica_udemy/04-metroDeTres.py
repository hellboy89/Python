valor1 = int(input("Primeiro Valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))

menor = valor1

if menor > valor2:
    menor = valor2
elif menor > valor3:
    menor = valor3

print(f"Menor = {menor}")
