def congruencialMixto(maximum, a, c, m, seed):
    x = seed
    for i in range(maximum):
        x = (a * x + c) % m
        print( x)


if __name__ == "__main__":
    #a = 21
    #c = 221
    #m = 100
    #maximum = 100
    #seed = 5

    #congruencialMixto(100,21,221,100,5)
    congruencialMixto(20,81,89,102,5)