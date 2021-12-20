quantRep = int(input("Quantos casos você vai digitar? "))

for i in range(0, quantRep):
    print("Digite três números: ")
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())

    media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

    print(f"Media = {media:.1f}")


