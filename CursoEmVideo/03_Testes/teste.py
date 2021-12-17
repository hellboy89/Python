"""
dados = dict()
lista = list()
dados['soma_idade'] = 0

lista.append('Denise')
lista.append('F')
lista.append(62)
lista.append('Cleber')
lista.append('M')
lista.append(67)
lista.append('Tatiana')
lista.append('F')
lista.append(47)
lista.append('João')
lista.append('M')
lista.append(12)

# Abaixo eu consigo pular os índices para pegar só os dados do qual eu preciso.
dados['nome'] = lista[0::3]
dados['sexo'] = lista[1::3]
dados['idade'] = lista[2::3]

print(f'LISTA é {lista}')
# print(f'Só os nomes da lista é {lista[0::3]}')
print('=-' * 50)
print(f'DICIONÁRIO é {dados}')

# Soma dos valores de idade.

for i, v in enumerate(dados['idade']):
    print(i, v)
    dados['soma_idade'] += v
print(f'a soma das idades é {dados["soma_idade"]}')
print('=-' * 30)
# if dados['sexo'] == 'M':
#     print(f'O nome dos homens é {dados["nome"]}')

posicao_m = list()
posicao_f = list()

for i, v in enumerate(dados['sexo']):
    if v == 'M':
        print(i, '->', v)
        posicao_m.append(i)
        print(f'O nome dos homens é {dados["nome"]}')
    if v == 'F':
        posicao_f.append(i)
dados['posicao_m'] = posicao_m[:]
dados['posicao_f'] = posicao_f[:]
print('=-' * 40)
print(dados)
print('=-' * 40)
print()
for i, v in enumerate(dados['posicao_m']):
    print(dados["nome"][v], end=' ')
print()
for i, v in enumerate(dados['posicao_f']):
    print(dados["nome"][v], end=' ')

# PEGANDO AS PESSOAS COM IDADE ACIMA DA MÉDIA TOTAL.
print('a média das idades é: {:.0f}'.format((dados['soma_idade']) / len(dados['nome'])))

dados['media_idades'] = int(dados['soma_idade'] / len(dados['nome']))
idade_acima_media = list()
for i, v in enumerate(dados['idade']):
    if v >= dados['media_idades']:
        idade_acima_media.append(i)
dados['idade_acima_media'] = idade_acima_media[:]

print()
print(dados)
print()

for i, v in enumerate(dados['idade_acima_media']):
    print(dados['nome'][v], end=' ')
print()
# AINDA NÃO, O PROBLEMA É QUE A VARIÁVEL "dados['idade_acima_media']" PEGA MAIS DE UM VALOR, POR ISSO NÃO DÁ PARA USAR ELA NO FOR ACIMA.
# ACHEI A SOLUÇÃO, SÓ USAR O VALOR DA LISTA EM SEPARADO COM O ENUMERATE.
# SURGIU UM OUTRO PROBLEMA, NÃO POSSO FAZER CONDICIONAMENTOS ENTRE INTEIROS E LISTAS, NECESSÁRIO PERCEBER QUANDO OCORRER. POIS NEM O PYTHON AVISA.
# AGORA TENHO QUE PEGAR O CALCULO DA 'MÉDIA DE IDADE', E TODAS AS PESSOAS QUE TIVEREM 'IDADE' ACIMA, 'MOSTRAR'.
# AGORA JÁ CONSEGUI DEFINIR A POSIÇÃO DE TODOS QUE SÃO 'M', TENHO QUE DESCOBRIR UMA FORMA DE VINCULAR AO 'NOME'.
# POSSO CRIAR UMA LISTA PARA RESOLVER, MAS AINDA NÃO CONSIGO PENSAR NA MANEIRA. QUE IRÁ ADICIONAR 2 VALORES DIFERENTES.
# CHEGUEI QUASE LÁ COM A SOLUÇÃO ACIMA, MAS SÓ ESTÁ PEGANDO OS DADOS DO NOME DO ÚLTIMO 'M'.
# SEQUIR A LÓGICA, O VALOR 'M' E 'F' MARCAR UMA POSIÇÃO, NECESSÁRIO PEGAR ESSA MESMA POSIÇÃO NA CHAVE DO 'NOME'.
# TENHO QUE PEGAR SÓ O NOME DOS HOMENS, MAS FILTRANDO PELO SEXO.
# DICIONÁRIO é {'soma_idade': 0, 'nome': ['Denise', 'Cleber'], 'sexo': ['F', 'M'], 'idade': [62, 67]}

dados = {'nome': ['Kaka', 'Romario', 'Vampeta'], 'n_partidas': [4, 2, 2], 'n_gols': [2, 3, 5, 1, 3, 5, 1, 5], 'codigo': [0, 1, 2]}

for i, v in enumerate(dados['nome']):
    print(v, dados['n_partidas'][i])

print('O jogador {} fez {} gols.'.format(dados['nome'][0], dados['n_gols']))

# (OK) - VAMOS POR PARTES, PRIMEIRO VAMOS SELECIONAR O 'NOME'
# (OK) - DEPOIS O 'N_PARTIDAS' DE CADA JOGADOR
# () -  EM POR ÚLTIMO O NÚMERO DE GOLS.
============================================================================


"""


dados = {'nome': 'juan', 'media': 8.0, 'situacao': 'APROVADO'}

print(dados.keys())
print(dados.values())
print(dados.items())

# dict_keys(['nome', 'media', 'situacao'])
# dict_values(['juan', 8.0, 'APROVADO'])
# dict_items([('nome', 'juan'), ('media', 8.0), ('situacao', 'APROVADO')])