"""
(OK) - Faça um programa que tenha uma 'função' chamada 'escreva()',
(OK) - que receba um texto qualquer como 'parâmetro'
(OK) - e mostre uma mensagem com tamanho adaptável.
"""


def escreva(msg):
    # Dessa forma abaixo é possível usar o LEN para criar linhas de separação exatamente igual ao tamanho do texto.
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('Juan Cleber')
escreva('Faculdades São José')
escreva('Artsoft Sistemas')
