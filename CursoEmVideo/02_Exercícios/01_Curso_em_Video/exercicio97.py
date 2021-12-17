"""
(OK) - Faça um programa que tenha uma 'função' chamada 'escreva()',
(OK) - que receba um texto qualquer como 'parâmetro'
(NÃO SEI) - e mostre uma mensagem com tamanho adaptável.
"""
# Professor informou que com apenas um comando é possível resolver essa questão. Que seria o comando "escreve".

def escreva(*sms):
    print('-=' * 5)
    print(sms[0])
    print('-=' * 10)
    print('-=' * 10)
    print(sms[1])
    print('-=' * 20)
    print('-=' * 20)
    print(sms[2])
    print('-=' * 20)


# TÔ FAZENDO ALGUNS TESTES NO ARQUIVO TESTE2.PY.
# Necessário ter apenas um comando aqui em baixo. O resto será feito no DEF.
escreva('TESTE')


