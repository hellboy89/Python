"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1019
(OK) - Leia um valor inteiro, que é o tempo em segundos.
(OK) - Imprima expresso no formato de horas:minutos:segundos

n = 556

horas = n // 60
n = n % 60

print(horas, end=' ')

minutos = n // 60
n = n % 60

print(n, end=' ')

segundos = n // 60
n = n % 60

print(n)

n = 140153

horas = n // 600
minutos = n // 60
segundos = n % 60

print(horas, minutos, segundos)

# Funciona certinho, mas não atende o exercício oficial, pois se passar de 24h, ele colocar o dia em vez só do tempo em horas.
from datetime import timedelta

sec=int(input(''))

time = str(timedelta(seconds=sec))

print(time)

seg = 140153

# (OK) - Calculo das horas
horas = seg // 3600

# () - Calculo dos minutos
minutos = seg % 3600

# () - Calculo dos segundos
segundos = 2

print(horas, minutos, segundos)
"""


def calc_tempo(e):
    # Foi pego a hora e feita a divisão inteira por 3600 que é a quantidade segundos em uma hora.
    h = e // 3600
    # E o resto dessa divisão acima será utilizada no calculo dos minutos e segundos.
    r = e % 3600
    m = r // 60
    s = r % 60
    return f'{h}:{m}:{s}'


e = calc_tempo(int(input('')))

print(e)


"""
TAGS:
- conversão de tempo
- conversão de segundos para horas minutos e segundos.
"""
