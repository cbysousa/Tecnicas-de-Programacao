lista = ['python', 'lambda', 'map']
maiusculas = (list(map(lambda x : x.upper(), lista)))
print(maiusculas)
print('---------------------------')

from math import sqrt
lista = [1, 81, 100, 4, 5, 6]
raiz = list(map(lambda x : sqrt(x), lista))
print(raiz)
print('---------------------------')

lista =  ["Python é incrível", "Lambda são úteis", "Map é funcional"]
dicionarios = list(map(lambda frase: {"palavras": len(frase.split()), "caracteres": len(frase)}, lista))
print(dicionarios)
print('---------------------------')