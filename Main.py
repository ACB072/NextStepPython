import os
import platform
from prettytable import PrettyTable
from termcolor import colored
from EjerciciosAntonio import Ejercicio1
from EjerciciosAntonio import Ejercicio2
from EjerciciosAntonio import Ejercicio3
from EjerciciosAntonio import Ejercicio4
from EjerciciosAntonio import Ejercicio5
from ejerciciosM import ejercicio6
from ejerciciosM import ejercicio7
from ejerciciosM import ejercicio8
from ejerciciosM import ejercicio9
from ejerciciosM import ejercicio10
from ejerciciosM import ejercicio11

while True:
    if platform.system() == "Windows":
        os.system("cls")
        print("mac")
    elif platform.system() == "Darwin":
        os.system("clear")

    # print("Bienvenidos")
    # print("Menu principal")
    # tabla = PrettyTable()
    # tabla.field_names = ["#", "Descripción"]
    # tabla.add_row([colored("1", "blue"), colored("1-Crea un programa en Python que acepte una fecha como cadena de caracteres", "green")])
    # print("2-Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona.")
    # print("3-Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene. ")
    # print("4-Crea un programa que le pida al usuario una hora en formato hh:mm y luego calcule y muestre la hora en 24 horas")
    # print("5-Crea un programa en Python que acepte una cadena de caracteres y devuelva la cadena invertida")
    # print("6-Crea un programa que le pida al usuario un número entero y luego calcule y muestre la suma de todos los números desde 1 hasta el número ingresado.")
    # print("7-Crea un programa que le pida al usuario una cadena de caracteres y luego imprima cada carácter en una línea separada.")
    # print("8-Crea un programa en Python que acepte una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que tienen más de 5 caracteres. ")
    # print("9-Crea un programa en Python donde la entrada sean una cadena de caracteres, una palabra y una palabra de reemplazo ,el resultado debe ser la cadena con todas las ocurrencias de la palabra reemplazadas por otra palabra.")
    # print("10-Crea un un programa en Python que tome una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que contienen al menos una vocal.")

    tabla = PrettyTable()
    tabla.field_names = ["Bienvenidos"]
    tabla.align["Bienvenidos"] = "c"
    tabla.add_row([colored("Menu principal", "red")])
    print(colored(tabla.get_string(), "red"))

    tabla = PrettyTable()
    tabla.field_names = ["#", "Descripción"]
    tabla.align["Descripción"] = "l"
    tabla.add_row([colored("1", "blue"), colored("Fecha como cadena de caracteres", "green")])
    tabla.add_row([colored("2", "blue"), colored("Busca tu zona horaria y la hora.", "green")])
    tabla.add_row([colored("3", "blue"), colored("Calcula el número de palabras que contiene una cadena.", "green")])
    tabla.add_row([colored("4", "blue"), colored("Convertir la hora en 24 horas.", "green")])
    tabla.add_row([colored("5", "blue"), colored("Invierte una cadena", "green")])
    tabla.add_row([colored("6", "blue"), colored("Calcular del numero ingresado hasta 1.", "green")])
    tabla.add_row([colored("7", "blue"), colored("Imprime cada caracter en una cadena separada.", "green")])
    tabla.add_row([colored("8", "blue"), colored("Seleccionar las cadenas que tiene más de 5 caracteres.", "green")])
    tabla.add_row([colored("9", "blue"), colored("reemplazar palabras.", "green")])
    tabla.add_row([colored("10", "blue"), colored("Crea una lista con cadenas que tengan vocales.", "green")])
    tabla.add_row([colored("0", "blue"), colored("Salir", "green")])
    print(colored(tabla.get_string(), "blue"))
    opcion = input("Seleccione una opción:")
    if opcion == "1":
        Ejercicio1.principal()
    elif opcion == "2":
        Ejercicio2.principal()
    elif opcion == "3":
        Ejercicio3.principal()
    elif opcion == "4":
        Ejercicio4.principal()
    elif opcion == "5":
        Ejercicio5.principal()
    elif opcion == "6":
        ejercicio6.SumNum()
    elif opcion == "7":
        ejercicio7.CadenaCar()
    elif opcion == "8":
        ejercicio8.Cadena5Car()
    elif opcion == "9":
        ejercicio9.reempCadena()
    elif opcion == "10":
        ejercicio10.Vocal()
    elif opcion == "11":
        ejercicio11.Multiplos3()
    elif opcion == "0":
        print("Adios :)")
        break
    continuar=input("Presione enter para continuar...")