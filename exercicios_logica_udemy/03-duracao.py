duracaoSeg = int(input("Digite a duração em segundos: "))

horas = duracaoSeg // 3600
resto = duracaoSeg % 3600

minutos = resto // 60

duracaoSeg = resto % 60

print(f"{horas} : {minutos} : {duracaoSeg}")
