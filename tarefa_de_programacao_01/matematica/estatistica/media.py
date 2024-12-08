def media_simples(lista):
    soma_dos_numeros = 0
    for i in range(len(lista)):
        soma_dos_numeros += lista[i]
        media = soma_dos_numeros / (len(lista))
    return media