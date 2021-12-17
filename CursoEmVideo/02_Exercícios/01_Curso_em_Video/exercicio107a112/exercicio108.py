"""
(OK) - Adapte o código do "desafio 107", criando uma função chamada "moeda()".
(OK) - que mostre os valores como um valor monetário formatado.
"""

from utilidadesCeV import moeda

valor = int(input('Digite o preço: R$ '))
convert = str(valor).replace('.', ',0')
metade = moeda.metade(valor)
dobro = moeda.dobro(valor)
aumento10 = moeda.aumento10(valor)
print(f'A metade de R$ {convert},00 é R$ {metade}')
print(f'O dobro de R$ {convert},00 é R$ {dobro},00')
print(f'Aumentando 10% fica R$ {aumento10}')

"""
# Possível fazer o esquema abaixo para alterar a saída de um valor
# em vez de sair como o padrão que é com "." sair com ",".
 
n = 100.00
convert = str(n).replace('.', ',0')
print(convert)

TAGS:
- Criando arquivo funções (def) separado.
- Convertendo vírgula para ponto.
"""
