"""
(OK) - Faça um programa que tenha uma "função" "notas()" 
() - que pode receber várias notas de alunos e vai retornar um "dicionário" com as seguinte informações.
() - Quantidade de notas.
() - A maior nota.
() - A menor nota.
() - A média da turna
() - A situação (opcional)
() - Adicione também as "docstrings" da função.
"""

print('\033c')


def notas(* alunos):
    alunos = list()
    print(alunos)
    print(type(alunos))

# Programa Principal


notas([1, 5, 2, 5])

print()
# PRECISO FAZER UM DICIONÁRIO QUE VAI RECEBER AS NOTAS DOS ALUNOS, O DICIONÁRIO VAI ESTAR NO "DEF", MAS A ENTRADA DE DADOS ESTARÁ EM "PROGRAMA PRINCIPAL".
