"""
(DIFÍCIL E CHATO) - Crie uma "matriz" de "dimensão 3x3"
(OK) - E preencha com valores lidos pelo teclado
(NÃO CONSEGUI, TENHO QUE ENTENDER) - No final mostre a "matriz" na tela,
(O QUE RESOLVEU FOI O ^5) - Com a formatação correta.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
