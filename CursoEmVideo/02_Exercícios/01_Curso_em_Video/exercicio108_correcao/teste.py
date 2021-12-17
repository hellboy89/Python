import moeda

p = float(input('Digite o preço: R$ '))
# também é possível referência a função dessa forma como abaixo. Que já economiza linhas de código.
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
