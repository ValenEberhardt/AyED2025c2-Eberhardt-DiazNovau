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


    



print(db.devolver_temperatura("01/03/2025"))
    




      

