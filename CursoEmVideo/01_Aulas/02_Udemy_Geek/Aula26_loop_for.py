"""

# FOR é uma estruturação de repetição.
# Em C ou Java, se escreve abaixo.
# for(int i = 0; i < 10; i++) {
# //Execução do Loop
# }

# Mas em python funcion de maneira mais simples.
# for item in interavel:
#   //execucao do loop.

# Loop é utlizado para iterar sobre sequências ou sobre valores iteráveis.
# Que são valores que podem ser separados, como no exemplo abaixo, na qual imprimos somente a letra G.
nome = 'Geek University'
print(nome[0])

# Exemplos de Iteráveis:
# - String: nome = 'Geek University'
# - Lista: lista = {1, 3, 5, 7, 9}
# - Range: numeros = range (1, 10

============================================================================

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # será transformado em uma lista.
# Exemplo de FOR 1. Usando iteráveis na String
for letra in nome:
    print(letra, end=' ')
print()
# Exemplo de FOR 2. Iterando em uma lista.
for numeros in lista:
    print(numeros, end=' ')
print()
# Exemplo de FOR 3. Iterando em um range. (Ele excluí o último número).
# Então começa do 1 e vai até o 9.
for numeros in range(1, 10):
    print(numeros, end=' ')
print()
# FOR de trás para frente. Pegando pela variável principal 'NOME'.
for letras_inv in nome[::-1]:
    print(letras_inv, end=' ')

============================================================================

# Possível também visualizar melhor os índices dos números. Exemplo abaixo.
nome = 'Geek University'
# Para isso pode ser utilizado o enumerate como abaixo.
# O I significa íncice, onde ele irá marcar a posição da saída da variável. O V seria o conteúdo da variável.
# Não precisa obrigatoriamente ser essas letras, mas só se ligar nas posições.
for i, v in enumerate(nome):
    print(i, '->', v)
print()
# Possíve também pedir ajuda ao terminal do python, caso precise de ajuda com algum parâmetro como abaixo.
help(enumerate)
# Mais exemplo abaixo.
for indice, letra in enumerate(nome):
    print(nome[indice])
# Outro exemplo.
nome = 'Geek University'
for _, letra in enumerate(nome):
    print(_, '->', letra)

============================================================================

# Também possível pegar o ENUMERATE sem o índice, apenas definindo somente um valor depois do FOR.
nome = 'Geek University'
for valor in enumerate(nome):
    print(valor)
print()
# Se eu quiser pegar só os índices.
for valor in enumerate(nome):
    print(valor[0])
print()

============================================================================

# Definindo o número de vezes que será executado
# qtd = int(input('quantos loops vc quer: '))
# for n in range(0, qtd+1):
#     print(f'Imprimindo {n} vezes.')
# Utilizando uma variável contadora.
qtd = int(input('quantos loops: '))
soma = 0
for n in range(1, qtd + 1):
    n = int(input('digite um número: '))
    # toda vez que executado o FOR, irá pegar o valor de N e somar na variável 'soma'.
    soma += n
print(f'a soma de todos os valores é {soma}')

============================================================================

# Se quiser imprimir toda a saída na mesma linha, só usar o end=''.
nome = 'Geek University'
for letra in nome:
    print(letra, end=' ')
# Se quiser mais informações também pode pedir ajuda ao terminal.
help(print)

============================================================================

# Uma dica interessante na utilização do PYCHARM, é a tecla CTRL, só apertar e clicar no valor.
# Que o PYCHARM irá mostrar mais informações sobre os mesmos.
teste = 1
for i, v in enumerate(teste):
    print(i, v)
print(teste)

============================================================================

# Tabela de Emojis Unicode:
# https://apps.timwhitlock.info/emoji/tables/unicode
# Para imprimir caractéres Unicode, necessário isso abaixo.
# Código Original: U+1F604
# Código Modificado: U0001F604 (Substituir o + por 000)
for num in range(1, 11):
    print('\U0001F604' * num)
print('\U0001F60D')
# Diversão
n = int(input('quer imprimir quantas vezes: '))
for c in range(1, n+1):
    print('\U0001F624' * 20)

============================================================================

"""

