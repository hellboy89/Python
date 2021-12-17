"""
# O último número é sempre excluído da contagem.
for c in range(1, 5):
    print(c, end=' ')
print()
# Digitando OI 4 vezes.
for c in range(0, 4):
    print('oi')
print()
# Não esquecer da indentação, tudo que estiver dentro dela, fará parte do FOR.
for c in range(0, 3):
    print('oi')
    print('fim')
print('agora sim.. FIM!')
print()
# Fazendo contagem de 0 à 9.
for c in range(0, 10):
    print(c, end=' ')
print()
# Possível fazer a contagem inversa. Com o END=' ', deixo tudo na mesma linha.
# Lembrar que sempre possível fazer contagem inversa no Python, com o parâmetro -1.
for c in range(6, 0, -1):
    print(c, end=' ')
print()
# Também possível fazer a contagem pulando de 2 em 2.
for c in range(0, 10, 2):
    print(c, end=' ')
print()
# Pulando de 3 em 3.
for c in range(0, 10, 3):
    print(c, end=' ')

============================================================================

# Executando um contador a partir de uma entrada.
n = 10
for c in range(1, n):
    print(c, end=' ')
print()
# Por exemplo não é possível fazer até outros tipos de entrada, como mudar os passos.
inicio = int(input('digite o inicio: '))
fim = int(input('digite o fim: '))
passo = int(input('digite os passos: '))
# Somente o último que ele remove, por isso a importância do +1.
for c in range(inicio, fim+1, passo):
    print(c, end=' ')

============================================================================

# Para fazer um contador é possível sempre criando uma variável 0.
dados = 0
for c in range(0, 3):
    n = int(input('digite um número: '))
    # Com os dados abaixo, irá somar o valor de N, na variável dados, toda vez que executar o FOR.
    dados += n
print(f'O somário de todos foi {dados}.')
print()

============================================================================

"""

