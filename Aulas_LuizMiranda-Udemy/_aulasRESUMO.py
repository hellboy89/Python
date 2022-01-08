# Comando abaixo limpa o terminal antes de executar o próximo código
import os
os.system('cls' if os.name == 'nt' else 'clear')


def lista():
    import sys

    # Geradores, Iteradores e Iteráveis em Python

    lista = [0, 1, 2, 3, 4, 5]

    lista = iter(lista)

    print(next(lista))
    print(next(lista))
    print(next(lista))
    print(next(lista))
    print(next(lista))
    print(next(lista))

    print(hasattr(lista, '__next__'))

    lista2 = list(range(10))

    # esse comando abaixo mostra o consumo em memória da lista, que no caso
    # retornou 136 bits.

    print(sys.getsizeof(lista2))

    # se aumentar o tamanho da lista, aumenta a quantidade de bits.

    lista3 = list(range(1000))

    print(sys.getsizeof(lista3))


def gerador():
    import sys
    import time

    for n in range(100):
        yield n
        time.sleep(0.01)


def iniciarGerador():
    g = gerador()

    for v in g:
        print(v, end=' ')

# iniciarGerador()


def _071_geradoresIteradores():
    nome = "Juan Cleber"
    iterador = iter(nome)

    # cada next ele pega uma letra
    # se passar do limite irá gerar um erro.
    # há não ser que seja utilizado o try, para passar do erro com except.

    try:
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))
    except:
        pass

# _071_geradoresIteradores()


def _071_consumirGerador():
    nome = "Juan Cleber"
    iterador = iter(nome)
    gerador = (letra for letra in nome)

    print(next(gerador))
    print(next(gerador))
    print(next(gerador))
    print(next(gerador))

    print('olha o for')

    # aqui todo a parte do next, consome o recurso da variável,
    # sobrando somente o resto para o For abaixo.

    for letra in gerador:
        print(letra)

# _071_consumirGerador()


def _072_exercicioListComprehension():
    carrinho = []
    carrinho.append(('Produto 1', 30.50))
    carrinho.append(('Produto 2', 20))
    carrinho.append(('Produto 3', 50))

    total = sum([float(y) for x, y in carrinho])

    print(f"{total:.2f}")


# _072_exercicioListComprehension()

def _074_zip():
    cidades = ['sap paulo', 'belo horizonte', 'salvador', 'monte belo']
    estados = ['sp', 'mg', 'ba']

    # com o zip é possível unir valores de uma variável a outra.

    cidades_estados = zip(estados, cidades)
    print(list(cidades_estados))


# _074_zip()

def _074_zipLongest():
    from itertools import zip_longest

    cidades = ['sap paulo', 'belo horizonte', 'salvador', 'monte belo']
    estados = ['sp', 'mg', 'ba']

    # com o zip é possível unir valores de uma variável a outra.

    cidades_estados = zip_longest(estados, cidades)
    print(list(cidades_estados))


_074_zipLongest()

# CONTINUAR NA AULA DE ZIP_LONGEST