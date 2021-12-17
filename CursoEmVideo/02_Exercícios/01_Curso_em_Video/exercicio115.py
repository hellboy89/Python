"""
() - Crie um pequeno "sistema modularizado"
() - Que permita cadastrar pessoas pelo seu "nome" e "idade" em um arquivo de texto simples.
() - O sistema só vai ter "2 opções": "Cadastrar uma nova pessoa" e "listar" todas as cadastradas.
"""

def dadosTXT(nome, idade):
    try:
        while True:
            with open('exercicio115.txt', 'a') as file:
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


nome = input('qual seu NOME: ')
idade = input('qual sua IDADE: ')
dados_func = dadosTXT(nome, idade)
print(dados_func)

with open('exercicio115.txt', 'r') as ler:
    var = ler.read()
    print(var)
    ler.close()