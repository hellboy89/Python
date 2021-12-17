"""

# Referência no vídeo abaixo.
# https://www.youtube.com/watch?v=9LcqETqY1kQ
# Funções tem em todo python. Por exemplo, print e input é uma função.
# Mas podemos criar a nossa próprio função com o DEF, como abaixo.
# Função tem o objetivo principal, de não precisarmos reescrever alguns códigos várias vezes, podemos ter o controle de tudo em apenas um lugar, que seria dentro das funções.
print('\033c')


def funcao():
    print('hello word')


# Print não importa o número de vezes que eu executar a função, ela irá recarregar todas.

funcao()
funcao()
funcao()
funcao()

================================================================

# Código abaixo irá gerar um erro, pois como defini um valor dentro da função, que é o "msg", é necessário repassar um valor para ela.
def funcao():
    print('hello word')
    print(msg)

funcao()

================================================================

# Lembrando que o valor que eu irei chamar dentro da função, é o mesmo que está registrado entre ().
def funcao(msg):
    print(msg)

# Sempre colocar o nome da função se quiser chamar ela de outro local. Podendo colocar vários textos que serão executados.
funcao('ola')
funcao('foda-se')
funcao('sexo')
funcao('putaria')

================================================================

# Posso chamar os valores da forma que eu quiser.
def saudacao(msg, nome):
    print(msg)
    print(nome)

saudacao('ola', 'juan')

================================================================

# se caso fizer dessa forma não irá enviar nada na tela na primeira condição do saudacao(), somente sses valores que são padrões, caso não tenha, é eles que a função irá usar abaixo.
def saudacao(msg='Olá', nome='Usuário'):
    print(msg)
    print(nome)

saudacao()
saudacao('ola', 'juan')

================================================================

# Lembrando que os valores tem que seguir essa ordem da variável como abaixo. Há não ser que eu aponte, como mais abaixo. Há não ser que eu especifique mais abaixo e troque essa ordem padrão.
def saudacao(msg='Olá', nome='Usuário'):
    print(msg, nome)

saudacao('Rose', 'Axl')
# Defina como abaixo.
saudacao(msg='Axel', nome='Rose')
saudacao('ola', 'juan')

================================================================

# Alterando valores de saída


def saudacao(msg='Olá', nome='Usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    # Não é o correto utilizar o recurso de impressão abaixo, o certo é usar o "return", que será visto mais abaixo.
    print(msg, nome)

# Entrada de valores    
saudacao('Rose', 'Axl')
saudacao(msg='Axel', nome='Rose')
saudacao('ola', 'juan')

================================================================

def saudacao(msg='Olá', nome='Usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    # Isso quer dizer que toda a saída do comando será enviada para uma variável que será declarada mais abaixo
    return f'{msg} {nome}'

# Após definida a variável, necessário realizar a impressão da mesma, com o print abaixo.
variavel = saudacao()
print(variavel)

================================================================

# Referência continuar no vídeo abaixo que é a part 2.
# https: // www.youtube.com/watch?v = T0j68JbeGJg
# Lembrando que dentro das funções só tratamos os dados da maneira que queremos, todo o valor retornado por ela, deve ser definido fora da função.

def funcao(var):
    print(var)    

funcao('faço o que quero! :)')

================================================================

def funcao(var):
    print(var)


variavel = funcao('vc não me manda!')
# Aqui no caso irá retornar com o valor "none" nessa segunda linha, pois como não tem uma função return na função, ela não envia os dados, "none" significa nulo.
print(variavel)

================================================================

# Abaixo seria a forma correta de retornar um valor da função para a variável var como no caso.
def funcao(var):
    return var
    # Para entendermos a ordem de precedência, assim que o valor return for executado, nada abaixo da função irá executar. Por isso o print ficou com valor mais claro.
    print('Isso não será executado')

variavel = funcao('vc não me manda!')

print(variavel)

================================================================

# No exemplo abaixo é possível fazer divisão no próprio "return".
def divisao(n1, n2):
    return n1 / n2

divisao = divisao(8, 2)
print(divisao)
# Como no exemplo abaixo irá retornar um valor None, é necessário realizar um tratamento mais abaixo, com condição.
# Lembrando que não é possível fazer o else dessa forma, pois depois que é encontrado a palavra "return" o python não executa mais nada que esteja na função.
def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2

# Abaixo irá gerar um erro, pois não é possível dividir o 0 por nenhum número. Mas para resolver isso é fácil, basta por uma condição dentro da função
divisao = divisao(8, 0)

# Onde irá retornar o valor 'conta inválida'.
if divisao:
    print(divisao)
else:
    print('conta inválida')

================================================================

def dumb():
    return 1

print(dumb(), type(dumb()))

def dumb2():
    # Também posso retornar uma lista, ou escrever direto no return.
    dumb = [2, 3, 4, 5]
    return dumb

dumb2 = dumb2()
print(dumb2, type(dumb2))

================================================================

def f(var):
    print(var)


def dumb():
    return f


var = dumb()
print(type(var))

print(type(f))

"""


