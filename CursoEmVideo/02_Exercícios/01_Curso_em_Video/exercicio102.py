"""
(OK) - Crie um programa que tenha uma "função fatorial()"
(NÃO SEI) - Que receba "dois parâmetros".
(OK) - O primeiro que indique o "número" a calcular
(NÃO SEI) - e o outro chamado "show" (opcional).
(NÃO SEI) - Indicando se será mostrando ou não na tela o processo de cálculo do fatorial.
"""
print('\033c')


def fatorial(num=1):
    """
    -> Calcula o Fatorial de um numero.
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta.
    :return: O valor do Fatorial de um numero n.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


print(fatorial(4))

# help(fatorial)
print()


# PRECISO SABER COMO FAÇO PARA ACRESCENTAR O PARÂMETRO SHOW.
# ESTOU FAZENDO TESTES NO ARQUIVO TESTE4.PY.
# PRECISO ORGANIZAR SOBRE COMO FAZER O CALCULO DE FATORIAL POR PARTES COMO: 4! = 4x3x2x1 = 24