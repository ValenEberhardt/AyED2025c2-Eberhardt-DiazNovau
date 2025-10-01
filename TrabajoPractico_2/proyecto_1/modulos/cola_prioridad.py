class ColaPrioridad:
    def __init__(self):
        #Se almacena el monticulo en una lista
        self.monticulo = []
    
    def esta_vacia(self):
        return len(self.monticulo) == 0
    
    def _intercambiar(self, i, j):
        self.monticulo[i], self.monticulo[j] = self.monticulo[j], self.monticulo[i]
        