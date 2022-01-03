# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

# o valor * significa que todas as variáveis serão empacotadas 
# para uma lista

def teste(*val):
    print(val)
    print(val[0])

teste(1, 2, 3, 4, 5)

# os kwargs como abaixo, são argumentos nomeados, como mostrado no exemplo
# mais abaixo. Que entram na variável como dicionários.

def func(*args, **kwargs):
    print(args)
    print(kwargs)
    soma = 0
    for v in args:
        soma += v
    print(f"a soma dos args é: {soma}")

func(1, 2, 3, 4, 5, nome1="Juan", nome="Cleber")

