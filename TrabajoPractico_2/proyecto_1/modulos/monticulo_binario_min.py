class MonticuloBinarioMin:
    def __init__(self):
        #Se almacena el monticulo en una lista
        self.monticulo = [0]
        self.tamano = 0
    
    def esta_vacia(self):
        return len(self.monticulo) == 0
    

    def infiltArriba(self, i):
        while i // 2 > 0:
            if self.monticulo[i] < self.monticulo[i // 2]: #el hijo es menor que el padre? Si: Hace el intercambio
                tmp = self.monticulo[i // 2]
                self.monticulo[i//2] = self.monticulo[i]
                self.monticulo[i] = tmp
        i = i//2

    def insertar(self,k):
        self.monticulo.append(k)
        self.tamano =+ 1
        self.infiltArriba(self.tamano)
    
    def infiltAbajo(self, i):
        while (i * 2) <= self.tamano:
            hm = self.hijoMin(i)
            if self.monticulo[i] > self.monticulo[hm]:
                tmp = self.monticulo[i]
                self.monticulo[i] = self.monticulo[hm]
                self.monticulo[hm] = tmp
            i = hm 

    
    def hijoMin(self, i):
        if i*2 + 1 > self.tamano:
            return i*2 
        else:
            if self.monticulo[i*2] < self.monticulo[i*2 +1]:
                return i*2
            else:
                return i*2 + 1
            
    
    def eliminarMin(self):
        valorSacado = self.monticulo[1]
        self.monticulo[1] = self.monticulo[self.tamano]
        self.tamano = self.tamano - 1 
        self.monticulo.pop()
        self.infiltAbajo(1)
        return valorSacado
    

    def construirMonticulo(self, lista):
        i = len(lista) // 2
        self.tamano = len(lista)
        self.monticulo = [0] + lista[:]
        while (i > 0): 
            self.infiltAbajo(i)
            i = i - 1



if __name__ == "__main__":
    miMonticulo = MonticuloBinarioMin()
    miMonticulo.construirMonticulo([9,5,6,2,3])

    print(miMonticulo.eliminarMin())
    print(miMonticulo.eliminarMin())
    print(miMonticulo.eliminarMin())
    print(miMonticulo.eliminarMin())
    print(miMonticulo.eliminarMin())