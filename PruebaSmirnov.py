if __name__ == "__main__":
    archivo = open("Tabla 3.1.txt", "r")
    numeros = [float(valor) for linea in archivo for valor in linea.strip().split("\t")]
    numeros.sort()

    n = 100
    dacumulada = [i/n for i in range(1, n+1)]
    estadistico = max([abs(x - y) for x, y in zip(numeros, dacumulada)])

    print("Estadistico de Kolmogorov-Smirnov:",estadistico)

    dan = 0.134
    if estadistico < dan:
        print("Los numeros presentados provienen de una distribucion uniforme: Son Aleatorios")
    else:
        print("Los numeros presentados NO provienen de una distribucion uniforme: NO son Aleatorios")