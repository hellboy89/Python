# faça um programa que jogue "par ou impar" com o computador. O jogo será interrompido quando
# o jogador "perde", mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

v = 0
while True:
    jogador = int(input('diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    # aqui ele define uma condição, só irá passar se for digitado P ou I.
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR? [P/I]: ')).strip().upper()[0]
    # esse f'' é a forma antiga de definir a saída da variável.
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print(' DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        # um exemplo de condições aninhadas que pode ser utilizado.
        if total % 2 == 0:
            print('vc VENCEU!')
        else:
            print('vc PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('vc VENCEU!')
            v += 1
        else:
            print('vc PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')

# import random
#
#
# rand = random.randint(0, 11)
#
# while True:
#     valor = int(input('digite um valor de 0 à 10: '))
#     parimpar = str(input('PAR ou IMPAR? [P/I] ')).lower().strip()[0]
#
#     if valor % 2 == 0 and parimpar == 'p':
#         print('\no número escolhido foi PAR!')
#     elif valor % 2 == 1 and parimpar == 'i':
#         print('\no número escolhido foi IMPAR!')
#     else:
#         break
#         print('valor incorreto, tente novamente')


# print(n)
# print(n % 2)

# => TESTANDO O RANDOM
# if n % 2 == 0:
#     print('\no computador escolheu {} que é PAR.\n'.format(n))
# else:
#     print('\no computador escolheu {} que é IMPAR.\n'.format(n))

# => TESTANDO POSSIBILIDADES
# while True:
#     n = random.randint(0, 100)
#     time.sleep(0.5)
#     # print(n)
#     if n % 2 == 0:
#         print('o computador escolheu {} que é PAR.'.format(n))
#     else:
#         print('o computador escolheu {} que é IMPAR.'.format(n))
