# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

from modules.Nodo import Nodo

class ListaDobleEnlazada:
    def __init__(self):
        # Inicializar cabeza y cola de la lista doblemente enlazada
        self.cabeza = None
        self.cola = None
        self.tamano = 0

    def esta_vacia(self):
        if self.cabeza is None:
            return True
        return False
    
    def Agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamano += 1
    
    def Agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamano += 1
    
    def insertar(self, posicion):
        pass

    def extraer(self, posicion):
        pass

    def copiar(self):
        nueva_lista = ListaDobleEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            nueva_lista.Agregar_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return nueva_lista
    
    def invertir(self):
        pass

    def concatenar(self, lista):
        pass

    def __len__(self):
        return self.tamano
    
    def __add__(self, lista):
        pass
    
    def __iter__(self):
        pass