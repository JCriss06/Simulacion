def congruencialMultiplicativo(a, seed, m, maximum):
    x = seed
    print("Congruencial Multiplicativo")
    for i in range(maximum):
        x = (a * x) % m
        print("Numero "+str(i + 1)+":", x)

if __name__ == "__main__":
    #congruencialMultiplicativo(403,3,10000,100)
    congruencialMultiplicativo(7,64,1020,100)