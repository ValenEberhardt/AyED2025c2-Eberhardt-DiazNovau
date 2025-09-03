class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return str(self.dato)
   




if __name__ == "__main__":
    nodo1 = Nodo(3)
    nodo2 = Nodo(5)
    
    nodo2.siguiente = nodo1
    #nodo1.__anterior = nodo2

    print(nodo2.siguiente)