num=int(input ("Ingrese el rango :"))
for i in range(0,num+1) : 
    resto =i%2
    if resto == 0 :
        if i ==0:
            print(" No está determinado el 0 como par ")
        else:
            print("El numero es par ",i)
    else:
        print("El numero es impar",i)

