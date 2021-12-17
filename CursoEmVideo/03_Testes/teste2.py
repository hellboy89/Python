"""

dados = dict()
lista = list()

dados['nome'] = str(input('qual o nome do jogador: ')).title()
dados['quant_parti'] = int(input(f'qual a quantidade de partidas jogadas por {dados["nome"]}: '))
dados['soma_gols'] = 0

for c in range(1, dados['quant_parti'] + 1):
    lista.append(int(input(f'quantos gols fez na {c} partida: ')))
dados['gols_part'] = lista[:]
# CALCULAR A SOMA DOS GOLS
for i, v in enumerate(dados['gols_part']):
    dados['soma_gols'] += v
# =========================
print('-=' * 30)
print(dados)
print('-=' * 30)
print(f'O nome do jogador é: {dados["nome"]}')
print(f'O campo gols é: {dados["gols_part"]}')
print(f'O campo total foi: {dados["soma_gols"]}')
print('=-' * 30)
print(f'O jogador {dados["nome"]} jogou {dados["quant_parti"]} partidas.')
# APONTAR A QUANTIDADE DE GOLS PARA CADA PARTIDA.
for c in range(0, dados['quant_parti']):
    print(f'     => Na partida {c}, fez {dados["gols_part"][c]} gols.')
print(f'Somandos todos os gols foram {dados["soma_gols"]}.')

============================================================================

# TESTES EXERCÍCIO 97

# Aqui mostra a quantidade de caractéres que tem em  'ola, mundo'.
# olamundo = 'ola, mundo'
# print(len(olamundo))
# SAÍDA: 10

def escreva(sms):
    q_trac = '=-'
    carac = len(escreva)
    trac = len(q_trac)
        if <

escreva('ola, mundo')


# TÔ COM DIFICULDADE DE DESENVOLVER A IDÉIA. MAS QUERIA QUE FOSSE FEITO UMA CONTAGEM DE CARACTÉRES QUE TEM NO ESCREVA, E DEPOIS FOSSE ADICIONADO O '-=' DE ACORDO COM A QUANTIDADE DE CARACTÉRES. PRINCIPALMENTE TERIA QUE UTILIZAR O "LEN".

try:
    a = int(input('digite o valor de A: '))
    b = int(input('digite o valor de B: '))
    media = (a + b) / 2
except ():
    print(f'deu ruim mané, o erro foi {err}')
else:
    print(media)
finally:
    print('\nvolte sempre mané!')


teste1 = "ola criança"

print('ola1')
print('ola2')
print(teste1)
print('ola4')


x = int(input())
y = int(input())

maior = x if x > y else y
menor = y if y < x else x
menor += 1
soma = 0

while (menor < maior):
    if (menor % 2 != 0):
        soma += menor
    menor += 1
print(soma)


n = int(input())

for i in range(1, n + 1):
    x = input().split()
    a, b, c = x
    print('{:.1f}'.format((float(a) * 2 + float(b) * 3 + float(c) * 5) / 10))
"""

# Python code to demonstrate naive method
# to compute factorial
n = 4
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("The factorial of 23 is : ", end="")
print(fact)
