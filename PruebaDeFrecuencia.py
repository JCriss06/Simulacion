import numpy as np
def pruebaDeFrecuencia(fobservada, fesperada):
    chi_cuadrada = sum((np.array(fobservada) - np.array(fesperada))**2 / np.array(fesperada))
    print('Valor de Chi-cuadrada:',chi_cuadrada)
    if chi_cuadrada < 9.49:
        print('Los numeros siguen una distribucion uniforme: Son Aleatorios')
    else:
        print('Los numeros NO siguen una distribucion uniforme: NO son Aleatorios ')

if __name__ == "__main__":
    archivo = open('Tabla 3.1.txt','r')
    numeros = [float(numero)for linea in archivo for numero in linea.split()]

    N = len(numeros)
    n = 5
    amplitud = 1 / n
    FObservada = [0] * n
    FEsperada = [N / n] * n

    for numero in numeros:
        intervalo = int(numero //amplitud)
        FObservada[intervalo] += 1

    pruebaDeFrecuencia(FObservada, FEsperada)