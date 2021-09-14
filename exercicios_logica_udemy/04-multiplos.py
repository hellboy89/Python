print("Digite dois numeros inteiros: ")
val1 = int(input())
val2 = int(input())

if val1 % val2 == 0 or val2 % val1 == 0:
    print("São Multiplos.")
else:
    print("Não são Multiplos.")

