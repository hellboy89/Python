# crie um programa que leia a "idade" e o "sexo" de "várias pessoas". A cada pessoa cadastrada, o programa
# deverá perguntar se o "usuário" quer ou não continuar. No final mostre:
# a) quantas pessoas tem mais de "18 anos".
# b) quantos "homens" foram cadastrados.
# c) quantas "mulheres" tem menos de "20 anos".

idadec = idade18 = sexoc = idade20 = 0

while True:
    idade = int(input('informe a sua idade: '))
    sexo = str(input('informe o sexo [M/F]: ')).strip()[0].lower()
    parar = str(input('deseja continuar o cadastro? [S/N] ')).strip()[0].lower()
    idadec += idade
    if idade > 18:
        idade18 += 1
    if sexo == 'm':
        sexoc += 1
    if sexo == 'f' and idade < 20:
        idade20 += 1
    if parar == 'n':
        break

print('tem {} pessoas com mais de 18 anos.'.format(idade18))
print('foram cadastrados {} homens.'.format(sexoc))
print('foram cadastrados {} mulheres abaixo de 20 anos.'.format(idade20))
