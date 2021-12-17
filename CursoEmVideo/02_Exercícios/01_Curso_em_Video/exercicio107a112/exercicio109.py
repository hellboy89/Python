"""
(OK) - Modifique as funções que foram criadas no "desafio 107"
(OK) - Para que elas aceitem "um parâmetro" a mais,
(OK) - Informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no 108.
"""

from utilidadesCeV import moeda

valor = float(input('qual valor: R$ '))

metade = moeda.metade(valor, sit=True)
dobro = moeda.dobro(valor, sit=True)
aumento10 = moeda.aumento10(valor, sit=True)
reduzindo13 = moeda.reduzindo13(valor, sit=True)

print(f'A metade é {metade}')
print(f'O dobro é {dobro}')
print(f'Aumentando 10% é {aumento10}')
print(f'Reduzindo 13% fica {reduzindo13}')

"""
Terei que utilizar formas opcionais de selecionar uma função. Tem um exemplo disso no "exercício105_correcao.py".
"""
