# Leia o salário de um trabalhador e o valor da prestação de um empréstimo. (FEITO)
# Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso
# contrário imprima: Empréstimo concedido.

sal = float(input('quanto é o seu salário: '))
emp = float(input('qual valor do empréstimo: '))

limite = sal * 0.20

if emp > limite:
    print('empréstimo negado!')
else:
    print('emprétimo autorizado, parabéns!')
