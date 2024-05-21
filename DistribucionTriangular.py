import matplotlib.pyplot as plt
import math
def distribucionTriangular(a, b, c, R1, R2):
    if R1 < ((b - a) / (c - a)):
        return a + (b - a) * math.sqrt(R2)
    else:
        return c - (c - b) * math.sqrt(R2)

if __name__ =="__main__":
    pares = []
    file =  open('ParesTabla3.1.txt', 'r')
    for line in file:
        numeros = line.strip().split(',')
        pares.append((float(numeros[0]), float(numeros[1])))

    a = 0.0
    b = 0.5
    c = 1.0

    resultado = []
    for par in pares:
        R1, R2 = par
        resultado.append(distribucionTriangular(a, b, c, R1, R2))

    for num in resultado:
        print(num)

    plt.hist(resultado, bins=3, density= True, alpha=0.6, color='blue')
    plt.axvline(x=a, color='g', linestyle='--', label='Mínimo')
    plt.axvline(x=c, color='r', linestyle='--', label='Máximo')
    plt.axvline(x=b, color='orange', linestyle='--', label='Moda')

    plt.title('Distribucion Triangular Tabla 3.1')
    plt.xlabel('Valor')
    plt.ylabel('Densidad de Probabilidad')
    plt.legend()
    plt.grid(True)
    plt.show()