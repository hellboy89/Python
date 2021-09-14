print("Digite as três distâncias: ")
dist1 = float(input())
dist2 = float(input())
dist3 = float(input())

maior = dist1

if maior < dist2:
    maior = dist2
elif maior < dist3:
    maior = dist3

print(f"Maior distância = {maior:.2f}")

