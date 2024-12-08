acumulador = 0.0

def soma(operando_a=None, operando_b=None):
    global acumulador
    if operando_a is None and operando_b is None:
        return acumulador # retorna o acumulador se nenhum argumento for passado
    elif operando_b is None:
        acumulador += operando_a
    else:
        acumulador = operando_a + operando_b
    return acumulador

def sub(operando_a=None, operando_b=None):
    global acumulador
    if operando_a is None and operando_b is None:
        return acumulador
    elif operando_b is None:
        acumulador = acumulador - operando_a
    else:
        acumulador = operando_a - operando_b
    return acumulador

def div(operando_a=None, operando_b=None):
    global acumulador
    if operando_a is None and operando_b is None:
        return acumulador
    elif operando_b is None:
        acumulador = acumulador / operando_a
    else:
        acumulador = operando_a / operando_b
    return acumulador

def mut(operando_a=None, operando_b=None):
    global acumulador
    if operando_a is None and operando_b is None:
        return acumulador
    elif operando_b is None:
        acumulador = acumulador * operando_a
    else:
        acumulador = operando_a * operando_b
    return acumulador