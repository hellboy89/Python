"""
(OK) - Crie um programa que leia 'nome, ano de nascimento e carteira de trabalho'
(OK) - e cadastre-os (com 'idade') em um 'dicionário'
(OK) - se por acaso a CTPS for diferente de 'zero', o dicionário receberá o 'ano de contratação' e o 'salário'.
(OK) - Calcule e acrescente, além da 'idade', com quantos anos a pessoa vai ser 'aposentar'.
"""
from datetime import date

cadastro = dict()
cadastro['Nome: '] = str(input('Nome: '))
cadastro['AnoNascimento: '] = int(input('Ano de Nascimento: '))
cadastro['CarteiraTrabalho: '] = int(input('Carteira de Trabalho: '))
cadastro['Idade'] = date.today().year - cadastro['AnoNascimento: ']
if cadastro['CarteiraTrabalho: '] != 0:
    cadastro['AnoContratacao: '] = int(input('Ano de Contratação: '))
    cadastro['Salario: '] = int(input('Salário: '))
if cadastro['Idade'] >= 60:
    cadastro['Aposentadoria'] = 'Sim'
else:
    cadastro['Aposentadoria'] = 'Não'
print('>>>>> CADASTRO DO FUNCIONÁRIO <<<<<')
print('=-' * 30)
print('Nome: {}'.format(cadastro['Nome: ']))
print('Idade:  {}'.format(cadastro['Idade']))
print('CTPS: {}'.format(cadastro['CarteiraTrabalho: ']))
print('Ano Contratação: {}'.format(cadastro['AnoContratacao: ']))
print('Salário: {}'.format(cadastro['Salario: ']))
print('Aposentado: {}'.format(cadastro['Aposentadoria']))
print('=-' * 30)