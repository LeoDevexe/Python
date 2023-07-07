# OPERADORES ARITMÉTICOS
num1 = float(input("Ingrese el primer número "))
num2 = float(input("Ingrese el segundo número "))


# MENÚ DE OPERACIONES
print("MENÚ")
print("1. SUMA")
print("2. RESTA")
print("3. MULTIPLICACIÓN")
print("4. DIVISON")
print("5. POTENCIA")


opciones = input("INGRESE LA OPERACION QUE DESEA REALIZAR :")

# if anidado
if opciones == '1':
    suma = num1+num2
    print("Usted escogió SUMA ", suma)
else:
    if opciones == '2':
        resta = num1-num2
        print("Usted escogió RESTA", resta)
    else:
        if opciones == '3':
            mult = num1*num2
            print("Usted escogió MULTIPLICACION", mult)
        else:
            if opciones == '4':
                if num2 == 0:
                    print("No existe la division para 0 ")
                else:
                    div = num1/num2
                    print("Usted escogió DIVISION", div)
            else:
                if opciones == '5':
                    pot = num1**num2
                    print("Usted escogió POTENCIA", pot)
                else:
                    print("INGRESE UNA OPCIÓN CORRECTA")
