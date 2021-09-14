horaIni = int(input("Hora Inicial: "))
horaFin = int(input("Hora Final: "))
horaTot = 24

duracao = horaTot - (horaTot + horaIni - horaFin) % 24

if horaIni == horaFin:
    print("O jogo durou 24h.")
else:
    print(f"O jogo durou {duracao} horas.")


