peso = int(input('digite o seu peso: '))
alt = float(input('digite a sua altura: '))

imc = peso / (alt * alt)

if imc < 18.5:
    print('\ncom {:.1f} de IMC, você está abaixo do peso.'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('\ncom {:.1f} de IMC, você está com o peso ideal.'.format(imc))
elif imc > 25 and imc <= 30:
    print('\ncom {:.1f} de IMC, você está com sobrepeso.'.format(imc))
elif imc > 30 and imc <= 40:
    print('\ncom {:.1f} de IMC, você está com obesidade.'.format(imc))
elif imc > 40:
    print('\nobesidade mórbida.')
