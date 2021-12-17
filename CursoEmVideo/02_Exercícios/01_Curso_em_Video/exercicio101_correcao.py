"""
(OK) - Crie um programa que tenha uma "função" chamada "voto()"
(OK) - que recebe como "parâmetro" o "ano de nascimento" de uma pessoa,
(OK) - "retornando" um valor "literal"
(OK) - Indicando se uma pessoa tem voto "NEGADO, OPCIONAL ou OBRIGATÓRIO" nas eleições.
"""
print('\033c')

def voto(ano):
    # O parâmetro FROM ou IMPORT podem ser utilizado dentro da função, com o objetivo de economizar memória na execução, como não vai precisar ser lido por todo o código, só na função.
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    # Todos os valores abaixo foram retornados para o início do programa. que começa na variável "nasc".
    if idade < 16:
        return f'Com {idade} anos: Não Vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional.'
    else:
        return f'Com {idade} anos: Voto Obrigatório.'

# Programa Principal
nasc = int(input("Em que ano você nasceu? "))
# Como após finalizado todo a saída terminará na variável nasc, é necessário o print abaixo para imprimir a saída.
print(voto(nasc))
print()