soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'digite o {c} valor: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('a soma de todos os pares que são {} é {}'.format(cont, soma))
