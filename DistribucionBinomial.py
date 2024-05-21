import random
def getBinomial(n, p):
    x = 0
    for i in range(n):
        if random.random() < p:
            x += 1
    return x

if __name__ == "__main__":

    n = 10  # Número de ensayos
    p = 0.5  # Probabilidad de éxito en un solo ensayo
    valorBinomial = getBinomial(n, p)
    print("Valor Binomial generado:", valorBinomial)
