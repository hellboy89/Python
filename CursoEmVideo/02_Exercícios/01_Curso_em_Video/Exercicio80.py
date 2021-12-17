"""
(OK) - Crie um programa onde o usuário possa digitar cinco "valores numéricos"
(OK) - e os cadastre em uma "lista",
(OK, mas tive muita dificuldade) - "já na posição correta" de inserção (SEM USAR O "sort()").
(OK) - No final, mostre a "lista ordenada" na tela.
"""

lista = []

for c in range(0, 5):
    n = int(input('informe um valor: '))
    # todo número que entrar irá para o final da lista.
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posição {pos} da lista...')
                break
            pos += 1

print('-=' * 30)
print('a lista ordenada ficaria: {}'.format(lista))
