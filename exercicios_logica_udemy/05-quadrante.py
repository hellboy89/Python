print("Digite os valores das coordenadas X e Y: ")

valX = int(input())
valY = int(input())

while valX != 0 or valY != 0:
    if valX > 0 and valY > 0:
        print("Quadrante Q1")
    elif valX > 0 and valY < 0:
        print("Quadrante Q4")
    elif valX < 0 and valY < 0:
        print("Quadrante Q3")
    elif valX < 0 and valY > 0:
        print("Quadrante Q2")
    elif valX == 0 or valY == 0:
        break

    valX = int(input())
    valY = int(input())


