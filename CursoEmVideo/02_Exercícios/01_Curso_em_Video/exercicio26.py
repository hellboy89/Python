frase = str(input('digite uma frase: ')).strip()

separa = frase.split()

count_a = frase.upper().count('A')

busca_a = frase.upper().find('A')

print('a letra A aparece o número de {}'.format(count_a))
print('a letra A aparece na primeira vez na posição {}'.format(busca_a))
print('a letra A aparece na última posição {}'.format(frase[::-1].upper().find('A')))
