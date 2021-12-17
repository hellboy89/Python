nota1 = float(input('informe a primeira nota: '))
nota2 = float(input('informe a segunda nota: '))

media = (nota1 + nota2) / 2

if media <= 10:
    print('a média do aluno é: {}'.format(media))
elif media >= 10.01:
    print('por favor, insira um valor válido, o máximo é 10!')
