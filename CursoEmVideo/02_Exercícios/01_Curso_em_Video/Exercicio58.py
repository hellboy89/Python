# Melhores o jogo do "desafio 028" onde o computador vai "pensar" em um "número entre 0 e 10".
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer.

from random import randint

computador = randint(0, 10)
print('Sou seu computador.. Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('qual é seu palpite? '))
    palpites += 1
    # é possível parar um while usando o "if".
    if jogador == computador:
        # é o True abaixo que encerra o processo do While, pois ele só inicia poir o acertou is false.
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente mais uma vez.')
        elif jogador > computador:
            print('Menos.. Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
