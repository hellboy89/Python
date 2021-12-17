idade = int(input('digite a sua idade: '))

if idade == 18:
    print('está na hora de se alistar ao serviço militar. Já passou em {} anos.'.format(idade - 18))
elif idade > 18 and idade < 27:
    print('já passou da hora de se alistar ao serviço militar. Já passou em {} anos.'.format(idade - 18))
elif idade >= 27:
    print('vc já passou da idade!. Já passou em {} anos.'.format(idade - 18))
elif idade < 18:
    print('ainda não está na idade de se alistar no serviço militar. Ainda falta {} anos.'.format(18 - idade))
elif idade > 100:
    print('ninguém é tão velho assim, TENTE NOVAMENTE! Já passou em {} anos.'.format(idade - 18))
