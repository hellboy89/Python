"""

# As funções servem para adicionar uma rotina, ou seja uma tarefa que iremos fazer repetidamente.
# Atualmente o próprio python já possui funções, como o print, float, int. Entre outros. Agoram serão mostrados nessa aula como criar uma rotina mais complexa e com novas funcionalidades.
# No python a rotina ou função é iniciada com a nomenclatura abaixo.

def mostraLinha():
    print('------------------------------')
def sistemaAlunos():
    print('     SISTEMAS DE ALUNOS     ')
def sistemaCadastro():
    print('     CADASTRO DE FUNCIONARIO     ')
def erroSistemas():
    print('     ERRO DO SISTEMA     ')
    

# O parâmetro acima pode ser mostrado novamente simplesmente chamando a função abaixo. Desse jeito em qualquer lugar do meu código eu posso chamar a função criada acima, com o DEF.
# Mais exemplificado abaixo. Onde irei chamar uma função na linha de baixo, deixando o código mais objetivo e organizado.

mostraLinha()
sistemaAlunos()
mostraLinha()
sistemaCadastro()
mostraLinha()
erroSistemas()
mostraLinha()

============================================================================

# Uma outra forma de realizar o processo, utilizando o recurso de MENSAGENS (MSG), como mostrado mais detalhadamente abaixo.
# Nâo precisa ter exatamente o nome de 'mensagem' é só um apontador, nem o nome de 'msg'.
def mensagem(msg):
    print('----------')
    print(msg)
    print('---------')

mensagem('SISTEMA DE ALUNOS')
mensagem('SISTEMA DE CADASTRO')
mensagem('ERRO no SISTEMA')

def sobrenomes(juan):
    print('-=' * 30)
    print(juan)
    print('-=' * 30)
# O que ele irá fazer é imprimir o primeiro 'def' na sequência, trocando o print pelos nomes abaixo. E irá fazer isso após cada entrada que eu adicionei abaixo.
sobrenomes('JUAN')
sobrenomes('CLEBER')
sobrenomes('FARIA')
sobrenomes('ALVES')

============================================================================

# Também há uma forma mais prática de realizar calculos, como mostrado abaixo.
# Entre parênteses após a criação da função necessário apontar a posição das variáveis que irão entrar.
def soma(a, b, c):
    print(f'A = {a}, B = {b} e C = {c}')
    s = a + b + c
    media = s / 3
    print(f'A média é {media}')
# Somente irei apontar os valores abaixo separado por vírgula, se foram mais de um, só adicionar.
soma(4, 5, 10)
soma(8, 9, 5)
soma(2, 1, 30)
# A linha abaixo irá gerar um erro, pois soma tem que receber 4 valores separados por vírgula
# soma(4)
# Hà uma outra forma de definir a soma também para ficar mais explícito, como abaixo.
soma(a=4, b=5, c=25) 
# Se quiser também é possível mudar a ordem, como abaixo.
soma(c=20, b=14, a=30)

============================================================================

# O python tem uma funcionlidade na função chamada EMPACOTADOR, que serve para colocar vários valóres no DEF, como mostrado abaixo.
# Desse modo eu posso receber vários valores, sem seguir a regra mostrada anteriormente onde eu tenho váriáveis específicas.
# Lembrando que o * no DEF significa que ele irá DESEMPACOTAR os valores de entrada.
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2,1,7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

============================================================================

def dobra(lst):
    # Aqui ele irá fazer um contador.
    pos = 0
    # Pois os while só vai ser executado enquanto a quantidade de valores for menos que a lista.
    while pos < len(lst):
        # Aqui ele já irá fazer a multiplicação.
        lst[pos] *= 2
        # Aqui é o contador que irá parar a função quando ele atender a necessidade do While.
        pos += 1

# Abaixo é os valores da lista.
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

============================================================================

# Somando valores usando funções (DEF).
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.') 

soma(5, 2)
soma(2, 9, 4)

============================================================================

# INTERACTIVE HELP
# É uma forma de pedir ajuda ao python se caso tiver dúvida com a execução de algum comando, ela pode ser utilizada com a sintaxe abaixo.
# help()
# Que também é uma função, tudo que tem () no final é uma função no python.
# Se quiser pode digitar a busca abaixo e selecionar diretamente no vscode o comando SHIFT + ENTER, que irá rodar no terminal
# LEMBRANDO QUE PRECISO ESTAR NO MODO DE "HELP" DO PYTHON, apenas digitando "help()".

help(print)
help(max)
help(enumerate)
help(len)
help(input)

# Se quiser SAIR da ajuda interativa, basta digitar "quit".

============================================================================

# Também é possível pegar uma documentação utilizando a sintaxe abaixo, seguido de __doc__.
# Ele não mostra necessariamente as mesmas informações que os parâmetros "help()", mas é algo se precisar também.
# print(print.__doc__)
# print(input.__doc__)

============================================================================

# DOCSTRINGS: Que é basicamente uma string de documentação.
# Serve para criar uma pequena documentação da funçõa que criei como mostrado abaixo.
from time import sleep

# O docstrings começa extamente em baixo da função, e se inicia pelo comentário de aspas triplas (""" """).


def contador(i, f, p):
    #ASPAS TRIPLAS
    #TIVE QUE COLOCAR ESSE "#" POIS NÃO É POSSÍVEL COLOCAR ASPAS TRIPLAS DENTRO DE ASPAS TRIPLAS
    #Contador que conta o inicio, fim e passo. Apenas digitando valores pretendidos.
    #i de inicio
    #f de fim
    #p de contador
    #ASPAS TRIPLAS
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.2)


contador(
    int(input('inicio:  ')),
    int(input('fim:     ')),
    int(input('passo:   '))
)
# Abaixo é a função "help" utilizada para chamar a doc da função, apontando para o nome da própria função.
help(contador)

============================================================================

# Mais um exemplo de docstrings.


def contador(i, f, p):
    # ASPAS TRIPLAS
    -> Faz uma contagem e mostra na tela.
    Testes
    # ASPAS TRIPLAS
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)

============================================================================

# PARÂMETROS OPCIONAIS: São utilizados quando "não quero" passar o valor de um parâmetro para a função, como no exemplo abaixo.

# Os "PARÂMETROS OPCIONAIS" são declarados aqui, dando o valor 0 para a variável, como no "c=0".
# Também pode ser substituído pelo DESEMPACOTAMENTO, utilizando a função *, antes da variável. Só em alguns casos é possível utilizar os "PARÂMETROS OPCIONAIS".


def somar(a, b, c=0):
    s = a + b + c
    print(f'a soma vale {s}.')


somar(3, 2, 5)
somar(8, 4)

============================================================================

# Mais um exemplo de "PARÂMETROS OPCIONAIS", como abaixo.
# Onde é possível colocar todos os valores como nulos, "caso eles não tenham valores".


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'a soma vale {s}.')


somar(3, 2, 5)
somar(8, 4)
# Sem os parâmetros opcionais informados acima, os valores abaixo retornariam um erro na FUNÇÃO.
somar()

============================================================================

# Mais um exemplo de "PARÂMETROS OPCIONAIS".


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'a soma vale {s}.')


# Aqui como só tenho os valores e "b" e "c", ele irá preencher na função, como não tem "a", então vai ser 0.
# Se caso a quantidade de valores for maior do que isso, é melhor usar o "*" na função.
somar(b=4, c=2)

============================================================================

# ESCOPO DE VARIÁVEIS: É basicamente um local onde a variável irá existir, e também deixar de existir...
# Variável Global: São variáveis que podem ser utilizadas em todos os lugares do código.
# Variável Local: São variáveis que são utilizadas apenas de locais específicos, como dentro de uma função...


def teste():
    x = 8
    print(f'na função teste, n vale {n}.')
    print(f'na função teste, x vale {x}')


# Programa principal
n = 10
# O print abaixo irá funcionar certinho, pois é uma variável "global", pode ser utilizado em qualquer lugar, até dentro das funções.
print(f'no programa principal, n vale {n}.')
# Irá retornar um erro no "print" abaixo, pois o X somente foi declado dentro da função, então ele é uma variável "local".
print(f'no programa principal, x vale {x}.')

============================================================================

# Mais um exemplo abaixo de "ESCOPO DE VARIÁVEIS".
# Como exemplificado abaixo o A tem dois valores, fora da função vale 5, dentro vale 8. Então ele irá pegar o valor que está mais próximo do recurso onde tá sendo utilizado.

def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')


a = 5
teste(a)
print(f'A fora vale {a}.')

============================================================================

# Mais um exemplo de "ESCOPO DE VARIÁVEIS", o N dentro da função, não afeta o N fora da função.

def funcao():
    n = 30
    print(f'N dentro vale {n}.')


n = 50
print(f'N fora vale {n}.')
funcao()

============================================================================

# No "ESCOPO DE VARIÁVEIS" tem uma forma de fazer com que uma variável global, também funcione dentro da variável local que tenha o mesmo valor, apenas fazendo algo como mostrado abaixo.


def teste(b):
    # Com o parâmetro abaixo ele irá substituir a variável local dentro do def, pela "global"
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')


a = 5
teste(a)
print(f'A fora vale {a}')

============================================================================

# RETORNO DE VALORES: Serve para retornar os valores dentro das variáveis, será mostrado melhor abaixo.
# Pode ser usado com o parâmetro "return".


def somar(a=0, b=0, c=0):
    s = a + b + c
    # A função abaixo "return s" irá retornar o resultado para a função de somar descrita abaixo. Sendo assim tenho que modificar a declaração abaixo, com um print.
    return s


# Pode ser utilizado como abaixo.
print(somar(3, 2, 5))

# Como abaixo também criando dentro de uma variável.
resp = somar(3, 2, 5)
print(resp)

# Ou assim também.
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
soma = r2 + r2 + r3
print(soma)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')

============================================================================

# Mais um exemplo de RETORNO DE VALORES.


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('digite um valor: '))
print(f'O valor do fatorial de {n} é igual a {fatorial(n)}')

# Também pode ser feito com abaixo.
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'os resultados são {f1}, {f2} e {f3}.')

============================================================================

# Exemplo de RETORNO DE VALORES, com valore booleanos.


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('digite um número: '))
# Aqui ele irá mandar o valor de "num" para dentro da função.
print(par(num))

# Outro modo com IF.
if par(num):
    print('É par!')
else:
    print('Não é par!')

"""

