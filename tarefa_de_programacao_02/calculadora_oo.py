class Calculadora:
    def __init__(self):
        self.__acumulador = 0.0

    def soma(self, operando_a, operando_b=None):
        if operando_a is None and operando_b is None:
            return self.__acumulador # Retorna o acumulador se nenhum operando for fornecido
        elif operando_a is None:
            self.__acumulador += operando_b
        elif operando_b is None:
            self.__acumulador += operando_a
        else:
            self.__acumulador = operando_a + operando_b
        return self.__acumulador
    
    def subtracao(self, operando_a, operando_b=None):
        if operando_a is None and operando_b is None:
            return self.__acumulador # Retorna o acumulador se nenhum operando for fornecido
        elif operando_a is None:
            self.__acumulador -= operando_b
        elif operando_b is None:
            self.__acumulador -= operando_a
        else:
            self.__acumulador = operando_a - operando_b
        return self.__acumulador
    
    def multiplicacao(self, operando_a, operando_b=None):
        if operando_a is None and operando_b is None:
            return self.__acumulador # Retorna o acumulador se nenhum operando for fornecido
        elif operando_a is None:
            self.__acumulador *= operando_b
        elif operando_b is None:
            self.__acumulador *= operando_a
        else:
            self.__acumulador = operando_a * operando_b
        return self.__acumulador
    
    def divisao(self, operando_a, operando_b=None):
        if operando_a is None and operando_b is None:
            return self.__acumulador
        elif operando_a is None:
            self.__acumulador /= operando_b
        elif operando_b is None:
            self.__acumulador /= operando_a
        else:
            self.__acumulador = operando_a / operando_b
        return self.__acumulador
