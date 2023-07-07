num=int(input("INGRESE EL FINAL DEL RANGO "))
i=0
while i<=num:
    if i%2!=0:
        print("\t IMPAR",i)
        i+=1
    else:
        if i%2 == 0:
            print("PAR",i,end="")
            i+=1