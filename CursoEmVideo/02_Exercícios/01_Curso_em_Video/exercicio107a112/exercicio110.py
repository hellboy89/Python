"""
(OK) - Adicione ao módulo "moeda.py" criado nos desafios anteriores, uma função chamada "resumo()".
(OK) - Que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""

from utilidadesCeV import moeda

valor = float(input('qual valor: R$ '))
print('-=' * 15)
print('{:>22}'.format('RESUMO DE VALOR'))
print('-=' * 15)
valoran = moeda.valoranalisado(valor, sit=True)
dobro = moeda.dobro(valor, sit=True)
metade = moeda.metade(valor, sit=True)
aumento = moeda.aumento80(valor, sit=True)
reducao35 = moeda.reducao35(valor, sit=True)
print(f'Preço analisado:      {valoran}')
print(f'Dobro do preço:       {dobro}')
print(f'Metade do preço:      {metade}')
print(f'80% de aumento:       {aumento}')
print(f'35% de redução:       {reducao35}')
print('-=' * 15)
