import sys


def num_faltante(x):
    n = len(x)+1
    suma=0
    for i in x:
        suma+=i

    total= (n*(n+1))/2


    faltante = total-suma

    return int(faltante)



def main():
    linea = sys.stdin.readline()
    n_casos = int(linea)
    linea = sys.stdin.readline()
    for i in range(0, n_casos):
        numeros = [int(num) for num in linea.split()]
        respuesta = num_faltante(numeros)
        print(respuesta)
        linea = sys.stdin.readline()


main()
