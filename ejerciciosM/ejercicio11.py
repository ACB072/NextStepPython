 #! 11. Crea un programa en Python que tome una lista de números enteros y devuelva una nueva lista que contenga solo los números que son múltiplos de 3. El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar los números.

def Multiplos3():
    numeros = input("Intoduce una lista de números separados por espacios: ").split()
    nuevaLista = []
    for num in numeros:
        if int(num) % 3 == 0:
            nuevaLista.append(num)
    print(nuevaLista)


