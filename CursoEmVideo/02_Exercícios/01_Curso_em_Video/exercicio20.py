# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

a1 = str(input('digite o nome do primeiro aluno: '))
a2 = str(input('digite o nome do segundo aluno: '))
a3 = str(input('digite o nome do terceiro aluno: '))
a4 = str(input('digite o nome do quarto aluno: '))

ordem = [a1, a2, a3, a4]

shuffle(ordem)

# print(ordem)

print('a ordem de apresentação do trabalho é:\n {}'.format(ordem))
