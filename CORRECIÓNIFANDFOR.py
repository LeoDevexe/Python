print("MENÚ")
print("1. SUMA")
print("2. RESTA")
print("3. MULTIPLICACIÓN")
print("4. DIVISON")
print("5. POTENCIA")
op=int(input("Ingrese la operación"))

if op>=1 and op <= 5 :
    if op ==1 :
        for num1 in range(0,11):
            print ("Tabla del",num1)
            for num2 in range (0,11):
                print(num1,"+",num2,"=",num1+num2)
    else :
        if op ==2 :
            for num1 in range(0,11):
                print ("Tabla del",num1)
                for num2 in range (0,11):
                    print(num1,"-",num2,"=",num1-num2)
        else :
            if op ==3:
                for num1 in range(0,11):
                    print ("Tabla del",num1)
                    for num2 in range (0,11):
                        print(num1,"x",num2,"=",num1*num2)
            else :
                if op ==4:
                    for num1 in range(0,11):
                        print ("Tabla del",num1)
                        for num2 in range (0,11):
                            if num2==0:
                                print(num1,"/",num2,"=""No existe division para 0")
                            else : 
                                print(num1,"/",num2,"=",num1/num2)
                else:
                    if op ==5:
                        for num1 in range(0,11):
                            print ("Tabla del",num1)
                            for num2 in range (0,11):
                                print(num1,"^",num2,"=",num1**num2)
                    else:
                        print("INGRESE UNA OPCIÓN CORRECTA")