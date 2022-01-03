# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

d1 = {
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4) : 'Tupla'
}

# adicionar nova chave no dicionário.
# pode ser feito dessa forma abaixo.

d1.update({
    'nova_chave': 'novo_valor'
})

# se quiser apagar uma chave do dicionário.

del d1[123]

print(d1)

# verificando valores e chaves.

print('str' in d1)
print('str' in d1.keys())
print('valor' in d1.values())
print(len(d1))

# acessando chaves e valores separadamente.

print("acessando valores:")
for v in d1.values():
    print(v, end = ' ')

print("\nacessando chaves:")
for c in d1.keys():
    print(c, end = ' ')

print("\nverificando chave e valores: ")
# acessando valores separadamente com esse print abaixo.
for k, v in d1.items():
    print(k, v)

print()
# testando com um dicionário com mais informações.

clientes = {
    'client1' : {
        'nome' : 'Juan',
        'sobrenome' : 'Cleber'
    },
    'cliente2' : {
        'nome' : 'Denise',
        'sobrenome' : 'Da Rocha'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'exibindo: {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

# testando cópia de valores no dicionário.

d1 = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: ['Juan', 'Cleber']
}

c1 = d1

# usando comando baixo para ver o id da variável na memória.
# para saber se são iguais ou diferentes.

# mas para criar uma cópia do dicionário que seja completamente diferente
# é ncessário utilizar o parâmetro abaixo.

c2 = d1.copy()

print(hex(id(d1)))
print(hex(id(c2)))
print(d1 == c2)

print(d1)
print(c2)

