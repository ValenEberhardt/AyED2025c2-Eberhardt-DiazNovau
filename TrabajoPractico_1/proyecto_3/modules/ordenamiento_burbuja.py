from random import randint

def ordenamiento_burbuja(lista):
    for num_pasadas in range(len(lista)-1, 0, -1):
        for j in range(num_pasadas):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenamiento_burbuja_corto(lista):
    intercambiado = True
    num_pasadas = len(lista)-1
    while num_pasadas > 0 and intercambiado:
        intercambiado = False
        for j in range(num_pasadas):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
        num_pasadas -= 1

if __name__ == '__main__':
    # ordena numeros y palabras
    numeros = []
    for i in range(3):
        n = randint(10000,99999)
        numeros.append(n)    
    
    numeros_burbuja = ordenamiento_burbuja(numeros)
    numeros_sort = sorted(numeros) #prueba ordenar los numeros con la funcion de listas de python

    print(numeros_burbuja)
    print("\n", numeros_sort)
    if numeros_burbuja == numeros_sort:
        print("EL ordenamiento burbuja funciona")

    