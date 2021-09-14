quantRep = int(input("Quantos números você vai digitar? "))

dentro = 0
fora = 0

for i in range(0 , quantRep):
    num = int(input("Digite um número: "))
    if 10 <= num <= 20:
        dentro += 1
    else:
        fora += 1

print(f"{dentro} Dentro")
print(f"{fora} Fora")
