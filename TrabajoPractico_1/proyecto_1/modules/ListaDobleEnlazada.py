# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

from modules.Nodo import Nodo

class ListaDobleEnlazada():
    def __init__(self):
        # Inicializar cabeza y cola de la lista doblemente enlazada
        self.cabeza = None
        self.cola = None
        self.tamano = 0

    def esta_vacia(self):
        if self.cabeza is None:
            return True
        return False
    
    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamano += 1