"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

ano = 365 dias
mês = 30 dias

"""


def calc_tempo(dias):
    # (OK) - e informe em anos,
    anos = dias // 365
    anos_rest = dias % 365
    # (OK) - meses
    mes = anos_rest // 30
    dias = anos_rest % 30
    return anos, mes, dias


# (OK) - Leia o valor inteiro correspodente a idade de uma pessoa em dias
dias = calc_tempo(int(input('')))

print(f'{dias[0]} ano(s)')
print(f'{dias[1]} mes(es)')
print(f'{dias[2]} dia(s)')

"""
TAGS:
- Calculo anos, meses e dias
- Teste funções, uso de defs
"""
