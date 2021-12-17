# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('digite um nome: '))

separa = nome.split()

acha = nome.find('silva')

# print(separa)

# print(acha)

if acha >= 0:
    print('tem silva no nome!')
else:
    print('NÃO tem silva no nome!')
