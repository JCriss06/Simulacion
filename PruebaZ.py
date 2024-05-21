import math
def pruebaZ(x_testada, N):
    z = ((x_testada - 1/2) * math.sqrt(N)) / (math.sqrt(1/12))
    vabsoluto = abs(z)
    print('|Z| =', vabsoluto)
    if vabsoluto < 1.96:
        print("Los numeros son Aleatorios")
    else:
        print("Los numeros NO son Aleatorios")

if __name__ == "__main__":
    archivo = open('Apendice A.txt','r' )
    suma = 0
    contador = 0
    for linea in archivo:
        elementos = linea.strip().split('\t')
        for elemento in elementos:
            numero = float('.' + elemento)

            suma += numero
            contador += 1
    x_testada = suma / contador

    pruebaZ(x_testada,contador)