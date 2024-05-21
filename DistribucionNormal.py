import matplotlib.pyplot as plt
import numpy as np
def DistribucionNormal(mu, sigma, lista12):
    acumulada = []
    for lista in lista12:
        sumatoria = sum(lista)
        x = mu + sigma * (sumatoria - 6)
        acumulada.append(x)
    return acumulada

if __name__ == "__main__":
    archivo = open("LinealTabla3.1.txt", "r")
    numeros = [float(line.strip()) for line in archivo]

    lista12 = [numeros[i:i + 12] for i in range(0, 96, 12)]

    mu = 0.5
    sigma = 0.25

    resultado = DistribucionNormal(mu, sigma, lista12)

    for i in resultado:
        print(i)

    plt.hist(resultado, bins =4, density=True, alpha = 0.6, color='r')

    x = np.linspace(0, 1, 50)
    pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    plt.plot(x, pdf, color='blue', label='PDF de la distribución normal')

    plt.title('Distribucion Normal Tabla 3.1')
    plt.xlabel('Valor')
    plt.ylabel('Densidad de Probabilidad')
    plt.grid(True)
    plt.show()