"""
n1 = int(input('digite um valor: '))
n1 = 1 + 100

print(n1)


"""

try:
    while True:
        nome = input('qual o nome: ')
        idade = input('qual idade: ')
        with open('teste7.txt', 'a') as file:
            file.write(f'Nome: {nome}')
            file.write('\n')
            file.write(f'Idade: {idade}')
            file.write('\n')
            file.close()
        perg = input('que parar? [S/N] ')
        if perg in 'Nn':
            break
except Exception as erro:
    print(f'deu ruim no {erro}')
else:
    with open('teste7.txt', 'r') as ler:
        var = ler.read()
        print(var)
        ler.close()
finally:
    print(f'\n\nAdeus mané!')