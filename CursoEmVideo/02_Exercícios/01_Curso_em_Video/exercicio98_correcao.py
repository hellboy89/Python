"""
(OK) - Faça um programa que tenha um "função" chamada "contador()".
(OK) - que receba 3 "parâmetros: início, fim e passo" e realize a contagem.
(OK) - Seu programa tem que realizar "três contagens" através da função criada:
(OK) - A) De 1 até 10, de 1 em 1
(OK) - B) De 10 até 0, de 2 em 2
(OK) - C) Uma contagem "personalizada".
"""

from time import sleep


def contador(i, f, p):
    if p < 0:
        # abaixo é para transformar um número positivo em negativo, ou vice versa. Dessa forma facilitando a contagem do número negativo até o positivo.
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.1)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.1)
            cont -= p
        print('FIM')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio:  '))
fim = int(input('fim:     '))
pas = int(input('passo:   '))
contador(ini, fim, pas)

# Uma coisa que notei, é que a entrada de dados tem que ser feita fora do DEF, no DEF e onde está toda a parte lógica do calculo, e a entrada de dados fica no final.