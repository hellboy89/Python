"""
(OK) - Dentro do pacote "utilidadesCeV" que criamos no "desafio 111", temos um "módulo" chamado "dado".
() - Crie uma função chamada "leiaDinheiro()" que seja capaz de funcionar como a função "input()",
() - mas com uma "validação de dados" para aceitar apenas valores que sejam "monetários".
"""

from utilidadesCeV import dado
import moeda

valor = "500"
convert = int(valor)

teste = dado.leiaDinheiro(valor)
teste2 = moeda.metade(convert)

print(teste)
print(teste2)

# teste = valor.isdigit()
# esse teste acima pode resolver, pois toda vez que coloco um número ele coloca true.
# UTILIZAR O PARÂMETRO IS.NUMERIC, IS.STRING, que foi dado nas primeiras aulas que não lembro com detalhes que pode resolver, e colocar dentro de uma condicional na função.
