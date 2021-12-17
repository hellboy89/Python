"""

# Nessa aula será mostrado como trabalhar com cores no terminal.
# Existe módulo em python que trabalham com cores no terminal. Como o "Colorize", mas não iremos ver isso.
# Iremos para o básico, utilizando os próprio recursos do python, que é o ANSI (Escape Sequence).
# Então para iniciar com cores no python, tenho que iniciar com "\033[", e terminar com "m", que é uma regra de sintaxe.
# Então essa abaixo é a sintaxe completa como exemplo.
# \033[0;33;44m]
# Onde o "0" é o Style, o "33" é a cor do texto, e o "44" é a cor do fundo (background). O "m" usa no fim da string.

# STYLE:
# 0 = Para none, ou seja, valor nenhum, é o padrão.
# 1 = Para Negrito.
# 4 = Para sublinhado.
# 7 = Para negativo, irá inverter as cores do texto e do background. O que é branco vira preto e vice versa no background.

# TEXTO:
# 30 = Branco.
# 31 = Vermelho.
# 32 = Verde.
# 33 = Amarelo.
# 34 = Azul.
# 35 = Rosa.
# 36 = Azul Claro.
# 37 = Cinza.

# BACKGROUND:
# 40: Branco.
# 41: Vermelho.
# 42: Verde.
# 43: Amarelo.
# 44: Azul.
# 45: Rosa.
# 46: Azul Claro.
# 47. Cinza.

# Função x1bc como usada abaixo, serve para limpar o terminal antes da excução do código.
# print("\x1bc")
# Comando de baixo tem o mesmo objetivo, limpar o terminal.
# print('\033c')
print('\033c')
print('\033[0;30;41mTESTE')
print('\033[1;33;46mTESTE')
print('\033[1;35;43mTESTE')
print('\033[1;30;42mTESTE')
# Tem o mesmo resultado que o de cima.
print('\033[30;42mTESTE')
# Se quiser deixar na cor padrão, basta não definir ela entre parenteses como abaixo.
print('\033[mTESTE')
print()

============================================================================

# BUG VSCODE: Notei que ao colocar em negrito fica tudo cinza, mudando de cor.
# Mas para configurar melhor para as cores não irem até o final, bastar encerrar no fim do texto com \033[m, não esquecer deste comando, multo útil para não bugar o terminal.
print('\033c')
print('\033[1;36mTESTE\033[m')
print('\033[1;31mOlá mundo\033[m')
print('\033[1;31;43mOlá mundo\033[m')
print('\033[7;31;44mOlá mundo\033[m')
print('\033[4;30;45mOlá Mundo\033[m')
print('\033[30mOlá Mundo')
print('\033[1;33;44mOlá Mundo\033[m')
print('\033[7;33;44mOlá Mundo\033[m')
print()

============================================================================

# Mais um exemplo

print('\033c')

# Mais exemplos de cores, num algoritmo.
a = 3
b = 5
# Dentro de uma texto, só não esquecer de finalizar o início das cores com o \033[m, no final.
print(f'os valores são \033[32m{a}\033[m e \033[31m{b}\033[m.')

print()

============================================================================

print('\033c')
# Também é possível formatar a cor na saída da variável, como abaixo.

nome = "Juan Cleber"

# Tem uma pequena gambiarra aqui com o {} para poder encaixar os valores na posição correta.
print('Olá {}{}{}, seja bem vindo'.format('\033[4;34m', nome, '\033[m'))

print()

============================================================================

print('\033c')

# Também possível fazer um esquema com dicionários para poder importar as cores que precisa de forma fácil.

nome = "Juan Cleber"

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em tec conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))

print()

============================================================================

"""
