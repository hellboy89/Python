"""
(OK) - Faça um programa que tenha uma "função" chamada "ficha()",
(OK) - que receba dois "parâmetros opcionais": o "nome" de um jogador e quantos "gols" ele marcou.
(OK) - O programa deverá ser capaz de mostrar a "ficha do jogador", mesmo que algum dado não tenha sido informado corretamente.
"""
print('\033c')

# Aqui já foi definido o <desconhecido> logo no valor da variável de entrada, ou seja, se valor nenhuma for fornecido no jogador, ele será "desconhecido", sem a necessidade de utilizar um if, como na minha solução.
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa principal
n = str(input("Nome do Jogador: "))
g = str(input("Número de Gols: "))
# Abaixo foi necessário para verificar o valor de G e ter certeza que ele é um valor inteiro.
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
