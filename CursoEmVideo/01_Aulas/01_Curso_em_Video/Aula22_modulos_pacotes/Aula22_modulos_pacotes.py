"""

# MODULARIZAÇÃO: Assunto dessa aula, a função da modularização é dividir um programa muito grande para fácil entendimento e manutenção. Muito utilizado nas empresas.
# Por isso é chamado "modularização", pois a idéia é dividir o programa em módulos, aumetando muito a legibilidade do código.
# Uma coisa que é mais interessante da modularização, é dividir um problema que seja muito grande, em pequenos problemas, e resolve-los aos poucos.

============================================================================

# Então um exemplo do código abaixo, ainda é um código pequeno, mas caso ele cresça demais, uma boa opção para a modularização é colocar partes dele em outros arquivos, ou seja, definir a função em arquivos diferentes.
# Então como estamos colocando todos os DEFs em outro arquivo, é necessário importar as funcionalidades dele para este arquivo, utilizando o "IMPORT" como abaixo.
# No VSCODE, não me deu opção de preenchimento automático ao colocar o nome do diretório no import, tive que preencher manualmente. Não esquecer também de mudar nas funções abaixo o nome também do Módulo.
# O Python tem milhões de módulos que é possível importar, dessa forma que fiz agora, estou importando meu próprio módulo de funções.

import uteis
# Também é possível importar só as funções abaixo como mostrado.
# Só lembrando que dessa forma abaixo feita, não é o recomendável pelo Python, pois pode dar incompatibilidade caso eu tenha outras DEFs que possuam o mesmo nome. Sempre é recomendado importar a função inteira, como acima.
from uteis import fatorial, dobro, triplo

num = int(input('digite um valor: '))
fat = fatorial(num)
print(f'o fatorial de {num} é {fat} ')
print(f'o dobro de {num} é {dobro(num)}')
print(f'o tripo de {num} é {triplo(num)}')

============================================================================

# VANTAGENS MODULARIZAÇÃO:
# - Organizaçaõ do código.
# - Facilidade na manutenção.
# - Ocultação de código detalhado.
# - Reutilizar em outros projetos. 

# Mas se caso um programa crescer demais e apenas os módulos não puderem satisfazer é possível utilizar os PACOTES, que também chamado de BIBLIOTECAS.

# PACOTES tem o objetivo de organizar todas as nossas DEFs (FUNÇÕES), organizar da forma que quisermos como por número, datas, cores, strings... Como no detalhe abaixo.

# ===================PACOTE UTEIS==================
# NÚMEROS       DATAS       CORES        STRINGS
# def xyz():    def xua():  def ab():    def teste():
# def abc():    def hehe(): def cri():   def te():
# def vam():    def fal():  def han():   def am():
# ==================================================

# É isso como acima é organizar todos os DEFs de uma forma que seja lógica.
# Para importar um PACOTE é da mesma forma que os MÓDULOS, basta utilizar o "import".
# Ou por exemplo só partes dele como "from uteis import cores", onde irá importar só a coluna de cores da terceira aba. Ou vários outros no mesmo projeto.
# Então para criar um PACOTE é bem simples, pois toda divisão utilizada nos IDEs, é feita por pasta, seria mais ou menos como mostrado no esquema abaixo.

# (PASTA) PACOTE UTEIS
        #__init__.py (ACHAR ARQUIVOS NO PACOTE)
    # (SUBPASTA) CORES
            #__init__.py (ACHAR ARQUIVOS NO PACOTE)
    # (SUBPASTA) DATAS
            #__init__.py (ACHAR ARQUIVOS NO PACOTE)
    # (SUBPASTA) NÚMEROS
            #__init__.py (ACHAR ARQUIVOS NO PACOTE)
    # (SUBPASTA) STRINGS
            #__init__.py (ACHAR ARQUIVOS NO PACOTE)

# Onde a pasta principal é o PACOTE e as subpastas os MÓDULOS, com os arquivos *.py em cada um deles.
# E pra achar arquivos específicos dentro dos pacotes, os mesmos tem a nomenclatura "__init__.py", como mostrado no esquema acima.
# Criei essa mesma estrutura pelo meu VSCode, vamos ver se funciona.

# Usando o comando abaixo estou importando da pasta principal "uteis" o diretório numeros, indo direto para o arquivo __init__.py

from uteis import numeros

num = int(input('digite um valor: '))
fat = numeros.fatorial(num)
print(f'o fatorial de {num} é {fat} ')
print(f'o dobro de {num} é {numeros.dobro(num)}')
print(f'o tripo de {num} é {numeros.triplo(num)}')


"""

