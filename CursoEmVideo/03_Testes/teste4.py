"""

# TENTATIVA DE RESOLUÇÃO DO EXERCÍCIO 102, MAS AINDA INCOMPLETO.

print('\033c')

num = 10
num_list = list()

f = 1
for c in range(num, 0, -1):
    f *= c

print(f'valor do fatorial é {f}.\n')

# for i, v in enumerate(num_list):
#     print(i, v)
contador = -1
for c in range(1, num):
    contador += 1
    num_list.append(contador)

print(num_list[::-1],'\n')

print(f'{num} x', end=' ')
for i, v in enumerate(num_list[::-1]):
    print(v+1, end=' x ')
print('FIM', end=' ')
print(f' = {f}')


print()

# CONSEGUI CHEGAR NUM RESULTADO MAIS OU MENOS ACEITÁVEL PARA PEGAR O FATORIAL, MAS AINDA EM TESTES.
# TENHO QUE CRIAR UM VALOR SEQUENCIAL QUE MOSTRE GRAFICAMENTE O FATORIAL DE UM NÚMERO COMO 4! = 4x3x2x1 = 24.
# TENHO QUE IR POR PARTES.
# TALVEZ A IDÉIA SEJA COLOCAR TODOS OS VALORES DO FATORIAL NUMA LISTA, O QUE ESTOU TENTANDO FAZER.

============================================================================

print('\033c')
teste = input('diga algo: ')
print(teste)

# Python Program to Convert seconds
# into hours, minutes and seconds

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


# Driver program
n = 140153
print(convert(n))


import traceback

try:
    a = int(input('valor A: '))
    b = int(input('valor B: '))
    media = (a + b) / 2
except Exception as erro:
    print(f'deu ruim no "{erro}"')
else:
    print(f'a média é {media}')
finally:
    print(f'\n\nVOLTE SEMPRE')

============================================================================

===========> SALVAR ARQUIVO NO TXT

# Comando abaixo para fazer a ESCRITA no arquivo.
# Se o arquivo não existir, ele irá criar.
with open('exercicio115_create.txt', 'w') as f:
    f.write('readme2\n')
    f.write('juan\n')
    f.write('juan3\n')
    f.write('teste5\n')
    f.write('hehe mané\n')
    f.close()

# Adicionar uma NOVA LINHA.
with open('exercicio115_correcao.txt', 'a') as new:
    new.write('teste nova linha')
    new.close()

# Comando abaixo para LER o arquivo.
with open('exercicio115_correcao.txt', 'r') as file:
    var = file.read()
    print(var)
    file.close()
"""


def dadosTXT(nome, idade):
    try:
        while True:
            with open('teste7.txt', 'a') as file:
                file.write(f'Nome: {nome}')
                file.write('\n')
                file.write(f'Idade: {idade}')
                file.write('\n')
                file.close()
            perg = input('que parar? [S/N] ')
            if perg in 'Nn':
                break
    except Exception as erro:
        print(f'deu ruim no {erro}')


nome = input('qual seu NOME: ')
idade = input('qual sua IDADE: ')
dados_func = dadosTXT(nome, idade)
print(dados_func)

with open('teste7.txt', 'r') as ler:
    var = ler.read()
    print(var)
    ler.close()
