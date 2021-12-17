"""
# O IF é um condicionado que cria 2 condições ou mais dentro de uma programa, com várias possibilidades.
tempo = int(input('quantos anos tem seu carro: '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('FIM')
# Também há uma forma de fazer mais simplificada como mostrada abaixo.
tempo = int(input('quantos anos tem seu carro? '))
# Lembrando da ordem de precedência do valor.
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

============================================================================

# Forma Tradicional
nome = str(input('qual seu nome: ')).capitalize()
if nome == 'Juan':
    print(f'Que nome lindo {nome}')
else:
    print(f'Seu nome é muito comum')
# Forma Simplificada
nome = str(input('Qual seu nome: ')).capitalize()
print('que nome lindo' if nome == 'Juan' else 'Seu nome é feio')

# Forma Tradicional
n1 = float(input('digite a sua primeira nota: '))
n2 = float(input('digite a sua segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua média foi {media}')
if media >= 6:
    print('parabéns, vc passou')
else:
    print('estude mais mané.')
# Forma Simplificada
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'a sua média foi {media}')
print('vc passou' if media >= 6 else 'vc tá reprovado retarda')

============================================================================

# Também temos a opção de fazer condições aninhadas, que são o ELIF, como mostrado abaixo.
# O ELIF pode ser utilizado quando necessário informar uma condição, e não jogar o resto simplesmente para o ELSE.
# Lembrando que só pode ter um IF e um ELSE na minha condição, mas ELIF pode quantos quiser.
if carro.esquerda():
    bloco1
elif carro.direita():
    bloco2
elif carro.re():
    block3
else:
    bloco4

# Abaixo um exemplo de uma estrutura condicional aninhada.
nome = str(input('qual seu nome: ')).capitalize()
if nome == 'Juan':
    print('seu nome é muito bonito!')
elif nome == 'Denise' or nome == 'Tatiana' or nome == 'Danielly':
    print('vc tem um nome feminino')
# Sempre lembrar de utilizar o operador IN, pois ele é um poderoso recurso para filtragem de dados.
elif nome in 'Matheus Axel Rose Roberto Tonho':
    print('vc tem um nome diferenciado')
else:
    print('nome desconhecido, tente novamente mané!')

"""


