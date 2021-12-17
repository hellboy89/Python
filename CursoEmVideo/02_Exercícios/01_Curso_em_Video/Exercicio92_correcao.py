"""
(OK) - Crie um programa que leia 'nome, ano de nascimento e carteira de trabalho'
(OK) - e cadastre-os (com 'idade') em um 'dicionário'
(OK) - se por acaso a CTPS for diferente de 'zero', o dicionário receberá o 'ano de contratação' e o 'salário'.
(OK) - Calcule e acrescente, além da 'idade', com quantos anos a pessoa vai ser 'aposentar'.
"""

from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
# A variável abaixo esta de fora do dicionário.
nasc = int(input('Ano de nascimento: '))
# Foi colocado de fora para ser utilizado abaixo. Mas poderia fazer mesmo dentro do dicionário.
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
# Está feito em partes, abaixo se o valor do CTPS for 0, ele já finaliza e não continua o resto do código.
# Fazendo com que o código seja mais leve e enxuto.
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('ano de contratacao: '))
    dados['salario'] = float(input('salário: R$ '))
    # Aqui será feito um cálculo para descobrir se o funcionário já está aposentado.
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
