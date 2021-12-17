primeiro = int(input('primeiro termo: '))
razao = int(input('razão: '))
decimo = primeiro + (10 - 1) * razao

cont = 0

for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('acabou')
print(cont)
