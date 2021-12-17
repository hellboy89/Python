from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''sua opção
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 3 ] TESOURA''')

jogador = int(input('qual é a sua jogada: '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')
print('-=' * 20)
print('O computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 12)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VC VENCEU MANÉ!')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VC VENCEU MANÉ!')
    else:
        print('opção inválida')
elif computador == 2:
    if jogador == 0:
        print('VC VENCEU MANÉ!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
