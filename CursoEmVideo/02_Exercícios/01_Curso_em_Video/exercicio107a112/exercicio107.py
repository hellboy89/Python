"""
(OK) - Crie um módulo chamado "moeda.py"
(OK) - Que tenha as funções incorporadas: "aumentar(),
(OK) - diminuir(),
(OK) - dobro()
(OK) - e metade().
(OK) - Faça também que "importe" esse módulo e use algumas dessas funções.
"""

from utilidadesCeV import moeda

valor = float(input('digite um preço: R$ '))

metade = moeda.metade(valor)
dobro = moeda.dobro(valor)
aumento10 = moeda.aumento10(valor)
reduzindo13 = moeda.reduzindo13(valor)
print(f'A metade de {valor:.2f} é {metade:.2f}')
print(f'O dobro de {valor:.2f} é {dobro:.2f}')
print(f'Aumentando em 10%, temos {aumento10:.2f}')
print(f'Reduzindo em 13%, temos {reduzindo13:.2f}')
