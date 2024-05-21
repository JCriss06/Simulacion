import random

if __name__ == "__main__":
    intervalo = 1000000
    in_Circulo = 0

    for i in range(intervalo):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if (x**2 + y**2 <= 1):
            in_Circulo += 1

    valorPI = (in_Circulo / intervalo) * 4
    print("Valor aproximado de π:", valorPI)