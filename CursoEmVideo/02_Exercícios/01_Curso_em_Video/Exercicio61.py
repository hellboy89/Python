# refaça o "desafio 051", lendo o "primeiro termo" e a "razão" de uma "PA",
# mostrando os "10 primeiros termos" da progressão usando a estrutura "while".

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
# como a questão só quer os primeiros 10 termos, por isso o contador abaixo "cont <= 10".
while cont <= 10:
    print('{} -> '.format(termo), end='')
    #aqui ele irá somar o termo = termo + razao.
    termo += razao
    cont += 1
print('FIM')
