# Crie um programa que tenha uma "tupla" única com "nomes de produtos" e seus respectivos "preços", na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma "tabular".

lista = ('pão', 1, 'leite', 3.50, 'frango', 10.90, 'PC', 1500.00)

print('-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>8.2f}')
print('-' * 50)
