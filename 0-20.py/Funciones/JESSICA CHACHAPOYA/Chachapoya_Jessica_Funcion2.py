#Realizar un programa de operaciones matemáticas, suma, resta, multiplicación y división, las cuales cada operación debe ser una función.
#1.  Crear 4 funciones nominales de las operaciones suma, resta, multiplicación y división.
#2.  Crear un menú con las 4 operaciones
#3.  Seleccionar la operación a resolver con input
#4.  Validar las opciones del menú, si esta fuera de rango escribir un mensaje “La operación ingresada es incorrecta”
#5.  Ingresar dos valores num1 y num2 como números para realizar las operaciones debe admitir decimales.
#6.  En cada operación llamar a la función correspondiente para que muestre el resultado.
#7.  Al terminar la operación preguntar “¿Desea continuar en el programa?” si para que pregunte que operación se va a resolver, no escribirá “Hasta la vista” y saldrá del programa.


def Suma():#se crea la funcion 
        num1 = float(input("Ingrese el primer numero: "))#se ingresa los diguitos por teclado 
        num2= float(input("Ingrese el segundo numero: "))#se ingresa los diguitos por teclado 
        calculo = num1+num2#se hace el calculo
        print("El resultado de la suma es: ", calculo)#se desplazara el resultado
        print()

        def Resta():
            num1 = float(input("Ingrese el primer numero: "))
            num2= float(input("Ingrese el segundo numero: "))
            calculo = num1-num2
            print("El resultado de la resta es: ", calculo)
            print()
    
        def Multiplicacion():
            num1 = float(input("Ingrese el primer numero: "))
            num2= float(input("Ingrese el segundo numero: "))
            calcular = num1*num2
            print("La multiplicacion total es: ", calcular)
            print()

        def Divicion():
            num1 = float(input("Ingrese el primer numero: "))
            num2= float(input("Ingrese el segundo numero: "))
            calcular = num1/num2
            print("La divicion total es: ", calcular)
            print()

ciclo = 1  #el inicio del contador
while ciclo == 1: #ciclo de inicio y fin del programa
    print("1 Suma ")
    print("2 Resta ")
    print("3 Multiplicacion")
    print("4 Divicion")

    opc = int(input("Ingrese la opcion deseada: "))
    if opc >= 1 and opc <= 4:
        if (opc) == 1:
            Suma()
        else:
            if (opc) == 2:
                Resta()
            else:
                if (opc) == 3:
                    Multiplicacion()
                else:
                    if (opc) == 4:
                        Divicion()
                        
ciclo = int(input("diguite del 1 si desea otra opcion, diguite 2 finalizar : "))#se ingresa por teclado si desea otra opcion o finaliza
if ciclo == 1:#se condiciona el ciclo repetitivo 
    ciclo += 0 # si se diguito la opcion 1 el ciclo repetira las opciones
else:
    if ciclo == 2:# si se diguito la opcion 2 el ciclo  finalizara 
        print("Finalizo")