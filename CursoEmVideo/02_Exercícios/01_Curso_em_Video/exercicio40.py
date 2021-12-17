n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('reprovado!')
    print('\na média foi {}.'.format(media))
elif media > 5.0 and media < 6.9:
    print('recuperação!')
    print('\na média foi {}.'.format(media))
elif media >= 7.0 and media <= 10:
    print('aprovado!')
    print('\na média foi {}.'.format(media))
elif media > 10:
    print('valor incorreto o máximo de notas é 10.')
