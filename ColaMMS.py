import math
import random
import numpy as np
import Person
import Slot

def distribucion_exponencial(lbma):
    div = 1 / (-1 / lbma) * (np.log(random.random()))
    return int(round(60 * div, 0))

def poisson(mi):
    l = math.exp(-mi)
    p = 1
    k = 0
    k += 1
    p *= random.random()
    while p > l:
        k += 1
        p *= random.random()
    return k - 1

if __name__ == '__main__':
    temporizador = 0
    caja = 1
    cajaList = []
    cola = []
    promedioPoisson = 50
    exponencialLambda = 0.25
    gentePorHora = []
    horasSimuladas = 100
    mejorActual = 2147483645

    while mejorActual > 10:
        for i in range(caja):
            cajaList.append(Slot.Slot())
        for i in range(horasSimuladas * 60):
            if temporizador == 0:
                for n in range(poisson(promedioPoisson)):
                    cola.append(Person.Person(distribucion_exponencial(exponencialLambda)))
            for slot in cajaList:
                if slot.person is None and len(cola) > 0:
                    slot.person = cola.pop(0)
                elif slot.person is not None:
                    slot.person.tiempoAvance()
                    if slot.person.time <= 0:
                        slot.person = None
                        if len(cola) > 0:
                            slot.person = cola.pop(0)
            if temporizador == 59:
                peopleInQueue = len(cola)
                for slot in cajaList:
                    if slot.person is not None:
                        peopleInQueue += 1
                gentePorHora.append(peopleInQueue)
                temporizador = 0
            else:
                temporizador += 1

        promedioRedondeado = round(np.average(gentePorHora))
        print('Con {0} cajas, el promedio de personas en total es de {1}'.format(caja, promedioRedondeado))
        mejorActual = promedioRedondeado if promedioRedondeado < mejorActual else mejorActual
        cajaList.clear()
        gentePorHora.clear()
        cola.clear()
        caja += 1
        temporizador = 0