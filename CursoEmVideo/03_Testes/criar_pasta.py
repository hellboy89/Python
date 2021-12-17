"""
import os
perg = str(input('o que deseja fazer?'))
if perg == 'ipconfig':
    # pegar comando no CMD abaixo, sempre usar o 'cmd /k "comando"'.
    os.system('cmd /k "ipconfig & exit"')
elif perg == 'ping':
    os.system('cmd /k "ping google.com & exit"')
elif perg == 'netstat':
    os.system('cmd /k "netstat -nat & exit"')

================================================================

import os
import datetime
# os.system('cmd /k "mkdir teste"')
# Para imprimir uma data completa pode usar o comando abaixo.
data = datetime.datetime.now()
# saída como ao lado: 2021-05-20 12:07:53.466262
print(data)

import os
import datetime
# os.system('cmd /k "mkdir teste"')
# Comando abaixo já filtra um pouco menos, mas necessário colocar na ordem correta.
date = datetime.datetime(2020, 5, 17)
# saída como ao lado: 2020-05-17 00:00:00
print(date)

import os
import datetime
date = datetime.datetime.now()
# CERTINHO: Nesse já pega a data do jeito certo com dia, mês e ano.
print(date.strftime("%d-%m-%y"))
# saída: 20-05-21

================================================================

# ALGORITMO FUNCIONAL ABAIXO PARA CRIAR PASTA NO WINDOWS
import os
# Primeiro necessário definir o nome do diretório.
directory = 'GeekforGeek'
# Após isso necessário para dentro do diretório onde será criado o arquivo. LEMBRAR QUE AS BARRAS SÃO INVERÇAS.
parent_dir = "C:/Users/jcleber/Desktop/python/teste_criarpasta/"
# Depois será feito uma junção entre o diretório que será criado e o caminho.
os.path = os.path.join(parent_dir, directory)
# Após isso irá iniciar a criação com o comando os.mkdir.
os.mkdir(os.path)

================================================================

# SELECIONANDO DATA DE DIAS ATRÁS. 
import os
import datetime
# Para pegar data de dias atrás é necessário fazer como abaixo.
# Criando uma variável com a data atual.
hoje = datetime.date.today()
# Após isso fazer um calculo com o operador TIMEDELTA, que fazer parte do módulo 'datetime'.
ontem = hoje - datetime.timedelta(days=7)
print(ontem)

"""

# ALGORITOMO DE COMO CRIAR UMA PASTA COM A DATA ATUAL NO WINDOWS.

import os
diretorio = 'teste123'

parent_dir = "C:/Users/jcleber/Desktop/python/teste_criarpasta/"

os.path = os.path.join(parent_dir, diretorio)

os.mkdir(os.path)


# TENTANDO CRIAR UMA CONDIÇÃO PARA CASO O DIRETÓRIO JÁ EXISTIR, ELE INFORMAR UM AVISO, MAS DANDO ERRO POIS A FUNÇÃO 'EXISTS' NÃO TEM MAIS. NECESSÁRIO PESQUISAR!...
# A PARTE DE CRIAÇÃO DA PASTA TÁ CERTINHO, SÓ DANDO RUIM NA CONDIÇÃO DO 'EXISTS'.