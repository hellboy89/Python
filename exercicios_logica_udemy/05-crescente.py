print("Digite dois números: ")

valX = int(input())
valY = int(input())

while valX != valY:
    if valX > valY:
        print("Decrescente")
    else:
        print("Crescente")

    print("Digite outros dois números: ")
    valX = int(input())
    valY = int(input())
