from modules.ordenamiento_burbuja import ordenamiento_burbuja
from modules.ordenamiento_quicksort import quicksort
from modules.ordenamiento_radixsort import radix_sort
from random import randint

#Probamos que los algoritmos funcionen correctamente 

#Lista de 700 numeros del 1 al 1000 desordenados
numeros = []

for i in range(700):
    n = randint(1,1000)
    numeros.append(n)

print("Lista desordenada " , numeros)


#Ordenamiento burbuja
    
burbuja_numeros = ordenamiento_burbuja(numeros)
print("\nLista ordenada con Ordenamiento Burbuja " , burbuja_numeros)

#Ordenamiento quicksort

quicksort_numeros = quicksort(numeros)
print("\nLista ordenada con Ordenamiento Quicksort " , quicksort_numeros)

radixsort_numeros = radix_sort(numeros)
print("\nLista ordenada con Ordenamiento Radixsort " , radixsort_numeros)


if burbuja_numeros == quicksort_numeros and radixsort_numeros:
    print("\n Las listas son iguales")
else:
    print("\n las listas no son iguales")