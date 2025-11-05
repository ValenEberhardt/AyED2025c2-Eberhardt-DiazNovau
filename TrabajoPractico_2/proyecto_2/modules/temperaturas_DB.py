from modules.arbol_avl import ArbolAVL, NodoArbol
from datetime import datetime, timedelta

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
        fecha1_dt = self.formato_fecha(fecha1) 
        fecha2_dt = self.formato_fecha(fecha2)

        muestras = []

        while fecha1_dt <= fecha2_dt:
            temp = self.temperaturas.obtener(fecha1_dt)

            if temp is not None:
                muestras.append(temp)
            fecha1_dt += timedelta(1)
        
        maximo = max(muestras)

        return maximo

        
        



    def min_temp_rango(self, fecha1, fecha2):
        fecha1_dt = self.formato_fecha(fecha1) 
        fecha2_dt = self.formato_fecha(fecha2)

        muestras = []
        while fecha1_dt <= fecha2_dt:
            temp = self.temperaturas.obtener(fecha1_dt)

            if temp is not None:
                muestras.append(temp)
            fecha1_dt += timedelta(1)
        
        minimo = min(muestras)

        return minimo




    def temp_extremos_rango(self, fecha1, fecha2):
        fecha1_dt = self.formato_fecha(fecha1) 
        fecha2_dt = self.formato_fecha(fecha2)

        minima = self.min_temp_rango(fecha1_dt, fecha2_dt) 
        maxima = self.max_temp_rango(fecha1_dt, fecha2_dt)
        
        return minima, maxima



    def borrar_temperatura(self, fecha):
        fecha_dt = self.formato_fecha(fecha)

        self.temperaturas.eliminar(fecha_dt)
        ###Ver



    def devolver_temperaturas(self, fecha1, fecha2):
        fecha1_dt = self.formato_fecha(fecha1)
        fecha2_dt = self.formato_fecha(fecha2)

        temps = []

        while fecha1_dt <= fecha2_dt:
            temp = self.temperaturas.obtener(fecha1_dt)

            if temp is not None:
                temps.append(temp)
            fecha1_dt += timedelta(1)
            
        return temps



    def cantidad_muestras(self):
        self.temperaturas.longitud()



if __name__ == "__main__":
     
    temp = Temperturas_DB()
    temp.guardar_temperatura(30,"21/04/2025")
    temp.guardar_temperatura(29,"29/04/2025")
    temp.guardar_temperatura(20,"21/05/2025")
    temp.guardar_temperatura(15,"25/05/2025")

    fecha1 = "21/04/2025"
    fecha2 = "25/05/2025"

    print(temp.devolver_temperaturas(fecha1, fecha2))

    temp.borrar_temperatura(fecha2)
    temp.borrar_temperatura("29/04/2025")
   
    print(temp.devolver_temperaturas(fecha1, fecha2))
        
