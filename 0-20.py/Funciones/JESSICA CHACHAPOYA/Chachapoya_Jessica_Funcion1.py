#Realizar un programa para determinar el área de cada figura geométrica, cuadrado, rectángulo, triángulo y círculo.
#1.  Crear 4 funciones para determinar el área de cada figura geométrica, cuadrado, rectángulo, triángulo y círculo.
#Formulas para calcular el área:
#Cuadrado Área=(lado)^2
#Rectángulo Área=base * altura
#Triángulo Área=(base * altura)/2
#Círculo Área= 3,141592*(radio^2)
#2.  Crear un menú con las 4 operaciones
#3.  Seleccionar la operación a resolver con input
#4.  Validar las opciones del menú, si esta fuera de rango escribir un mensaje “La operación ingresada es incorrecta”
#5.  Las variables deben estar dentro de las funciones. El input para calcular el área del cuadrado para pedir el lado debe estar dentro de la función del cuadrado y así por cada una de las variables, base y altura del rectángulo deben estar en la función rectángulo.
#6.  En cada operación llamar a la función correspondiente para que muestre el resultado.
#7.  Al terminar la operación preguntar “¿Desea continuar en el programa?” si para que pregunte que operación se va a resolver, no escribirá “Hasta la vista” y saldrá del programa.

print("*******PREGUNTA 1*********")
def area_cuadrado(lado=""): #se crea la funcion 
    lado = int(input("Ingrese el lado del cuadrado : ")) #se ingresa los diguitos por teclado 
    calcular = lado*2*2 #se hace el calculo
    print("El resultado del area del cuadrado es : ", calcular) #se desplazara el resultado


def area_rectangulo(base="", altura=""):
    base = int(input("Ingrese la base del rectangulo : "))
    altura = int(input("Ingrese la altura del rectangulo : "))
    calcular = base*altura
    print("El resultado del area del rectangulo es : ", calcular)


def area_triaungulo(base="", altura=""):
    base = int(input("Ingrese la base del triangulo: "))
    altura = int(input("Ingrese la altura del triangulo: "))
    calcular = (base*altura)/2
    print("El resultado del area del triaungulo es:", calcular)


def area_circulo(radio=""):
    radio = int(input("Ingrese el radio del circulo: "))
    calcular = 3, 141592*(radio**2)
    print("El resultado del area del radio es : ", calcular)

print("*******PREGUNTA 2********")

ciclo = 1  #el inicio del contador
while ciclo == 1: #ciclo de inicio y fin del programa
    print("opc1 area_cuadrado")#menu del programa
    print("opc2 area_rectangulo")
    print("opc3 area_triangulo")  
    print("opc4 area_circulo")
    
    print("*****PREGUNTA 3*******")
    
    opc = int(input("Ingrese la opcion deseada: "))#se ingresa por teclado la opcion
    if (opc >= 1 and opc <= 4):#se condiciona la opcion
        if opc== 1: #opcion seleccionada se realiza la operacion     
            print("Area del cuadrado")#se imprime el calculo         pregunta 5
            area_cuadrado(lado="")#se llama a la funcion   pregunta 6
        else:
            if opc== 2:
                print("Area del Rectangulo")
                area_rectangulo(base="", altura="")
            else:
                if opc== 3:
                    print("Area del Triangulo")
                    area_triaungulo(base="", altura="")
                else:
                    if opc== 4:
                        print("Area del Circulo")
                        area_circulo(radio="")
    else:
        print("Fuera del rango")#mensaje si los diguitos ingresados no son correctos
        
        print("**********PREGUNTA 7************")
        
    ciclo = int(input("diguite del 1 si desea otra opcion, diguite 2 finalizar : "))#se ingresa por teclado si desea otra opcion o finaliza
    if ciclo == 1:#se condiciona el ciclo repetitivo 
        ciclo += 0 # si se diguito la opcion 1 el ciclo repetira las opciones
    else:
        if ciclo == 2:# si se diguito la opcion 2 el ciclo  finalizara 
            print("Finalizo")