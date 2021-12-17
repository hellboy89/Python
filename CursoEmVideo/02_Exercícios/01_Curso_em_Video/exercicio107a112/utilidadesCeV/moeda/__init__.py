def valoranalisado(valor, sit=False):
    if sit:
        convert = str(valor).replace('.', ',0')
        return convert
    else:
        return valor


def metade(valor, sit=False):
    calc = valor / 2
    if sit:
        convert = str(calc).replace('.', ',0')
        return convert
    else:
        return calc


def dobro(valor, sit=False):
    calc = valor * 2
    if sit:
        convert = str(calc).replace('.', ',0')
        return convert
    else:
        return calc


def aumento10(valor, sit=False):
    calc = valor * 0.10
    valordesconto = valor + calc
    if sit:
        convert = str(valordesconto).replace('.', ',0')
        return convert
    else:
        return valordesconto


def reduzindo13(valor, sit=False):
    calc = valor * 0.13
    valordesconto = valor - calc
    if sit:
        convert = str(valordesconto).replace('.', ',0')
        return convert
    else:
        return valordesconto


def formato(valor, sit=False):
    if sit:
        convert = str(valor).replace('.', ',0')
        return convert
    else:
        return valor


def aumento80(valor, sit=False):
    calc = valor * 0.80
    valoraumento = valor + calc
    if sit:
        convert = str(valoraumento).replace('.', ',0')
        return convert
    else:
        return valoraumento


def reducao35(valor, sit=False):
    calc = valor * 0.35
    desconto = valor - calc
    if sit:
        convert = str(desconto).replace('.', ',0')
        return convert
    else:
        return desconto
