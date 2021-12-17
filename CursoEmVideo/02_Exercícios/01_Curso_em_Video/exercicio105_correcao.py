"""
(OK) - Faça um programa que tenha uma "função" "notas()" 
(OK) - que pode receber várias notas de alunos e vai retornar um "dicionário" com as seguinte informações.
(OK) - Quantidade de notas.
(OK) - A maior nota.
(OK) - A menor nota.
(OK) - A média da turna
(OK) - A situação (opcional)
(OK) - Adicione também as "docstrings" da função.
"""
print('\033c')
# Caso a 'sit' for false, ele não irá executar o if condicional mais abaixo, já encerrando sem mostrar a situação.
def notas(*n , sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita variáveis)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'boa'
        elif r['media'] >= 5:
            r['situacao'] = 'razoavel'
        else:
            r['situacao'] = 'ruim'
    return r

# Programa principal
# Se alterado a situação do "sit" para False, ele não mostra a situação do aluno.
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
# help(notas)
