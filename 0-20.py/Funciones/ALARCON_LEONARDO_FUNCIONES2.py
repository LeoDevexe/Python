#FUNCIÓN PARA REALIZAR SUMA
def Suma(num1, num2):
    num1 = float(input("INGRESE EL PRIMER NÚMERO :"))
    num2 = float(input("INGRESE EL SEGUNDO NÚMERO :"))
    calc = num1+num2
    print("LA SUMA ES : ", calc)

#FUNCIÓN PARA REALIZAR RESTA
def Resta(num1, num2):
    num1 = float(input("INGRESE EL PRIMER NÚMERO :"))
    num2 = float(input("INGRESE EL SEGUNDO NÚMERO :"))
    calc = num1-num2
    print("LA RESTA ES : ", calc)

#FUNCIÓN PARA REALIZAR MULTIPLICACIÓN
def Multiplicacion(num1, num2):
    num1 = float(input("INGRESE EL PRIMER NÚMERO :"))
    num2 = float(input("INGRESE EL SEGUNDO NÚMERO :"))
    calc = num1*num2
    print("LA MULTIPLICACIÓN ES : ", calc)

#FUNCIÓN PARA REALIZAR DIVISIÓN
def Division(num1, num2):
    num1 = float(input("INGRESE EL PRIMER NÚMERO :"))
    num2 = float(input("INGRESE EL SEGUNDO NÚMERO :"))
    if num2 == 0:
        num2 = float(input(
            " NO EXISTE DIVISION PARA 0 INGRESE OTRO NUMERO PARA REALIZAR LA OPERACIÓN :"))
    calc = num1/num2
    print(" LA DIVISIÓN ES :", calc)

#DEFINIMOS LA VARIABLE CONTINUAR COMO TRUE PARA CUANDO YA NO SE DESEE CORRER EL PROGRAMA SEA = A FALSE
continuar = True
#CICLO WHILE PARA MOSTRAR EL MENÚ MIENTRAS SE DESEE CONTINUAR
while continuar:
    print("MENÚ")
    print("1. SUMA ")
    print("2. RESTA ")
    print("3. MULTIPLICACIÓN ")
    print("4. DIVISIÓN ")
    opciones = int(input("INGRESE LA OPERACION QUE DESEA REALIZAR :"))
    if opciones == 1:                   #CONDICIÓN PARA MOSTAR LA FUNCIÓN DEPENDIENDO AL NÚMERO QUE SE INGRESE
        Suma(num1="", num2="")          #SE LLAMA A LA FUNCIÓN CON SUS PARAMETROS DEFINIDOS CON COMILLAS YA QUE EN LA FUNCIÓN CON INPUT DEFINIRÁ QUE VALORES TOMAN ESTOS PARÁMETROS
    else:
        if opciones == 2:
            Resta(num1="", num2="")
        else:
            if opciones == 3:
                Multiplicacion(num1="", num2="")
            else:
                if opciones == 4:
                    Division(num1="", num2="")
                else:
                    print("INGRESE UNA OPCIÓN CORRECTA PORFAVOR")
                    print("")
    con = input("DESEA CONTINUAR EL PROGRAMA? Si---No ")             #SE CREA LA VARIABLE PARA INGRESAR SI DESEA CONTINUAR CON EL PROGRAMA O NO
    if con == "Si" or con == "SI":                                   #LA CONDICIÓN NOS INDICA QUE SI PONEMOS Si o SI CON MAYÚSCULAS EL PROGRAMA SE SIGUE EJECUTANDO POR LA INSTRUCCIÓN CONTINUE
        continue                                                     #CONTINUE VUELVE AL INCIO DEL BUCLE WHILE A EVALUAR LA CONDICIÓN
    else:
        if con == "No" or con == "NO":                              #Y AQUÍ ESTÁ LA CONDICIÓN EN LA QUE SI SE INGRESA No o NO continuar es igual a False y nos imprime hasta la vista concluyendo el programa 
            continuar = False
            print("HASTA LA VISTA ")
