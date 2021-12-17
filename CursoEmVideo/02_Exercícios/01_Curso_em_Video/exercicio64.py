# Crie um programa que leia "vários números" inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor "999", que é a "condição de parada".
# No Final mostre "quantos números" foram digitados e qual foi a "soma" entre eles (desconsiderando a flag)

# é o mesmo que num, cont e soma recebem 0
num = cont = soma = 0
num = int(input('digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('digite um número [999 para parar]: '))
print('=~'*30)
print('vc digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
print('=~'*30)
