class ArbolAVL:


    def __init__(self):
        self.raiz = None
        self.tamano = 0


    def longitud(self):
        return self.tamano
    

    def __len__(self):
        return self.tamano
    

    def __iter__(self):
        return self.raiz.__iter__()
    

    def agregar(self, clave, valor):
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
            self.tamano =+ 1
    

    def __setitem__(self, c, v):
        self.agregar(c, v)


    def _agregar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.HijoIzquierdo = NodoArbol(clave, valor, padre = nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre = nodoActual)
        

    def actualizarEquilibrio(self, nodo):
        if nodo.factorEquilibrio > 1  or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                nodo.padre.factorEquilibrio -= 1
            
            if nodo.padre.factorEquilibrio != 0:
                self.actualizarEquilibrio()




class NodoArbol:
    def __init__(self, clave, valor, izquierdo = None, derecho = None, padre = None):
        self.clave = clave
        self.valor = valor
        self.hijoizquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
    

    def tieneHijoIzquierdo(self):
        return self.hijoizquierdo
    

    def tieneHijoDerecho(self):
        return self.hijoDerecho
    

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self
    

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self
    

    def esRaiz(self):
        return not self.padre
    

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoizquierdo)
    

    def tieneHijo(self):
        return self.hijoDerecho or self.hijoizquierdo
    

    def ReemplazarDatos(self, clave, valor, hijo_izq, hijo_der):
        self.clave = clave
        self.valor = valor
        self.hijoizquierdo = hijo_izq
        self.hijoDerecho = hijo_der
        if self.tieneHijoIzquierdo():
            self.hijoizquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

