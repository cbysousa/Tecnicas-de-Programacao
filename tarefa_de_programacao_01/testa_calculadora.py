import calculadora as calc

def teste():
    print(f"1 + 8 = {calc.soma(1,8)}")
    print(f"? + 2 = {calc.sub(2)}")
    print(f"4 + 2 = {calc.soma(1,2)}")
    print(f"2 + 8 = {calc.mut(2,8)}")

if __name__ == "__main__":
    teste()