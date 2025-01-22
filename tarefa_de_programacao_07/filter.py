numeros = [-10, 15, -20, 25, 0, 30]
positivos = filter(lambda number: number >= 0, numeros)
print(list(positivos))
print('---------------------------')

palavras = ['mercedes', 'ferrarri', 'audi', 'honda', 'renault']
caracteres = list(filter(lambda palavra : len(palavra) > 5, palavras))
print(caracteres)
print('---------------------------')

inteiros = [1, 5, -20, 6, -12, 8, 10, 60, 80]
multiplos = list(filter(lambda x: x > 0 and (x % 3 == 0 or x % 5 == 0), inteiros))
print(multiplos)
print('---------------------------')

