# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

cpf = "168.995.350-09"

lista = cpf.split('.', 3)

cpfRetiraPonto = cpf.replace(".","").replace("-","")

if len(cpfRetiraPonto) == 11:
    print("CPF correto")
else:
    print("CPF invalido")

print(lista)
