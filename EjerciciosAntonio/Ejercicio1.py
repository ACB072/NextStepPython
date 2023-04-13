# 1. Crea un programa en Python que acepte una fecha como cadena de caracteres en formato `"dd/mm/aaaa"` y devuelva la fecha en formato 
# `"aaaa-mm-dd"`, con el año primero. 

#  El programa debe manejar excepciones en caso de que la cadena no tenga el formato correcto.
from datetime import datetime, timedelta

print("Programa Formato Fecha")
date=input("Introduce la fecha con el formato dd/mm/aaaa :")
dateobj=date
try:
      dateobj= datetime.strptime(dateobj, '%H:%m')
except:
        print("Formato de fecha introducido erroneo")
else: 
        
        print(dateobj.strftime("%H:%m"))
finally:
       print("Fin del programa")