acumulador = 0.0

def soma(operando_a, operando_b=None):
    global acumulador
    if operando_b is None:
        acumulador = acumulador + operando_a
    else:
        acumulador = operando_a + operando_b
    return acumulador

def sub(operando_a, operando_b=None):
    global acumulador
    if operando_b is None:
        acumulador = acumulador - operando_a
    else:
        acumulador = operando_a - operando_b
    return acumulador

def div(operando_a, operando_b=None):
    global acumulador
    if operando_b is None:
        acumulador = acumulador / operando_a
    else:
        acumulador = operando_a / operando_b
    return acumulador

def mut(operando_a, operando_b=None):
    global acumulador
    if operando_b is None:
        acumulador = acumulador * operando_a
    else:
        acumulador = operando_a * operando_b
    return acumulador