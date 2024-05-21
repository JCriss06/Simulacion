import numpy as np
import matplotlib.pyplot as plt

def DistribucionExponencial(plambda, numeros):
    distribucion = []
    for i in numeros:
        x = -(1 / plambda) * np.log(i)
        distribucion.append(x)
    return distribucion

if __name__ == "__main__":
    archivo = open("Tabla 3.1.txt", "r")
    numeros = [float(valor) for linea in archivo for valor in linea.strip().split()]

    plambda = 1

    muestra = DistribucionExponencial(plambda, numeros)
    #print(max(muestra))

    plt.hist(muestra, bins=5, density=True, alpha=0.6, color='b')

    x = np.linspace(0, max(muestra), 100)
    plt.plot(x, plambda * np.exp(-plambda * x), 'r-', lw=2)

    plt.title('Transformada Inversa de la Distribución Exponencial Tabla 3.1')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()