maior = 0
menor = 0

for p in range(1, 5):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:  # primeiro peso, a comparaçã é feita com base aqui.
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('o maior peso lido foi de {}kg.'.format(maior))
print('o menor peso lido foi de {}kg.'.format(menor))
