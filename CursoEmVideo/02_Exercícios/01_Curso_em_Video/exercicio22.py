# Crie um programa que leia o nome completo de uma pessoa e mostre:

nome = str(input('digite seu nome: '))

print('o nome com todas as letras maiúsculas é {}'.format(nome.upper()))

print('o nome com todas as letras minúsculas é {}'.format(nome.lower()))

nometodoseparado = nome.replace(' ', '')

print('quantas letras ao todo (sem considerar espaços) é {}'.format(len(nometodoseparado)))

nomeseparado = nome.split()

print('quantas letras tem o primeiro nome é {}'.format(len(nomeseparado[0])))
