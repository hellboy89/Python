# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

"""

Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(numero)f - Quantidade de casas decimais (float)
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)

> - esquerda
< - direita
^ - centro

"""

# colocando zeros a direita
num_1 = 1
print(f"{num_1:0>10}")

# colocando zeros a esquerda
num_2 = 1150
print(f"{num_2:0<10}")

print(f"{num_2:.2f}")

nome = "Juan Cleber"

print(nome.title())