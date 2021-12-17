"""
# Exemplo de FOR.
for c in range(1, 10):
    print(c, end=' ')
print('fim')
print()
# Abaixo fazendo um WHILE com o mesmo resultado do FOR acima.
# Adicionado um contador abaixo que começa por 1.
# Enquanto C for MENOR do que 10, o WHILE será executado. Assim que for 10 irá interromper.
c = 1
while c < 10:
    print(c, end=' ')
    c += 1
print('fim')
print()

============================================================================

# Quando posso usar o FOR ou o WHILE.
# O FOR só serve quando você sabe o limite do que precisa fazer.
# O WHILE é quando você não sabe o limite. E tem melhores opções de interromper.
# No exemplo do FOR abaixo é melhor simplificado.
# for c in range(0, 3):
#     n = int(input('digite um valor: '))
# print('fim')
# print()
# No exemplo abaixo não sei a quantidade, então o WHILE é melhor opção.
# O 'n != 0' é a condição de parada, quer dizer que enquanto o 'n' for diferente de '0' irá prosseguir.
# n = 1
# while n != 0:
#     n = int(input('digite um valor: '))
# print('FIM')
# print()

============================================================================

# Exemplo abaixo também pode ser feitos com Strings.
r = 'S'
# Quer dizer que enquanto 'r' for 'S', o WHILE irá executar. Qualquer outro caractér irá encerrar.
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('fim')
print()

============================================================================

# Abaixo uma forma diferente de contar os valores pares.
n = 1
# Criando um contador 0.
par = impar = 0
# O WHILE só irá interromper quando o n for 0.
while n != 0:
    n = int(input('digite um valor: '))
    # Essa condição abaixo utilizada para o 0 não entrar na contagem dos pares.
    if n != 0:
        # O resultado de qualquer número par com divisão inteira (%) por 2 é 0. Ímpar é 1.
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares.')
print(f'Você digitou {impar} números ímpares.')

============================================================================

"""

