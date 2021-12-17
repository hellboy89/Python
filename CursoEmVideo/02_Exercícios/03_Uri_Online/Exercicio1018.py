"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1018
(OK) - Leia um valor inteiro.
(OK) - A seguir calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
(OK) - As notas consideras são de 100, 50, 20, 10, 5, 2 e 1.
(OK) - A seguir mostre o 'VALOR LIDO' e a relação de notas necessárias.
"""


def calc_cedula(n):
    n100 = n // 100
    r = n % 100
    n50 = r // 50
    r = r % 50
    n20 = r // 20
    r = r % 20
    n10 = r // 10
    r = r % 10
    n5 = r // 5
    r = r % 5
    n2 = r // 2
    r = r % 2
    n1 = r // 1
    r = r % 1
    print(n)
    print(n100, "nota(s) de R$ 100,00")
    print(n50, "nota(s) de R$ 50,00")
    print(n20, "nota(s) de R$ 20,00")
    print(n10, "nota(s) de R$ 10,00")
    print(n5, "nota(s) de R$ 5,00")
    print(n2, "nota(s) de R$ 2,00")
    print(n1, "nota(s) de R$ 1,00")


n = int(input(''))
calc = (calc_cedula(n))


"""
TAGS:
- calculo simples 
- exemplo funções 
"""
