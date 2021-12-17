"""
(OK) - Crie um programa onde o usuário possa digitar "sete valores númericos"
(OK) - e cadastre-os em uma "lista única"
(NÃO CONSEGUI, MAS SOLUÇÃO ÓBVIA) - que mantenha separados os valores "pares" e "impares".
(OK) - No final, mostre os valores "pares" e "ímpares" em ordem "crescente".
"""

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'digite o {c}ª valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'os valores pares digitados foram: {num[0]}')
print(f'os valores ímpares digitados foram: {num[1]}')

