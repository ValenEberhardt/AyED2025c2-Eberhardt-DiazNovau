from modules.ListaDobleEnlazada import ListaDobleEnlazada,Nodo
from matplotlib import pyplot as plt
from random import randint
import time

"""tamanos = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

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
"""

lista = ListaDobleEnlazada()

def medir_tiempo(funcion, lista):
    inicio = time.time()
    funcion(lista)
    fin = time.time()
    return fin - inicio

tam_listas = [11, 123, 544, 1386, 5753, 13798]
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

for tam in tam_listas:
    lista = ListaDobleEnlazada()
    
    # Agregar elementos a la lista
    for i in range(tam):
        lista.agregar_al_final(i)
    
    # Medir tiempo de len
    tiempos_len.append(medir_tiempo(lambda x: len(x), lista))
    
    # Medir tiempo de copiar
    tiempos_copiar.append(medir_tiempo(lambda x: x.copiar(), lista))
    
    # Medir tiempo de invertir
    tiempos_invertir.append(medir_tiempo(lambda x: x.invertir(), lista))

# Graficar los resultados
plt.plot(tam_listas, tiempos_len, label='len', marker='o')
plt.plot(tam_listas, tiempos_copiar, label='copiar', marker='o')
plt.plot(tam_listas, tiempos_invertir, label='invertir', marker='o')
plt.xlabel('Cantidad de elementos N')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de métodos len, copiar, invertir')
plt.legend()
plt.grid(True)
plt.show()





