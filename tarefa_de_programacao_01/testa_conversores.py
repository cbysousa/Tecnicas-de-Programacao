import conversores as conv

def teste():
    print(f'\n20 graus celsius são iguais a {conv.celsius_para_fahrenheit(20):.0f} graus fahrenheit.\n')
    print(f'68 graus fahrenhei são iguais a {conv.fahrenheit_para_celsius(68):.0f} graus celsius.\n')
    print(f'50 metros são iguais a {conv.metro_para_pes(50)} pés.\n')
    print(f'164.05 pés são iguais a {conv.pes_para_metros(164.05)} metros.\n')
    print(f'10 quilômetros são iguais a {conv.quilometros_para_milhas(10)} milhas.\n')
    print(f'6.215040397762586 milhas são iguais a {conv.milhas_para_quilometros(6.215040397762586)} quilometros.\n')
    print(f'2 dias são iguais a {conv.dias_para_horas(2)} horas.\n')


if __name__ == "__main__":
    teste()