"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

(OK) - Faça um programa que leia três valores
(OK) - e apresente o maior dos três valores lidos
(OK) - seguido da mensagem “eh o maior”.
(OK) - Utilize a fórmula: maiorAB = (a+b+abs(a-b)) / 2
(OK) - Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
(OK) - Um segundo passo, portanto é necessário para chegar no resultado esperado.
"""
print('\033c')


def q_maior(a, b, c):
    lista = [a, b, c]
    maior = max(lista)
    # o return indica o valor que eu quero que saia da minha função e volte para o meu programa principal.
    return maior


valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

lista = (q_maior(a, b, c))

print(f'{lista} eh o maior')


print()
