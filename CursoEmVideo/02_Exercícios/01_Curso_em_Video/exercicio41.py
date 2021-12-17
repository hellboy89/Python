from datetime import date

anonasc = int(input('informe o ano de nascimento do atleta: '))
anoatual = date.today().year
idade = anoatual - anonasc

if idade <= 9:
    print('com {} anos, a categoria é MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('com {} anos, a categoria é INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('com {} anos, a categoria é JUNIOR.'.format(idade))
elif idade > 19 and idade == 20:
    print('com {} anos, a categoria é SÊNIOR.'.format(idade))
elif idade > 20 and idade < 101:
    print('com {} anos, a categoria é MASTER.'.format(idade))
elif idade > 101:
    print('com {} anos, tá velho demais pra nadar VÔVÔ.'.format(idade))
