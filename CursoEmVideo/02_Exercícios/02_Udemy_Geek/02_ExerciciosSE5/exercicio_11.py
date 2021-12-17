"""
(OK) - Escreva um programa que leia um número inteiro maior do que zero
(OK) - e devolva, na tela, a soma de todos os seus algarismos.
(OK) - Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1).
(OK) - Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".
"""

numero = int(input("Informe um número inteiro"))
soma = 0
while numero > 0:
    soma += numero % 10
    numero = numero // 10
print(soma)
