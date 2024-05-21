import random

def juegoVolado(inicial, apuesta, objetivo):
    while inicial > 0 and inicial < objetivo:
        x = random.uniform(0,1)
        if (x < 0.5):
            #gano
            inicial = inicial + apuesta
            apuesta = 10
        else:
            #perdio
            inicial = inicial - apuesta
            apuesta = 2 * apuesta
            if (apuesta > inicial):
                apuesta = inicial # apuesta lo disponible
    return inicial

if __name__ == '__main__':

    inicial = 30
    apuesta = 10
    objetivo = 50
    gano = 0
    n = 1000000

    for i in range(n):
        salida = juegoVolado(inicial, apuesta, objetivo)
        if (salida >= objetivo):
            gano = gano + 1
    probabilidad = gano / n
    print('Objetivo: $', objetivo)
    print('La probabilidad de llegar al objetivo es:',probabilidad)