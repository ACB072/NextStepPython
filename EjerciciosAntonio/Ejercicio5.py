#5. Crea un programa en Python que acepte una cadena de caracteres y devuelva la cadena invertida (por ejemplo, "hola" se convertiría en "aloh"). 

#El programa debe utilizar un bucle `for` para recorrer la cadena y construir la cadena invertida.

print("Programa invertir Cadena")
cadena=input("Introduce la cadena de texto :")

cadena_invertida= ""
for char in  cadena:
    cadena_invertida= char + cadena_invertida;

print(cadena_invertida)
   