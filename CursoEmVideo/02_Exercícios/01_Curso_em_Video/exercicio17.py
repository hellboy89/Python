# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
# POSSÍVEL FAZER USANTO MÓDULO DO MATH.

import math

co = float(input('informe o valor do cateto oposto: '))
ca = float(input('informe o valor do cateto adjacente: '))

# hip = sqrt(co * co + ca * ca)
hip = math.hypot(co, ca)

print('o valor da hipotenusa é {:.2f}'.format(hip))
