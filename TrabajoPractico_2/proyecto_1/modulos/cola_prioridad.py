from modulos.monticulo_binario_min import MonticuloBinarioMin

class ColaPrioridad:
    def __init__(self):
        self.cola = MonticuloBinarioMin()

    def agregar(self, item):
        self.cola.insertar(item)
    
    def eliminar(self):
        return self.cola.eliminarMin()
        

    def __len__(self):
        return len(self.cola.monticulo)
    
    def __iter__(self):
        return iter(self.cola)
    

if __name__ == "__main__":

    x = ColaPrioridad()

    x.agregar(3)
    x.agregar(2)
    x.agregar(1)
    
    for i in x:
        print(i)