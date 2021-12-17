"""


============================================================================

# Um exemplo abaixo do WHILE já visto na aula anterior.
cont = 1
# Irá executar o WHILE enquanto o cont for menor ou igual a 10.
while cont <= 10:
    print(cont, ' ', end=' ')
    # Variável abaixo contadora.
    cont += 1
print('acabou')
print()
# Mas agora é possível utilizar o WHILE 'infinito' com o TRUE.
# Utilizando o recurso do TRUE abaixo, a contagem será infinita, necessitando força interrupção.
cont = 1
while True:
    print(cont, '->', end='')
    cont += 1
print('acabou')

============================================================================

# Então para isso que existe o comando BREAK, para interromper uma WHILE.
n = 0
# Nesse exemplo abaixo, o WHILE só é interrompido quando 'n' for '999'.
while n != 999:
    n = int(input('digite um número: '))

============================================================================

# Adicionando um contador
n = cont = 0
# Enquanto o cont for menor que 3. o WHILE irá processuir.
while cont < 3:
    n = int(input('digite um número: '))
    # Irá somar mais 1 cada vez que for executado.
    cont += 1

============================================================================

n = s = 0
# Irá executar enquanto n não for 999.
while n != 999:
    n = int(input('digite um número: '))
    # O IF abaixo é para o 999 não ser somado no resultado final.
    if n == 999:
        break
    # Tive que mudar a ordem do contador abaixo para ele não contar com o 999 na soma.
    s += n
print(f'a soma dos valores é {s}!')
print()

============================================================================

# No exemplo abaixo como não tem condição de parada, o programa irá executar o WHILE infinitamente.
n = s = 0
while True:
    n = int(input('digite um número: '))
    # Mas com a condição abaixo eu interrompo ele.
    if n == 999:
        break
    s += n
# A forma de impressão abaixo é possível utilizar também desde o python 2.
print(f'a soma é {s}.')

============================================================================

#NOVA FORMA DE FORMATAÇÃO DE TEXTO USANDO O PYTHON 3.6+
nome = 'José'
idade = 33
salario = 1200
# Forma de imprimir abaixo usando o python 3.6+
print(f'o {nome} tem {idade} anos.')
# Forma de imprimir abaixo desde o python 3.
print('o {} tem {} anos.'.format(nome, idade))
# Forma de imprimir do python 2.
print('o %s tem %d anos.' % (nome, idade))
# Será utilizado mais dessa forma nova usando o FStrings.
# Se quiser que apareça com digitos só utilizar o .2f, com a quantidade de digitos após o decimal.
# O uso do ^20, irá deixar 20 de espaço entre a saída da variável.
print(f'o salário de {nome:^20} é de R$ {salario:.2f}, e ele tem {idade} anos.')
# Que também pode tá complementado com traços como abaixo.
print(f'{nome:-^20}')
# Também pode-se fazer alinhado a esquerda.
print(f'{nome:-<20}')
# Alinhado a direita.
print(f'{nome:->20}')

============================================================================

"""


