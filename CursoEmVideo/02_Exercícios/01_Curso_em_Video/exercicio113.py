"""
(OK) - Rescreva a função "leiaInt()" que fizemos no "desafio 104",
(OK) - Incluindo agora a possibilidade da digitação de um número de tipo inválido.
(OK) - Aproveite e crie também uma função "leiaFloat()" com a mesma funcionalidade.
"""


def leiaInt(inteiro):
    return inteiro


def leiaFloat(float):
    return float


while True:
    try:
        n = int(input('digite um valor INTEIRO: '))
        n2 = float(input('digite um valor REAL: '))
        inteiro = leiaInt(n)
        real = leiaFloat(n2)
    except (ValueError, TypeError):
        print(f'Digite somente números, obrigado!')
    except KeyboardInterrupt:
        print('Programa interrompido pelo usuário!')
    else:
        print(f'O valor INTEIRO é {inteiro}')
        print(f'O valor FLOAT é {real}')
        break
    finally:
        print('\nContinue TENTANDO!... Uma hora vai hehe! ;)')

# NECESSÁRIO COLOCAR TUDO DENTRO DE UM WHILE, POIS A PERGUNTA PRECISA SE REPETIR ATÉ O VALOR DIGITADO SER CORRETO.
