"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1014

"""
print('\033c')

def distancia(dist, comb):
    calc = dist / comb
    return calc

dist = int(input(''))
comb = float(input(''))

calc = (distancia(dist, comb))

print(f'{calc:.3f} km/l')

print()

"""
TAGS:
- exemplo de funções
- entendimento do return
"""