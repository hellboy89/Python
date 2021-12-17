# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal=float(input('informe o salário do funcionário: '))
aumento=sal*15/100

print('o salário com 15% de aumento ficaria R$ {:.2f}'.format(sal+aumento))