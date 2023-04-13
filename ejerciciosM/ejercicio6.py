 #! 6. Crea un programa que le pida al usuario un número entero y luego calcule y muestre la suma de todos los números desde 1 hasta el número ingresado. El programa debe utilizar un bucle `for` para sumar los números.



def SumNum():
    op = "si"
    while op == "si":
        num = int(input("Pone un número: "))
        sum = 0
        for num in range(1, num+1):
            sum = num + sum
        print(f"La suma de todos los números desde {num} hasta 1 = {sum}")

        choose = input("Quieres poner otro? 'si' o 'no': ")
        op = choose.lower()