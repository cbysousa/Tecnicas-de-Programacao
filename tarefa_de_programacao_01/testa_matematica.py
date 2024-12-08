import matematica as mat
from matematica.estatistica import media

def teste():
    print(f'1 + 2 = {mat.soma(1, 2)}')
    print(f'2 - 1 = {mat.subtracao(2, 1)}')
    print(f'A área de um círculo de raio 2 é igual a {mat.area_circulo(2)}')
    print(f'A área de um retângulo de base 4 e 2 de altura é igual a {mat.area_retangulo(4, 2)}')
    print(f'A média dos números 3, 4, 7, 8, 9 é igual a {media.media_simples([3, 4, 7, 8, 9])}')

if __name__ == "__main__":
    teste()