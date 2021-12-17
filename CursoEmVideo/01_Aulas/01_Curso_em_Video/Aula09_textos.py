"""
# Aqui será mostrado como manipular um texto no python, que é uma função muito importante para as próximas aulas.
# Principalmente para tuplas, listas e dicionários.
frase = 'Curso em Vídeo Python'
# Como mostrado mais detalhadamente na saída do comando abaixo, cada caracter fica armazenado em uma posição na memória. Em um número diferente.
for i, v in enumerate(frase):
    print(i, '->', v)
print()

============================================================================

frase = 'Curso em Vídeo de Python'
# Para isso é possível fazer várias coisas para editar esse texto na saída. Como abaixo.
# FATIAMENTO: Uma forma de separar os dados, exemplos abaixo.
# Irá pegar somente a letra que está na posição 0, no caso o C.
print(frase[0])
# Lembrando que o python diferencia maiúsculas de minúsculas.
print(frase[9])
# Escrevendo de trás para frente, sempre com o -1.
print(frase[::-1])
# Pegar o caractér do 9 até o 12, sempre tira o último.
print(frase[9:13])
# Pega do 9 até o 20.
print(frase[9:21])
# Começar no 9, vai até o 20, e pula de 2 em 2.
print(frase[9:21:2])
# Começar do início até o 5. O mesmo que 0:5.
print(frase[:5])
# Começar no 15 e vai até o final.
print(frase[15:])
# Começa do 9 até o final, e pula de 3 em 3.
print(frase[9::3])

============================================================================

# ANALISE: Para analisar informações sobre a string como abaixo.
frase = 'Curso em Vídeo de Python'
# LEN utilizado para contar os caractéres.
print(len(frase))
# Também possível utilizando o COUNT, para contar quantas vezes eu tenho o 'o' na frase. Que no caso 3 vezes.
print(frase.count('o'))
# Quantas vezes tem a palavra Python na variável.
print(frase.count('Python'))
# Possível fazer um COUNT com fatiamento como abaixo, que ele só considera as letras 'o' do 0 até o 13.
# Que no caso seria somente uma, como termina no 13.
print(frase.count('o', 0, 13))
# O FIND mostra a posição onde começar o caractér 'deo', que no caso no 11.
print(frase.find('deo'))
# Quando não tem, ele informa que está -1. Significa que o valor não existe.
print(frase.find('Android'))
# Uma função interessante que informa se o 'Curso' existe em frase, se sim retornar 'True', não é 'False'.
print('Curso' in frase)
frase = 'Curso em Vídeo Python'

============================================================================

# TRANSFORMAÇÃO: lembrando que um string é imutlavel, mas possível só manipular as saídas.
# REPLACE abaixo serve para substituir tudo que tiver a palavra 'Python' para 'Android'.
print(frase.replace('Python', 'Android'))
# Colocar tudo em maiúsculo. UPPER.
print(frase.upper())
# Ao contrário do upper é o LOWER, que colocar tudo em minúsculo.
print(frase.lower())
# Só a primeira letra em maiúsculo. CAPITALIZE.
print(frase.capitalize())
# O TITLE já coloca só as primeiras palavras em maiúsculas, então ele faz uma análise palavra por palavra.
print(frase.title())
# Também possível remover os espaços excedentes no início ou no fim. Como abaixo.
frase2 = '   Aprenda Python   '
print(frase2.strip())
# Também tem uma funcionalidade mais especifica que é o RSTRIP
# Que no caso o R é de right, então ele remover os espaços só da direita.
print(frase2.rstrip())
# Mas se quiser remover só da esquerda tem o LSTRIP. 'L' de left.
print(frase2.lstrip())

============================================================================

# DIVISÃO: Agora vamos ver como dividir partes de uma string.
frase = 'Curso em Vídeo de Python'
# O SPLIT irá dividir uma frase em partes, colocando dentro de uma 'LISTA'.
print(frase.split())

============================================================================

# JUNÇÃO: Tem a função de juntar os strings.
# Como no exemplo abaixo do JOIN, irá separar por um '-' cada caractér.
print('-'.join(frase))

============================================================================

# ESCREVENDO TEXTOS em Python.
# Para escrever um texto que seja grande como abaixo, é possível colocar ele entre aspas triplas como abaixo.
# Que irá ficar posicionado na mesma posição de saída.
# Cuiado para não deixar aspas do mesmo tipo dentro da outra, pois dará erro, mude para aspas simples ou duplas.
print('''Com esse placar, Atlético segue líder e vai a 11 pontos.
Cerro somaria mais um e chegaria a 8, na vice-liderança.
Disputa pelo primeiro lugar fica aberta na última rodada,
mas com saldo de gols (8 a mais) a favor do Galo.
A tabela da Libertadores.''')

============================================================================

"""

