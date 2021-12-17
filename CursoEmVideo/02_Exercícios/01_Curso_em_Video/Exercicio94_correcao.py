"""
(OK) - Crie um programa que leia 'nome, sexo e idade' de 'várias pessoas',
(OK) - guarde os dados de cada pessoa em um 'dicionário', e todos os dicionários em uma 'lista'.
(OK) - No final, mostre: A) Quantas pessoas foram cadastradas.
(OK) - B) A 'média' de idade do grupo.
(OK) - C) Uma lista com todas as 'mulheres'.
(OK) - D) Uma lista com todas as pessoas com 'idade' acima da 'média'.
"""

# Uma dica importante informada pelo professor "Gustavo Guanabara", é não se preocupar com a quantidade de linha do código, e sim com a experiência do usuário.
# Solução do professor foi um pouco diferente, pois no que eu fiz eu tinha colocado uma lista dentro do dicionário, o professor fez o oposto.

galera = list()
pessoa = dict()
soma = media = 0
while True:
    # Linha feita para limpar os dados do dicionários antes de adicionar um novo, pois o novo dado será adicionado na lista.
    pessoa.clear()
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        # Lembrar de usar o ITEMS, VALUES ou KEYS. Muito útil.
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
