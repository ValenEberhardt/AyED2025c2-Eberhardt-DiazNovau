from modules.ordenamiento_burbuja import ordenamiento_burbuja
from modules.ordenamiento_quicksort import quicksort
from modules.ordenamiento_radixsort import radix_sort
from random import randint
import time
from matplotlib import pyplot as plt

#Probamos que los algoritmos funcionen correctamente 

#Lista de 700 numeros del 1 al 1000 desordenados
burbuja_time = []
quicksort_time = []
radixsort_time = []
listasort_time = [] #Haciendo referencia al ordenamiento sort de las listas ya implementadas en python

tamanios = [1, 10, 100, 200, 500, 700, 1000]

plt.figure(figsize=(10, 6))

#Ordenamiento burbuja

for n in tamanios:
    numeros = [randint(1, 10000) for _ in range(n)]
    
    inicio = time.perf_counter()
    burbuja_numeros = ordenamiento_burbuja(numeros)
    fin = time.perf_counter()
    burbuja_time.append(fin - inicio)


#Ordenamiento quicksort

for n in tamanios:
    numeros = [randint(1, 10000) for _ in range(n)]
    
    inicio = time.perf_counter()
    quicksort_numeros = quicksort(numeros)
    fin = time.perf_counter()
    quicksort_time.append(fin - inicio)


#Ordenamiento RadixSort

for n in tamanios:
    numeros = [randint(1, 10000) for _ in range(n)]
    
    inicio = time.perf_counter()
    radix_sort_numeros = radix_sort(numeros)
    fin = time.perf_counter()
    radixsort_time.append(fin - inicio)


#Ordenamiento de listas incorporadas en python
for n in tamanios:
    numeros = [randint(1, 10000) for _ in range(n)]
    
    inicio = time.perf_counter()
    numeros.sort
    fin = time.perf_counter()
    listasort_time.append(fin - inicio)

#Grafico de los tiempos de cada tipo de ordenamiento segun tamaño de la lista 
plt.plot(tamanios, burbuja_time, marker='o', label='Burbuja')
plt.plot(tamanios, quicksort_time, marker='o', label='Quicksort')
plt.plot(tamanios, radixsort_time, marker='o', label='Radix Sort')
plt.plot(tamanios, listasort_time, marker='o', label='Sort de Python')

plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de ordenamiento')
plt.legend() 
plt.grid() 
plt.show()