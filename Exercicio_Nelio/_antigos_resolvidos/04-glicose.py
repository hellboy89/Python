glicose = float(input("Digite a medida da glicose: "))

if glicose < 100:
    print("Normal")
elif 100 <= glicose <= 140:
    print("Elevado")
elif glicose > 140:
    print("Diabetes")
else:
    print("Valor incorreto, digite novamente.")

