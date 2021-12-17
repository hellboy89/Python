# Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

a1 = str(input('digite o nome do primeiro aluno: '))
a2 = str(input('digite o nome do segundo aluno: '))
a3 = str(input('digite o nome do terceiro aluno: '))
a4 = str(input('digite o nome do terceiro aluno: '))

print('\no nome do aluno escolhido é {}'.format(random.choice([a1, a2, a3, a4])))
