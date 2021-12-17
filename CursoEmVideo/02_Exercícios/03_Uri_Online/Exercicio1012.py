"""
(OK) - Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
(OK) - a) a área do triângulo retângulo que tem A por base e C por altura.
(OK) - b) a área do círculo de raio C. (pi = 3.14159)
(OK) - c) a área do trapézio que tem A e B por bases e C por altura.
(OK) - d) a área do quadrado que tem lado B.
(OK) - e) a área do retângulo que tem lados A e B.
"""

valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

triangulo = (A * C) / 2
circulo = 3.14159 * (C ** 2)
trapezio = ((A + B) / 2) * C
quadrado = B ** 2
retangulo = A * B

print(valores)

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')

"""
TAGS:
- calculo de raiz quadrada
"""