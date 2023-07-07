print("Ingrese su nombre") 
nombre = input() #Obtenemos el nombre
print("Ingrese su apellido")
apellido = input() #Obtenemos el apellido

print("Ingrese un numero")
num = int(input("")) #Ingreso de un número que será el límite de la secuencia

print("Ingrese el rango de decimales en los que se dividirá la secuencia")
print("--Por ejemplo: 0.5--")
rango = float(input("")) #Obtenemos el rango de decimales

print("-----------------------------------")
veces = int(num/rango)  #cuantas VECES se repite o se suma el rango hasta llegar al límite final
                        #se convierte en entero para que pueda ser leído por el bucle "for"

ctrl_suma = 0 #permitira sumar el rango de números por cada iteración|
mitad = num/2 #obtenemos la mitad del numero 

if (num > 0): #numeros positivos
    for i in range (0,veces+1,1):
        if (ctrl_suma>mitad and ((ctrl_suma-rango)<mitad)):     #if que permite insertar la mitad en la lista cuando la mitad
            print(mitad," <---- es la mitad")                   #no recorra por la mitad y por ello no pueda leerlo
            print(ctrl_suma, " ", apellido)
            ctrl_suma = round((ctrl_suma+rango),2)
        else: 
            if(ctrl_suma == mitad):                              #if que permite imprimir la 'mitad' cuando si lo recorre en la lista
                print(mitad," <---- es la mitad")
                ctrl_suma = round((ctrl_suma+rango),2) 
            else: 
                if(ctrl_suma < mitad):
                    print(ctrl_suma," ", nombre )
                    ctrl_suma = round((ctrl_suma+rango),2)
                else:
                    if (ctrl_suma>mitad):
                        print(ctrl_suma," ", apellido)
                        ctrl_suma = round((ctrl_suma+rango),2)
                    else:
                        print("Algo salió mal")
    
    # código para completar todos los números
    num = float(num)
    if(num == ctrl_suma-rango):
        print("")
    else:
        print(num, " ", apellido)           

else: #numeros negativos
    for i in range (veces,0+1,1):
        if (ctrl_suma>mitad and ((ctrl_suma+rango)<mitad)):
            print(mitad," <---- es la mitad")
            print(ctrl_suma, " ", apellido)
            ctrl_suma = round((ctrl_suma-rango),2)
        else: 
            if(ctrl_suma == mitad):
                print(mitad," <---- es la mitad")
                ctrl_suma = round((ctrl_suma-rango),2) 
            else: 
                if(ctrl_suma > mitad):
                    print(ctrl_suma," ", nombre )
                    ctrl_suma = round((ctrl_suma-rango),2)
                else:
                    if (ctrl_suma < mitad):
                        print(ctrl_suma," ", apellido)
                        ctrl_suma = round((ctrl_suma-rango),2)
                    else:
                        print("Algo salió mal")   
    # código para completar todos los números
    num = float(num)
    if(num == ctrl_suma+rango):
        print("")
    else:
        print(num, " ", apellido)