
def max_digitos(lista):
    val_max = max(lista)
    if val_max == 0:
        return 1
    return len(str(val_max))



def countig_sort(lista, pos_dig): #pos_dig posicion del digito a a evaluar
    n = len(lista)
    output = [0] * n #lista de salida de elementos ordenados
    cont = [0] * 10 #lista de almacenamiento de la cuenta de cada dígito (0-9)
    
    #Contar la frecuencia de cada digito en la pos
    for i in range(n):
        index = (lista[i] // pos_dig) % 10 
        cont[index] += 1
    
    #modificar la lista cont para almacenar la pos real de cada digito
    for i in range(1, 10):
        cont[i] += cont[i - 1]
    
    #lista de salida

    i = n - 1 
    while i >= 0:
        index = (lista[i] // pos_dig) % 10 
        output[cont[index]-1] = lista[i]
        cont[index] -= 1
        i -= 1

    #Copiar la lista de salida de la lista original
    for i in range(n):
        lista[i] = output[i]

def radix_sort(lista):
    #encontrar la cantidada de digitos
    max_d = max_digitos(lista)

    #Iniciamos pos_dig en 1 para las unidades
    pos_dig = 1
    #iteramos para cada dígito, de derecha a izq
    while max_d > 0:
        countig_sort(lista, pos_dig)
        pos_dig *= 10
        max_d -= 1
    return lista


if __name__ == "__main__":
    mi_lista = [122, 98, 567, 24, 10, 7]
    print("Lista original:", mi_lista)
    radix_sort(mi_lista)
    print("Lista ordenada:", mi_lista)

