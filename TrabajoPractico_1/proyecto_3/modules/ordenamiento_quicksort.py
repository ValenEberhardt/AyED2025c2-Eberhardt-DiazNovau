from random import randint

def quicksort(lista):
    if len(lista)<2:
        return lista

    menores, iguales, mayores = [], [], []

    #Selecciona pivote aleatorio
    pivote = lista[randint(0, len(lista) - 1)]

    for item in lista:
        #Los elementos menores al pivote van a lista "menores". Elementos mas grandes va a la lista "mayores"
        #elementos iguales al pivotes van en la lista "iguales"
        if item < pivote:
            menores.append(item)
        elif item == pivote:
            iguales.append(item)
        elif item > pivote:
            mayores.append(item)
        
    #la funcion retorna la combinacion de las listas menores, igules y mayores.
    return quicksort(menores) + iguales + quicksort(mayores)


if __name__ == "__main__":

    lista = [4, 1, 8, 2, 5, 9, 7, 6, 10, 3]

    print(quicksort(lista))