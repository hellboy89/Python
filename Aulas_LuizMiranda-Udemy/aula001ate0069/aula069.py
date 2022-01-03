# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

d1 = {x: y for x, y in enumerate(range(5))}
print(d1)

d2 = {f'chave_{x}': x**2 for x in range(5)}
print(d2)

d3 = {x: y for x, y in lista}
print(d3)

d4 = {f'chave_{y}': y**4 for y in range(10)}
print(d4)
 
