from calculadora_oo import Calculadora

def teste():
    calc = Calculadora()

    print(f'5 + 5 = {calc.soma(5,5)}')
    print(f'5 - 5 = {calc.subtracao(5,8)}')
    print(f'5 x 5 = {calc.multiplicacao(5)}')
    print(f'5 / 5 = {calc.divisao(5,5)}')

if __name__ == "__main__":
    teste()