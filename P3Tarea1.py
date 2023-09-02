import sys

def removerDigitos(num_str, k):
    lista = []
    for digito in num_str:
        while k > 0 and len(lista) != 0 and lista[-1] > digito:
            lista.pop()
            k -= 1
        lista.append(digito)

    while k > 0:
        lista.pop()
        k -= 1
        
    resultado = ''.join(lista)
    return int(resultado)

     
def main():
    linea = sys.stdin.readline()
    ncasos = int(linea)
    linea = sys.stdin.readline()
    for i in range(0,ncasos):
        numeros = [num for num in linea.split()]
        respuesta = removerDigitos(numeros[0].strip("'"), int(numeros[1]))
        print(respuesta)
        linea = sys.stdin.readline()

main()