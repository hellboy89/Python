"""
(FAÇO NEM IDÉIA) - Crie um programa onde o usuário digite uma "expressão" qualquer que use "parênteses".
(FAÇO NEM IDÉIA) - Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na "ordem correta".
"""

expr = str(input('digite a expressao: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressão está válida!')
else:
    print('sua expressão está errada!')
