num = int (input("Ingrese el numero par "))

mitad = num/2
par = num%2
if par ==0: 
    if num>=0: 
        for i in range (0,num+1) :
            if i < mitad :
                print(i,"LEONARDO")
            else:
                if i > mitad:
                    print(i,"Alarcon")
                else:
                    print(i,"mitad")
    else:
        for i in range (num,0+1) :
            if i < mitad :
                print(i,"LEONARDO")
            else:
                if i > mitad:
                    print(i,"Alarcon")
                else:
                    print(i,"mitad")
else:
    print("No es numero par ")
#MISMO EJERCICIO CON DECIMALES Y VALIDAR NUMEROS NEGATIVOS