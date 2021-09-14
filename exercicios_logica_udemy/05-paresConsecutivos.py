num = int(input("Digite um numero inteiro: "))

valorPares = 0

while num != 0:
    if num % 2 != 0:
        num += 1

    soma = 5 * num + 20
    print(f"Soma = {soma}")

    num = int(input("Digite um numero inteiro: "))


