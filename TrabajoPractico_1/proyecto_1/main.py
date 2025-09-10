from modules.ListaDobleEnlazada import ListaDobleEnlazada
from matplotlib import pyplot as plt
from random import randint
import time

tamanos = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

tiempos_eliminar_milista = []
tiempos_eliminar_list = []


for n in tamanos:
    milista = ListaDobleEnlazada()
    lista = list()

    for _ in range(n):
        dato = randint(1, 100)
        milista.insertar(dato)
        lista.append(dato)
    
    contador = 0

    for _ in range(n):
        inicio = time.perf_counter()
        milista.extraer()
        fin = time.perf_counter()
        contador += (fin - inicio)

    tiempos_eliminar_milista.append(contador)

    contador = 0

    for _ in range(n):
        inicio = time.perf_counter()
        lista.pop()
        fin = time.perf_counter()
        contador += (fin - inicio)

    tiempos_eliminar_list.append(contador)



plt.figure(figsize=(10, 6))
plt.plot(tamanos, tiempos_eliminar_milista, marker='o', label="eliminar ListaDobleEn - O(1)")
plt.plot(tamanos, tiempos_eliminar_list, marker='o', label="eliminar lista - O(n)")
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de eliminación')
plt.legend()
plt.grid()
plt.show()







