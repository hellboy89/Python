somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 4):
    print('_____{}ª Pessoa _____'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
mediaidade = somaidade / 3

print('a media de idade do grupo é de {} anos.'.format(mediaidade))
print('o homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
