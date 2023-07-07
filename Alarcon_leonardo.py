num1 = int(input("Ingrese el inicio "))
num2 = int(input("Ingrese el limite "))
b=num1
if num1 > num2 :
    print("EL NUMERO INICAL NO PUEDE SER MAYOR QUE EL LIMITE")
else:
    if num1 and num2 >= 0 :
        for a in range(num1,num2):
            print(a,"+",a+1, "=",a+a+1)
            b=b+a+1   
        print("LA SUMA ES :",b)
    else:
        print("ERROR EL INICIO Y EL FINAL NO DEBEN SER MENORES QUE 0")