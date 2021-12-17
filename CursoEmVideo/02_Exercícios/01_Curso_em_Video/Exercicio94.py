"""
(OK) - Crie um programa que leia 'nome, sexo e idade' de 'várias pessoas',
(OK) - guarde os dados de cada pessoa em um 'dicionário', e todos os dicionários em uma 'lista'.
(OK) - No final, mostre: A) Quantas pessoas foram cadastradas.
(OK) - B) A 'média' de idade do grupo.
(OK) - C) Uma lista com todas as 'mulheres'.
(OK) - D) Uma lista com todas as pessoas com 'idade' acima da 'média'.
"""

dados = dict()
lista = list()
dados['soma_idades'] = 0
while True:
    lista.append(str(input('qual seu nome: ')).title())
    lista.append(str(input('qual seu sexo [M/F]: ')).upper().strip()[0])
    lista.append(int(input('qual sua idade: ')))
    perg = str(input('quer continuar [S/N]: ')).strip()[0]
    if perg in 'nN':
        break
# Com essa filtragem abaixo consigo selecionar melhor os índices para pegar os dados na posição que preciso da lista.
dados['nome'] = lista[0::3]
dados['sexo'] = lista[1::3]
dados['idade'] = lista[2::3]
# Soma das idades para calculo da média
for i, v in enumerate(dados['idade']):
    dados['soma_idades'] += v
# Abaixo é o solicitado no exercício
print(dados)
print('=-' * 30)
print('O grupo tem um total de {} pessoas.'.format(len(dados['nome'])))
print('A média de idade do grupo é {:.0f}'.format(dados['soma_idades'] / len(dados['nome'])))
# Imprimir o nome dos homens e das mulheres.
# Crie 2 LISTAS separadas para marcar a posição das mulheres.
posicao_m = list()
posicao_f = list()
# Após isso fiz uma condição para adicionar na lista todas que tem a variável 'M' no 'Sexo'.
for i, v in enumerate(dados["sexo"]):
    if v == 'M':
        posicao_m.append(i)
    if v == 'F':
        posicao_f.append(i)
# Aqui inseri os dados no dicionário na chave com nome 'dados['posicao_m'] e dados['posicao_f']'.
dados['posicao_m'] = posicao_m[:]
dados['posicao_f'] = posicao_f[:]
print(f'As mulheres cadastradas foram: ', end='')
# Aqui fiz a separação para ele imprimir somente as mulheres que estão na posição informada do dicionário.
for i, v in enumerate(dados['posicao_f']):
    print(f'{dados["nome"][v]}', end=' ')
print()
# Separando os valores da idade
# A variável abaixo serve para criar uma CHAVE no dicionário para pegar a média de idade, para ser usado posteriormente.
dados['media_idade'] = int(dados['soma_idades']) / len(dados['nome'])
idade_acima_media_pos = list()
# Aqui fiz a separação para adicionar os valores na lista acima e marcar a posição, exatamente como fiz na parte anterior.
for i, v in enumerate(dados['idade']):
    if v >= dados['media_idade']:
        idade_acima_media_pos.append(i)
dados['idade_acima_media_pos'] = idade_acima_media_pos[:]
# Aqui já fiz a parte final com a impressão dos dados informados.
print(f'As pessoas com idade acima da média são: ', end=' ')
for i, v in enumerate(dados['idade_acima_media_pos']):
    print(dados['nome'][v], end=' ')
