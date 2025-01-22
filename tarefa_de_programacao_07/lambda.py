soma = lambda x, y : x + y
print(soma(1,2))
print(soma(3,4))
print(soma(5,6))
print('---------------------------')

paridade = lambda numero : numero % 2 == 0
print(paridade(5))
print(paridade(10))
print(paridade(15))
print('---------------------------')

lista = [1, 2, 3, 4, 5, 6]
quadrado = list(map(lambda x : x ** 2, lista))
print(quadrado)
print('---------------------------')

celsius_para_fahrenheit = lambda c: (c * 9 / 5) + 32
arredondar = lambda x: round(x)
resultado = lambda c: arredondar(celsius_para_fahrenheit(c))
print(resultado(10))
print('---------------------------')

