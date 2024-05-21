import numpy as np
import matplotlib.pyplot as plt

def DistribucionUniforme (a, b, numeros):
    distribucion = []
    for i in numeros:
        x = a + (b - a) * i
        distribucion.append(x)
    return distribucion

if __name__ == "__main__":
    archivo = open("Tabla 3.1.txt", "r")
    numeros =[ float(valor) for linea in archivo for valor in linea.strip().split()]
    a = 5
    b = 10
    muestra = DistribucionUniforme(a, b, numeros)
    print(muestra)

    plt.hist(muestra, bins=5, density=True, alpha=0.6, color='g')

    x = np.linspace(a, b, 100)
    plt.plot(x, np.full_like(x, 1 / (b - a)), 'r-', lw=2)

    plt.title('Transformada Inversa de la Distribucion Uniforme Tabla 3.1')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()