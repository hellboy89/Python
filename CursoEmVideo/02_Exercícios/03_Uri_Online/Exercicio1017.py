"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1017
(OK) - Fornecer o temo em HORAS.
(OK) - E a velocidade do carro em KM/H.
    Carro faz 12 km/L. 
SAÍDA:
(OK) - A saída do programa é a quantidade de LITROS necessárias para faze a viagem.
"""
print('\033c')


def calculo(horas, km, gastom_km=12):
    calc = (km * horas) / gastom_km
    return calc


horas = int(input(''))
km = int(input(''))

calc = (calculo(horas, km))

print(f'{calc:.3f}')

"""
# horas = 10
# km = 85
# gastom_km = 12
# calc = (km * horas) / gastom_km

TAGS: 
- exemplo funções
- exemplo return
- calculo km/h e gasto litros gasolina
"""
print()
