# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

def soninho(status):
    if status == False:
        print("agora sim, estou cheio de disposição.")
        trabalhar2(True)
    else:
        print("só quero dormir e foda-se.")

def trabalhar2(gosta):
    if gosta == True:
        tarefas = []
        numeroTarefas = int(input("qual numero de tarefas? "))
        for v in range(0, numeroTarefas):
            descreva = input("descreva a tarefa? ")
            tarefas.append(descreva)
        for lista in tarefas:
            if "punheta" in lista:
                print("pare com essa desgraça seu merda!")
        print(tarefas)

def trabalhar(gosta):
    if gosta == True:
        print("excelente rapaz, então vc gosta do que faz né!")
        tarefas = input("O que irá fazer hoje? ")
        if "backup" in tarefas:
            print("vamos lá, abra a planilha e comece a conferir os backups...")
        elif "punheta" in tarefas:
            print("pare com esse vício maldito, vai te fazer queimar no inferno seu merda!")
        else:
            tarefas2 = input("o que vai fazer então vababundo: ")
            if "snapshot" in tarefas2:
                print("vai na planilha de snaps e comece a conferir agora mesmo.")
                conferencia = input("terminou de conferir? ")
                if "sim" in conferencia:
                    print("então blz, agora ache outra coisa para fazer...")
    else:
        print("precisa orar mais.")


soninho(False)