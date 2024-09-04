'''Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
La función recibirá el mes y el año y retornará verdadero o falso.
'''

import datetime

def es_viernes_13(mes, año):
    # Crear un objeto de fecha para el 13 del mes y año dados
    fecha = datetime.date(año, mes, 13)
    
    # Verificar si el día de la semana es viernes (0=Monday, ..., 4=Friday)
    return fecha.weekday() == 4

# Ejemplo de uso
mes = 10  # Octubre
año = 2023  # Año 2023

if es_viernes_13(mes, año):
    print(f"Sí, en {mes}/{año} hay un viernes 13.")
else:
    print(f"No, en {mes}/{año} no hay un viernes 13.")


   
