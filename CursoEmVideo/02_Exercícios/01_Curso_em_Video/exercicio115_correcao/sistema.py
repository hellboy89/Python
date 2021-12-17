from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
    elif resposta == 3:
        cabecalho('Sair do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! digite novamente!\033[m')
    sleep(1)
