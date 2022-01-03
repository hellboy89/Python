# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

texto = "Python"

# utilizando o enumerate para criar indices.
for n, letra in enumerate(texto):
    print(n, letra)

"""
For in Python
Iterando srings com for
Função range(start=0, stop, step=1)
"""

# for tradicional com contador.
for numero in range(10):
    print(numero, end=' ')

# Irá contar de 20 até 10.
for numero in range(20, 10, -1):
    print(numero, end=' ')

for numero in range(5, 100, 8):
    print(numero, end=' ')
 
 