# crie um programa que leia "dois valores" e mostre um "menu" na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('==> Qual é sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('a soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        multiplica = n1 * n2
        print('a multiplicação entre {} e {} é {}.'.format(n1, n2, multiplica))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('finalizando...')
    else:
        print('opção {} inválida, tente novamente.'.format(opcao))
print('fim do programa volte sempre.')
