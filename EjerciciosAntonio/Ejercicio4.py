#4. Crea un programa que le pida al usuario una hora en formato "hh:mm" y luego calcule y muestre la hora en 24 horas (por ejemplo, "19:30" se convertiría en "19:30"). 
#   La hora debe ser validada para asegurarse de que esté en el formato correcto y de que las horas y los minutos sean números enteros.
from datetime import datetime, timedelta
date=input("Introduce la hora con el formato hh:mm :")
dateobj=date
try:
      dateobj= datetime.strptime(dateobj, '%H:%M')
except:
        print("Formato de hora introducido erroneo")
else: 
        
        print(dateobj.strftime("%H:%M"))
finally:
       print("Fin del programa")