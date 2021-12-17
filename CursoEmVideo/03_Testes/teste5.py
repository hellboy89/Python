"""

lista = [1, 2, 3, 4]
lista2 = [1, 2, 4, 5]
lista3 = list()

for c in range(0, 3):
    n = int(input('informe um valor: '))
    lista3.append(n)
print(lista3)

================================================================

import datetime
import os
print('\033c')


# ====> PEGAR DATA DE HOJE

param_hoje = datetime.datetime.now()
data_hoje = param_hoje.strftime("%d-%m-%y")
# print(data_hoje)

# os.system('cmd /k "mkdir teste"')
os.system(command='ipconfig')
os.system()
# ====> CRIAÇÃO DE DIRETÓRIO (USANDO MÓDULO OS)

directory = data_hoje

parent_dir = "E:/TEMP/teste_criapasta/"

os.path = os.path.join(parent_dir, directory)

# Abaixo irá criar a pasta.
os.mkdir(os.path)


# Comando abaixo irá remover a pasta.
# os.rmdir(os.path)
lista = [7, 74, 106]
print(type(lista))
print(max(lista))

print('\033c')

from math import sqrt

calc = (5.0 - 1.0)**2 + (9.0 - 7.0)**2
#       x2    x1         y2    y1
print(sqrt(calc))
"""

teste = 10 + 10

print(teste)
