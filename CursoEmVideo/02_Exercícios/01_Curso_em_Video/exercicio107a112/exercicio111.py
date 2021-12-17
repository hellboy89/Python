"""
(OK) - Crie um "pacote" chamado "utilidadesCeV"
(OK) - Que tenha dois "módulos interno" chamados "moeda" e "dado".
(OK) - Transfira todas as funções utilizadas nos "desafios 107, 108 e 109"
     para o primeiro pacote e mantenha tudo funcionando.
"""

from utilidadesCeV import moedas

valor = 500

teste = moedas.reducao35(valor, sit=True)
print(teste)

"""
TAGS:
- exemplos de pacotes
- importando módulos e pacotes
"""