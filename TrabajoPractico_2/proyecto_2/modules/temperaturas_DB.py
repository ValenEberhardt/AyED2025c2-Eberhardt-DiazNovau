from modules.arbol_avl import ArbolAVL, NodoArbol
from datetime import datetime

class Temperturas_DB:

    def __init__(self):
        self.temperaturas = ArbolAVL()


    
    def formato_fecha(self, fecha):
        fecha = datetime.strptime(fecha, "%d/%m/%Y")
        return fecha
        


    def guardar_temperatura(self, temperatura, fecha):
        fecha_dt = self.formato_fecha(fecha)
        self.temperaturas.agregar(fecha_dt, temperatura)


    
    def devolver_temperatura(self,fecha):
        fecha_dt = self.formato_fecha(fecha)
        temp = self.temperaturas.obtener(fecha_dt)
        return temp
    
        



    def max_temp_rango(self, fecha1, fecha2):
        pass



    def min_temp_rango(self, fecha1, fecha2):
        pass



    def temp_extremos_rango(self, fecha1, fecha2):
        pass



    def borrar_temperatura(self, fecha):
        pass



    def devolver_temperaturas(self, fecha1, fecha2):
        pass



    def cantidad_muestras(self):
        pass

if __name__ == "__main__":
     
    temp = Temperturas_DB()

    print(temp.formato_fecha("20/04/2025"))
        
