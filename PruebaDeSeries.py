import numpy as np
def pruebaDeSeries(matrizFrecuencia, fEsperada):
    chi_cuadrada = np.sum((matrizFrecuencia - fEsperada) ** 2 / fEsperada)
    print('Prueba de series\nChi cuadrada:',chi_cuadrada)
    if chi_cuadrada < 36.4:
        print("Los numeros presentados pasan la prueba de uniformidad. Son Aleatorios")
    else:
        print("Los numeros presentados NO pasan la prueba de uniformidad. NO son Aleatorios")

if __name__ == "__main__":
    archivo = open('Pares.txt','r')
    pares = []
    for linea in archivo:
        par = tuple(map(float, linea.strip().split(',')))
        pares.append(par)

    N = len(pares)
    n = 5
    amplitud = 1 / n
    matrizFrecuencia = np.zeros((n, n))

    for par in pares: #contador frecuencia observada
        index_i = int(par[0] // amplitud)
        index_j = int(par[1] // amplitud)
        matrizFrecuencia[index_i, index_j] += 1

    FEsperada = np.full_like(matrizFrecuencia, N / (n ** 2))

    pruebaDeSeries(matrizFrecuencia, FEsperada)