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
        self.tamanio = 0

    def esta_vacia(self):
        if self.cabeza is None:
            return True
        
        return False
    
    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1
    
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1
    
    def insertar(self, item, posicion = None): 

        if posicion == None:
            self.agregar_al_final(item)
        
        elif posicion == 0:
            self.agregar_al_inicio(item)

        elif posicion > self.tamanio or posicion < 0: 
            raise ValueError

        elif posicion > 0 and posicion < self.tamanio:
            nuevo_nodo = Nodo(item)
            actual = self.cabeza

            for i in range(posicion):
                actual = actual.siguiente
            
            nuevo_nodo.anterior = actual.anterior
            nuevo_nodo.siguiente = actual
            actual.anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
            self.tamanio += 1

            #print("Nodo actual "+ nuevo_nodo.dato + " Nodo anterior " + nuevo_nodo.anterior + " Nodo siguiente " + nuevo_nodo.siguiente)



    def extraer(self, posicion=None): #Como hacer que la posicion no se un parametro obligatorio?

        if posicion == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is not None:
                self.cabeza.anterior = None
            else:
                self.cola = None
            self.tamanio -= 1

            return dato
        

        elif posicion == self.tamanio - 1 or posicion == None:
            dato = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola is not None:
                self.cola.siguiente = None
            else:
                self.cabeza = None
            self.tamanio -= 1

            return dato
        
        elif posicion > 0 and posicion < self.tamanio-1:
            actual=self.cabeza
            for i in range(posicion):
                actual=actual.siguiente
            dato=actual.dato
            actual.anterior.siguiente=actual.siguiente
            actual.siguiente.anterior=actual.anterior
            self.tamanio -= 1
            return dato
        
        
        elif self.esta_vacia():
            raise ValueError("La lista está vacía")
        elif posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición fuera de rango")
        
        



    def copiar(self):
        nueva_lista = ListaDobleEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            nueva_lista.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return nueva_lista
    

    def invertir(self):
        actual=self.cola
        while actual is not None:
            actual.anterior,actual.siguiente=actual.siguiente,actual.anterior
            actual=actual.siguiente
        self.cola,self.cabeza=self.cabeza,self.cola

        return self
            

    def concatenar(self, lista):
        lista_alterada=self.copiar()
        actual=lista.cabeza
        for i in range(1, lista.tamanio):
            lista_alterada.agregar_al_final(actual)
            actual=actual.siguiente
        lista_alterada.cola=actual


        return lista_alterada

    def __len__(self):
        return self.tamanio
    
    def __add__(self, lista):
        self.concatenar(lista)
        return self
        
    
    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
        pass


    def __str__(self):
        # sirve para poder mostrar el contenido de una LDE por consola con la función print
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <> ".join(elementos)


if __name__ == "__main__":


    prueba = ListaDobleEnlazada()

    prueba.agregar_al_final(3)
    prueba.agregar_al_inicio(1)

    prueba.insertar(2, 1)
    
    prueba.invertir()
    print(prueba)

