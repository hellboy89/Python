"""
(OK) - Crie um código em python que teste se "PUDIM" está acessível pelo computador usado.

SITE: http://pudim.com.br/
"""

from urllib.request import urlopen


def test_pudim():
    try:
        urlopen('http://pudim.com.br/', timeout=1)
        return True
    except:
        return False


teste = test_pudim()

if teste == True:
    print(f'\nConexão feita com sucesso ao site PUDIM.')
elif teste == False:
    print(f'\nConexão INVÁLIDA.')
