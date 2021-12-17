# faça um programa que mostre a "tabuada" de "vários números", um de cada vez, para cada valor digitado
# pelo usuário. O programa será "interrompido" quando o número solicitado for "negativo".

while True:
    n = int(input('digite um número: '))
    if n <= 0:
        break
    for c in range(0, 11):
        tab = n * c
        # print(tab)
        print('{} x {} é {}'.format(n, c, tab))
