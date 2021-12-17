"""
(OK) - Faça um "mini-sistema" que utilize o "interactive help" do python.
(OK) - O usuário vai digitar o "comando" e o "manual" vai aparecer. 
(BUG NA FUNÇÃO DO WHILE) - Quando o usuário digitar a palavra "FIM", o programa se "encerrará".
(OK) - Use "cores".
"""
print('\033c')

def ajuda(valor=None, msg=None):
    from time import sleep
    tam1 = len(msg) - 10
    print('~' * tam1)
    print(f'{msg}')
    sleep(0.5)
    while True:
        if valor:
            retorno = help(valor)    
        elif valor == 'fim':
            break
        print('~' * tam1)


# Programa principal

print('\033[1;42mSISTEMA DE AJUDA PYTHON\033[m')
ajuda(valor=(str(input('\033[7mfunção ou biblioteca [FIM]: \033[m'))),
      msg='ACESSANDO O MANUAL DO COMANDO')


# ajuda(msg1='\033[1;42mSISTEMA DE AJUDA PyHELP\033[m', msg2='\033[1;46mACESSANDO O MANUAL DO COMANDO\033[m')


print()

# PRECISO COLOCAR UMA MENSAGEM COM CORES PERSONALIZADAS E TAMANHO DOS TRAÇOS ACIMA E ABAIXO TAMBÉM.
