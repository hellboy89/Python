"""
(OK) - Crie um programa que tenha uma "função fatorial()"
(OK) - Que receba "dois parâmetros".
(OK) - O primeiro que indique o "número" a calcular
(OK) - e o outro chamado "show" (opcional).
(OK) - Indicando se será mostrando ou não na tela o processo de cálculo do fatorial.
"""
print('\033c')

# Aqui foi acrescentado o valor False no Show, porque é o valor padrão, mesmo que não adicione uma variável lá no programa principal, ele irá subir como "False".
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        # Aqui é onde se inicia a minha condição "show", pois toda vez que o show for True, ele virá para o condicional abaixo.
        if show:
            print(c, end='')
            # Essa condição abaixo serve para ele não colocar um X extra na formatação de saída.
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
print(fatorial(5, show=False))
# help(fatorial)
print()
