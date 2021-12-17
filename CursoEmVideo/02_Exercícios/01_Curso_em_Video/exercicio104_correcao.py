"""
() - Crie um programa que tenha a "função leiaInt()",
() - que vai funcionar de forma semelhante a função "input()" do python.
() - só que fazendo "validação" para aceitar apenas um valor numérico.
EX: n = leiaInt('digite um n')
"""
print('\033c')


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        # Foi graças a função abaixo "isnumeric" que foi possível realizar o condicional, diferente da minha solução criando letra por letra. E mais elegante também <3.
        if n.isnumeric():
            valor = int(n)
            # Aqui se for um número digitado ele retornar o valor "true" na variável "ok" e encerra abaixo. Retornando apenas a variável valor.
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
