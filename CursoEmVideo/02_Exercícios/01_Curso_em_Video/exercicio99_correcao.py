"""
(OK) - Faça um programa que tenha uma "função" chamada "maior()",
(OK) - que receba vários "parâmetros" com valores inteiros.
(OK) - Seu programa tem que analisar todos os valores e dizer qual deles é o "maior".
"""

from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

# Programa principal
maior(2, 9, 4, 5, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


# Só tenho que prestar mais atenção na entrada de dados, pois ela tem que ser feita fora do DEF, dentro somente a parte lógica do código.
# Nâo importa a quantidade de dados passados no parâmetro "escreva", ele sempre irá ler todos eles e executar o DEF.
