
import math

#FUNCIÓN PARA CALCULAR EL ÁREA DEL CUADRADO
def area_cuadrado(Lado):
    Lado = int(input("INGRESE EL LADO DEL CUADRADO ES :"))
    calc = Lado**2
    print("EL AREA DEL CUADRADO ES : ", calc)

#FUNCIÓN PARA CALCULAR EL ÁREA DEL RECTÁNGULO
def area_rectangulo(base, altura):
    base = int(input("INGRESE LA BASE DEL RECTANGULO : "))
    altura = int(input("INGRESE LA ALTURA DEL RECTANGULO: "))
    calc = base * altura
    print("EL AREA DEL RECTANGULO ES ", calc)

#FUNCIÓN PARA CALCULAR EL ÁREA DEL TRIÁNGULO
def area_triangulo(base, altura):
    base = int(input("INGRESE LA BASE DEL TRIANGULO : "))
    altura = int(input("INGRESE LA ALTURA DEL TRIANGULO: "))
    calc = base * altura/2
    print("EL AREA DEL TRIANGULO ES : ", calc)

#FUNCIÓN PARA CALCULAR EL ÁREA DEL CÍRCULO
def area_circulo(radio):
    radio = int(input("INGRESE EL RADIO DEL CIRCULO : "))
    calc = math.pi * radio ** 2
    print(" EL AREA DEL CIRCULO ES :", calc)

#DEFINIMOS LA VARIABLE CONTINUAR COMO TRUE PARA CUANDO YA NO SE DESEE CORRER EL PROGRAMA SEA = A FALSE
continuar = True
#CICLO WHILE PARA MOSTRAR EL MENÚ MIENTRAS SE DESEE CONTINUAR 
while continuar:
    print("MENÚ")
    print("1. AREA DEL CUADRADO ")
    print("2. AREA DEL RECTÁNCGULO ")
    print("3. AREA DEL TRIÁNGULO ")
    print("4. AREA DEL CÍRCULO ")
    opciones = int(input("INGRESE LA OPERACION QUE DESEA REALIZAR :"))
    if opciones == 1:                                   #CONDICIÓN PARA MOSTAR LA FUNCIÓN DEPENDIENDO AL NÚMERO QUE SE INGRESE
        area_cuadrado(Lado="")                          #SE LLAMA A LA FUNCIÓN CON SUS PARAMETROS DEFINIDOS CON COMILLAS YA QUE EN LA FUNCIÓN CON INPUT DEFINIRÁ QUE VALORES TOMAN ESTOS PARÁMETROS
    else:
        if opciones == 2:
            area_rectangulo(base="", altura="")
        else:
            if opciones == 3:
                area_triangulo(base="", altura="")
            else:
                if opciones == 4:
                    area_circulo(radio="")
                else:
                    print("INGRESE UNA OPCIÓN CORRECTA PORFAVOR")
                    print("")
    con = input("DESEA CONTINUAR EL PROGRAMA? Si---No ")        #SE CREA LA VARIABLE PARA INGRESAR SI DESEA CONTINUAR CON EL PROGRAMA O NO
    if con == "Si" or con == "SI":                              #LA CONDICIÓN NOS INDICA QUE SI PONEMOS Si o SI CON MAYÚSCULAS EL PROGRAMA SE SIGUE EJECUTANDO POR LA INSTRUCCIÓN CONTINUE
        continue                                                #CONTINUE VUELVE AL INCIO DEL BUCLE WHILE A EVALUAR LA CONDICIÓN
    else:                                                       
        if con == "No" or con == "NO":                          #Y AQUÍ ESTÁ LA CONDICIÓN EN LA QUE SI SE INGRESA No o NO continuar es igual a False y nos imprime hasta la vista concluyendo el programa 
            continuar = False
            print("HASTA LA VISTA ")
