# Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
# peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
# • Homens: (72. 7 * h) - 58
# • Mulheres: (62, 1 * h) - 44, 7

peso = int(input('qual seu peso: '))
alt = float(input('qual sua altura: '))
sexo = bool(input('qual seu sexo: '))

homens = (72.7 * alt) - 58
mulheres = (62.1 * alt) - 44.7

if sexo == True:
    print('seu peso ideal é {}'.format(homens))
if peso > 80.13 and sexo == True:
    print('vc está acima do peso gordão.')
if sexo == False:
    print('seu peso ideal é {}'.format(mulheres))
if peso < 50 and sexo == False:
    print('vá comer alguma coisa vagabunda seca.')
