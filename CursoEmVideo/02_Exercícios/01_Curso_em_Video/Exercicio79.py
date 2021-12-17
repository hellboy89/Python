"""
(OK) - Crie um programa onde o usuário possa digitar vários "valores numéricos"
(OK) - e cadastre-os em uma "lista".
(OK, NÃO CONSEGUI SOZINHO) - Caso o número já exista lá dentro, ele "não será adicionado".
(OK) - No final, serão exibidos todos os "valores únicos" digitados, em "ordem crescente".
"""

num = list()

while True:
    n = int(input('digite um valor: '))
    # abaixo irá verificar se o valor de n já existe no num, se caso não, irá adicionar, ao contrário irá avisar.
    if n not in num:
        num.append(n)
        print('valor adicionado com sucesso...')
    else:
        print('valor duplicado, não adicionado...')
    perg = str(input('quer continuar? '))
    if perg == 'n':
        break

num.sort()
print('os valores informados foram: {}'.format(num))
