valorX = float(input("Valor de X: "))
valorY = float(input("Valor de Y: "))

if valorX > 0 and valorY > 0:
    print("Q1")
elif valorX > 0 and valorY < 0:
    print("Q4")
elif valorX == 0 and valorY == 0:
    print("Origem")
elif valorX > 0 and valorY == 0:
    print("Eixo X")


