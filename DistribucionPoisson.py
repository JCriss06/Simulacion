import math
import random
def getPoisson(lambd):
    L = math.exp(-lambd)
    p = 1.0
    k = 0
    while p > L:
        k += 1
        p *= random.random()
    return k - 1

if __name__ == "__main__":

    valorLambda = 2.5
    valorPoisson = getPoisson(valorLambda)
    print("Valor de Poisson generado:", valorPoisson)
