"""
# Declarar um dicionário usando o dict().
dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
# inserir valor no dicionário
dados['sexo'] = 'M'
# remover valor
del dados['idade']
print(dados)
print(dados['nome'])
# print(dados['idade'])
print(dados['sexo'])

============================================================================

# Criando separação que seja visualmente melhor.
filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}
# Imprimir os valores das chaves
print(filme.values())
# Imprimir o nome das chaves
print(filme.keys())
# Imprimir as chaves e os valores
print(filme.items())
# Utilizando o for para mostrar na tela
for k, v in filme.items():
    print(f'O {k} é {v}')

============================================================================

pessoas = {'nome': 'Juan',
           'sexo': 'M',
           'idade': 31}
print(pessoas)
# Imprimindo separadamente.
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
# Utilizando for para mostrar de maneira mais organizada.
for k, v in pessoas.items():
    print(k, v)
# Imprimindo de forma mais formatada, filtrando dados. Não esquecer de aspas duplas entre [""].
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# Imprimindo só as chaves.
print(pessoas.keys())
# Imprimindo só os valores.
print(pessoas.values())
# Imprimindo os itens que tem chaves e valores.
print(pessoas.items())
# Removando o sexo. Lembrando que dicionários são mutáveis, ao contrário de tuplas.
del pessoas['sexo']
# Alterando uma valor do dicinários.
pessoas['nome'] = 'Cleber'
pessoas['idade'] = 67
# Adicionando novos elementos no dicionário.
pessoas['peso'] = 120
pessoas['cor'] = 'pardo'
# Imprimindo com for. Utilizando a primeira coluna nome = k, a segunda dados = v.
for k, v in pessoas.items():
    print(f'{k} = {v}')

============================================================================

# Colocando DICIONÁRIOS dentro de LISTAS.
# Criando uma LISTA vazia abaixo.
brasil = []
estado1 = {'uf': 'Rio de Janeiro',
           'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo',
           'sigla': 'SP'}
# Adicionando as variáveis acima na lista Brasil.
brasil.append(estado1)
brasil.append(estado2)
# Imprimindo tudo.
print(brasil)
# Filtrando por dicinoários
print(brasil[0])
print(brasil[1])
# Filtrando por UF, que está na posição 0.
print(brasil[0]['uf'])
# Filtrando por UF, que está na posição 1.
print(brasil[1]['uf'])
# Filtrando a sigla da posição 1 e 0.
print(brasil[1]['sigla'])
print(brasil[0]['sigla'])

============================================================================

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('unidade federativa: '))
    estado['sigla'] = str(input('sigla do estado: '))
    # O parâmetro abaixo copy irá criar uma cópia do DICIONÁRIO toda vez que o parâmetro FOR executar.
    # Ele serve em substituição do parâmtro [:] que é utilizado na lista.
    brasil.append(estado.copy())
print(brasil)
# Filtrando utilizando o for por linha.
for e in brasil:
    print(e)
print()
# Filtro mais detalhado na saída.
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
print()
# Filtrando só pelos valores finais.
for e in brasil:
    for v in e.values():
        print(v, end=' ')
print()

============================================================================

# Para adicionar 'vários valores' dentro do mesmo dicionário.
teste = dict()
# Fazer dessa forma, separar por vírgula.
teste['dado1'] = 23, 4
teste['dado2'] = 55, 29
teste['dado3'] = 22, 13
print(teste)
# Na hora de imprimir selecionar o dicionário e o valor separado por [].
print(teste['dado1'][0])

============================================================================

# ADICIONANDO LISTAS DENTRO DE UM DICIONÁRIO, USANDO 'FOR'
# Abaixo irá definir os dados como dicionários.
jogador = dict()
# Abaixo irá definir a lista.
partidas = list()
# Abaixo irá definir a CHAVE no dicionário com o valor nome, com VALOR nome do jogador.
jogador['nome'] = str(input('nome do jogador: '))
# Irá definir o número de partidas que será colocado no limite do contador FOR.
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# O limite do FOR será definido acima.
for c in range(0, tot):
    # Abaixo utilizando o método APPEND, cada vez que inserido o valor será acrescentado na variável PARTIDAS(lista).
    partidas.append(int(input(f'     Quantos gols na partida {c} ')))
# PULO DO GATO!.. Será feita uma cópia de todos os valore que estão na partida, para uma nova CHAVE chamada 'gols'.
jogador['gols'] = partidas[:]
# Imprimir o total.
print(jogador)
# SAÍDA
# {'nome': 'juan', 'gols': [2, 3, 5]}

"""

