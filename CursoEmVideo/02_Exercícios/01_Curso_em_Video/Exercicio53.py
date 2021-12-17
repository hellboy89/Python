frase = str(input('digite uma frase: ')).replace(' ', '').upper()
for c in range(1):
    fraseinv = frase[::-1]
    # print(fraseinv)
    if frase == fraseinv:
        print('é um palíndromo')
    else:
        print('NÃO é uma palíndromo')

# frase = 'a sacada da casa'
# juntar = frase.replace(' ', '')
#
# print((juntar))
