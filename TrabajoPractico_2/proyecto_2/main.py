from modules.temperaturas_DB import Temperturas_DB


ruta = "./data/muestras.txt"

db = Temperturas_DB()
with open(ruta, "r") as texto:
    # contenido = texto.read()
    # linea = texto.readline()
    # fecha, temp = linea.strip().split(";")
    # print(fecha)
    for linea in texto:
        fecha, temp = linea.split(";")
        db.guardar_temperatura(temp, fecha)





    
#Pruebas de uso de las funciones


#Guardar temperatura y Devolver teperatura:
db.guardar_temperatura(16, '11/7/2025')
print(db.devolver_temperatura("11/07/2025")) 

#Temperatura máxima y mínima en un rango (fecha1, fecha2):
fecha1 = '01/01/2025'
fecha2 = '31/01/2025'
max = db.max_temp_rango(fecha1, fecha2)
min = db.min_temp_rango(fecha1, fecha2)
print("Maxima del mes de enero: ", max, "Minima del mes de enero:", min)

#Temperatura minima y maxima en una misma funcion
min, max = db.temp_extremos_rango(fecha1, fecha2) #('11.9\n', '39.5\n')
print(min, max)






      

