"""
(OK) - Faça um programa que leia 'nome e média' de um aluno,
(OK) - Guardando também a 'situação' em um 'dicionário'.
(OK) - No final, mostre o conteúdo da estrutura na tela.
"""

# Dados tem que contar o NOME e MÉDIA.
dados = dict()
dados['nome'] = str(input('Insira o nome: '))
dados['media'] = float(input('Insira a média: '))
# só lembrara aqui de mudar, pois se a CHAVE tiver dentro de aspas simples vai dar erro, tenho que trocar para duplas, pois ele já está dentro de uma aspa simples.
print('A {} teve média {}.'.format(dados['nome'], dados['media']))
if dados['media'] >= 6:
    dados['situacao'] = 'APROVADO'
else:
    dados['situacao'] = 'REPROVADO'
print(f'O {dados["nome"]} ficou com a média {dados["media"]}, então foi {dados["situacao"]}')

# SOLUÇÃO DO PROFESSOR ABAIXO PARA O FINAL.
# Utilizando o FOR com o ITEMS para mostrar mais organizado. Sem a necessidade do enumerate.
print('-=' * 30)
for k, v in dados.items():
    print(f'{k} é igual à {v}')

# REPOSTA: {'nome': 'juan', 'media': 10.0, 'situacao': 'APROVADO'}