# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

#from modules.Nodo import Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return str(self.dato)
   


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
    
    def insertar(self, item, posicion):
        if posicion == None:
            self.Agregar_final(item)
        
        if posicion == 0:
            self.Agregar_inicio(item)

        if posicion > self.tamano or posicion < 0:
            raise ValueError

        if posicion > 0 and posicion < self.tamano:
            nuevo_nodo = Nodo(item)
            actual = self.cabeza

            for i in range(posicion):
                actual = actual.siguiente
            
            nuevo_nodo.anterior = actual.anterior
            nuevo_nodo.siguiente = actual
            actual.anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
            self.tamano += 1

            #print("Nodo actual "+ nuevo_nodo.dato + " Nodo anterior " + nuevo_nodo.anterior + " Nodo siguiente " + nuevo_nodo.siguiente)



    def extraer(self, posicion=None): #Como hacer que la posicion no se un parametro obligatorio?

        if posicion == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is not None:
                self.cabeza.anterior = None
            else:
                self.cola = None
            self.tamano -= 1

            return dato
        

        if posicion == self.tamano - 1 or posicion == None:
            dato = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola is not None:
                self.cola.siguiente = None
            else:
                self.cabeza = None
            self.tamano -= 1

            return dato
        
        if self.esta_vacia():
            raise ValueError("La lista está vacía")
        if posicion < 0 or posicion >= self.tamano:
            raise IndexError("Posición fuera de rango")
        
        



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

    def __str__(self):
        # sirve para poder mostrar el contenido de una LDE por consola con la función print
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)


if __name__ == "__main__":


    prueba = ListaDobleEnlazada()

    prueba.Agregar_final(3)
    prueba.Agregar_inicio(1)

    prueba.insertar(2, 1)
    
    prueba.extraer()
    
    print(prueba)

