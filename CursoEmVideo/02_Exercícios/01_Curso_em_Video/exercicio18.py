# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

ang = float(input('informe o valor do ângulo: '))

sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('o valor do seno é {:.2f}.\nO valor do cosseno é {:.2f}.'
      ' \nO valor da tangente é {:.2f}'.format(sen, cos, tan))
