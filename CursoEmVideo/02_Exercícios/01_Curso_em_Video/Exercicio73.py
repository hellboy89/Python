# Crie um "tupla" preenchida com os "20 primeiros" colocados da tabela do "campeonato brasileiro de futebol",
# na ordem de colocação. Depois mostre:
# a) apenas os "5 primeiros" colocados.
# b) os "últimos 4" colocados da tabela.
# c) Uma lista com os times em "ordem alfabética".
# d) Em que "posição" na tabela está o o time da "chapecoense".

colocados = ('america-mg', 'athletico-pr', 'atletico-mg', 'bahia', 'ceara sc', 'chapecoense',
             'corinthians', 'cuiabá', 'flamento', 'fluminense', 'fortaleza', 'grêmio', 'internacional',
             'juventude', 'palmeiras', 'bragantino', 'santos', 'sport recife', 'são paulo')

print('lista de times do brasileirão: {}'.format(colocados))
print('os 5 primeiros colocados são: {}'.format(colocados[0:5]))
print('os 4 últimos colocados são: {}'.format(colocados[15::]))
print('em ordem alfabética ficaria: {}'.format(sorted(colocados)))
print('o chapecoence está na {}ª posição.'.format(colocados.index("chapecoense")+1))


