"""

# O While é diferente do FOR.
# Sintaxe
# While expressao_booleana:
#    //execução do loop
# Tudo que está dentro do While será repetido, enquanto a expressão booleana for verdadeira.
# Expressão booleana é o True or False.
# Sempre é retornada para confirmar se uma expressão é verdadeira ou falsa.
# Como nos exemplo abaixo.
teste1 = 5 > 7
print(teste1)
# Irá retornar falso, pois 5 não é maior do que 7.
teste2 = 5 == 5
print(teste2)
# Irá retornar verdadeiro, pois 5 é igual a 5.

============================================================================

# Exemplo 1
numero = 1
# Aqui o limite é o contador acima, pois somente irá parar o While quando o valor de número for menor do que 10.
while numero < 10:
    print(numero, end=' ')
    numero += 1

# OBS.: Em um LOOP While é importante que cuidemos de um critério de parada. SEMPRE!!!
# Se caso não tiver uma condição de parada, o LOOP será infinito, e para parar será necessário usar o STOP do IDE.

============================================================================

# Exemplo 2
resposta = ''
# Aqui ele irá fazer a parada, somente quando a resposta for 'Sim", pois irá se tornar verdadeira a condição do While.
while resposta != 'SIM':
    resposta = input('já acabou jéssica? ').upper()
# Necessário pensar bem na forma de parada do código.

============================================================================

# O LOOP While também existe no C ou Java, mas para declarar é um pouco diferente como abaixo
while (expressao){
    //expressao
}
# do while (C ou Java)

do {

} while(expressao);

============================================================================

# Há uma forma com maiores opções de sair de um LOOP While, que é o BREAK, que será demonstrado com mais detalhes nos exemplo abaixo.
# BREAK também é largamente utilizado em outras linguagens com C ou Java.
# Lembrando que o BREAK é uma condição usada para parar qualquer LOOP, tanto FOR quanto WHILE. Como mostrado nos exemplo mais abaixo.

# Exemplo 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero, end=' ')
print(f'\n\nSAI DO LOOP WHILE')

# Exemplo 2
while True:
    comando = input('digite sair para sair? ')
    if comando == 'sair':
        break

============================================================================

"""

