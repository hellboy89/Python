# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('qual nome da cidade: ')).strip()

valor = cidade[:5].upper() == 'SANTO'

print(cidade[:5].upper() == 'SANTO')

if valor == True:
    print('sim tem SANTO no começo!')
else:
    print('não tem SANTO!')
