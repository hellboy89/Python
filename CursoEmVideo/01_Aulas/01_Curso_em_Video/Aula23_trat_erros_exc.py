"""
Referência: https://www.youtube.com/watch?v=xz2B3bfNjEk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=48

============================================================================

try:
    OPERAÇÃO
except TypeError:
    ERRO DE TIPO
except ValueError:
    ERRO DE VALOR
except OSError:
    ERRO DE SISTEMA DIVERSOS
else (opcional):
    DEU CERTO
finally (opcional):
    DEU CERTO / DEU FALHA

============================================================================

# O try é uma forma de tratamento de erros, pois ele irá tentar realizar o calculo dos valores abaixo.
try:
    a = int(input('digite o valor de A: '))
    b = int(input('digite o valor de B: '))
    media = (a + b) / 2
# Se caso a condição acima tiver algum erro, ela será informada na exceção abaixo.
# Também há essa forma de criar um tipo de saída de erro específico, usando o parâmetro "Exception as erro".
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
# Se caso der certo, irá para o "else", como abaixo.
else:
    print(f'A média é {media}')
# O "finally" como abaixo, irá executar a condição estando certa ou errada.
finally:
    print(f'Volte sempre')
# Fazendo dessa forma não irá mostrar uma tela de erro do código, simplesmente o que está no "except"

============================================================================

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('não é possível dividir um número por zero!')
# Em caso de parada (STOP) forçado pelo pycharm, irá mostrar a mensagem abaixo.
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
# Se quiser que mostre uma mensagem mais completa de use o parâmetro abaixo.
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print(f'\nVOLTE SEMPRE!')

"""


