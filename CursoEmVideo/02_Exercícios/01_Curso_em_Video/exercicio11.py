# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2 m².

alt = float(input('insira a altura da parede: '))
lar = float(input('insira a largura da parede: '))
area = lar*alt
tinta = area / (area/2)

# if alt == 2 and lar == 2:
#     print('dá certinho para um litro de tinta.')
# else:

print('com {} de espaço total,\n a quantidade de tinta necessária é {}'.format(area, tinta))
