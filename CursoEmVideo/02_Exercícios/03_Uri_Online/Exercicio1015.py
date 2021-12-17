"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1015

"""
print('\033c')


def distancia(x1, y1, x2, y2):
    from math import sqrt
    distancia = (x2 - x1)**2 + (y2 - y1)**2
    raiz_q = sqrt(distancia)
    return raiz_q


valores1 = input().split()
valores2 = input().split()
x1 = float(valores1[0])
y1 = float(valores1[1])
x2 = float(valores2[0])
y2 = float(valores2[1])

calc = (distancia(x1, y1, x2, y2))

print(f'{calc:.4f}')

print()

"""
TAGS:
- calculo raiz quadrada
- separação de números por linha com split
- exemplo de funções
"""