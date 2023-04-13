#2. Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona. 
#El programa debe manejar excepciones en caso de que la zona horaria ingresada no sea válida.

from datetime import datetime, timedelta

from pytz import timezone
import pytz

print (pytz.all_timezones)
zona=input("Introduce la zona horaria que deseas ver, con el formato Continente/Localizacion: ")
try:
        zonatiempo=timezone(zona)
        print(datetime.now(timezone(zona)))
except pytz.exceptions.UnknownTimeZoneError:
        print("Debe ser una zona horaria valida")
