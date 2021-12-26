num = int(input("Digite o valor de N: "))

fatorial = 1
for i in range(num, 0, -1):
    fatorial = fatorial * i

print(f"Fatorial = {fatorial}")

