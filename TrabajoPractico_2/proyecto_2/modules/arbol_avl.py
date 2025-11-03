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
    

    def __delitem__(self, clave):
        self.eliminar(clave)


    def eliminar(self, clave):
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave, self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano - 1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')
        self.actualizarEquilibrio(nodoAEliminar)
    


    def remover(self, nodoActual):
        if nodoActual.esHoja():  # hoja
            if nodoActual.padre is None:  # es la raíz
                self.raiz = None
            else:
                if nodoActual == nodoActual.padre.hijoIzquierdo:
                    nodoActual.padre.hijoIzquierdo = None
                else:
                    nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneAmbosHijos():  # interior
            suc = nodoActual.encontrarSucesor()
            suc.empalmar()
            nodoActual.clave = suc.clave
            nodoActual.valor = suc.valor
        else:  # este nodo tiene un (1) hijo
            if nodoActual.tieneHijoIzquierdo():
                if nodoActual.padre is None:  # es la raíz
                    self.raiz = nodoActual.hijoIzquierdo
                    self.raiz.padre = None
                else:
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    if nodoActual.esHijoIzquierdo():
                        nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                    else:
                        nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
            else:
                if nodoActual.padre is None:  # es la raíz
                    self.raiz = nodoActual.hijoDerecho
                    self.raiz.padre = None
                else:
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    if nodoActual.esHijoIzquierdo():
                        nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                    else:
                        nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho

            




    def obtener(self, clave):
        if self.raiz:
            res = self._obtener(clave, self.raiz)
            if res:
                return res.valor
            else:
                return None
        else:
            return None
        
    

    def _obtener(self,clave, nodoActual):
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave,nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave,nodoActual.hijoDerecho)



    def agregar(self, clave, valor):
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
        self.tamano += 1
    

    def __setitem__(self, c, v):
        self.agregar(c, v)


    def _agregar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre = nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre = nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoDerecho)
        

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
                self.actualizarEquilibrio(nodo.padre)
    

    def rotarIzquierda(self, rotRaiz):
        nuevaRaiz = rotRaiz.hijoDerecho
      #  if nuevaRaiz is None:
       #     return
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz 
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio +1 - max(rotRaiz.factorEquilibrio, 0)



    def rotarDerecha(self, rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo
 #       if nuevaRaiz is None:
  #          return
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz =nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                 rotRaiz.padre.hijoDerecho = nuevaRaiz
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio +1 - max(rotRaiz.factorEquilibrio, 0)
            




    def reequilibrar(self, nodo):
        if nodo is None:
            return
        if nodo.factorEquilibrio < 0:
            if nodo.hijoDerecho.factorEquilibrio > 0:
                self.rotarDerecha(nodo.hijoDerecho) 
                self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
            if nodo.hijoIzquierdo.factorEquilibrio < 0:
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
            else:
                self.rotarDerecha(nodo)





class NodoArbol:
    def __init__(self, clave, valor, izquierdo = None, derecho = None, padre = None):
        self.clave = clave
        self.valor = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0
    
    def __iter__(self):
        if self:
            if self.tieneHijoIzquierdo():
                
                for elem in self.hijoIzquierdo:
                    yield elem
            yield self.clave
            if self.tieneHijoDerecho():
                for elem in self.hijoDerecho:
                    yield elem


                    

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo
    

    def tieneHijoDerecho(self):
        return self.hijoDerecho
    
    def tieneAmbosHijos(self):
        return self.hijoDerecho is not None and self.hijoIzquierdo is not None
    

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self
    

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self
    

    def esRaiz(self):
        return not self.padre
    

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)
    

    def tieneHijo(self):
        return self.hijoDerecho is not None or self.hijoIzquierdo is not None
    

    def reemplazarDatos(self, clave, valor, hijo_izq, hijo_der):
        self.clave = clave
        self.valor = valor
        self.hijoIzquierdo = hijo_izq
        self.hijoDerecho = hijo_der
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

    
    def encontrarSucesor(self):
        suc = None
        if self.tieneHijoDerecho():
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
               if self.esHijoIzquierdo():
                   suc = self.padre
               else:
                   self.padre.hijoDerecho = None
                   suc = self.padre.encontrarSucesor()
                   self.padre.hijoDerecho = self
        return suc

    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual
    

    def empalmar(self):
       if self.esHoja():
           if self.esHijoIzquierdo():
                  self.padre.hijoIzquierdo = None
           else:
                  self.padre.hijoDerecho = None
       elif self.tieneAlgunHijo():
           if self.tieneHijoIzquierdo():
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoIzquierdo
                  else:
                     self.padre.hijoDerecho = self.hijoIzquierdo
                  self.hijoIzquierdo.padre = self.padre
           else:
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoDerecho
                  else:
                     self.padre.hijoDerecho = self.hijoDerecho
                  self.hijoDerecho.padre = self.padre






if __name__ == "__main__":
     arbol = ArbolAVL()

     #arbol.agregar(1, 1)
     #arbol.agregar(2, 2)
     #arbol.agregar(3, 3)

     arbol.agregar(9, 9)
     arbol.agregar(7, 7)
     arbol.agregar(5, 5)

     arbol.eliminar(9)

     for i in arbol:
         print(i)

    #



