
for i in range(0,21) : 
    resto =i%2
    if resto == 0 :
        if i ==0:
            print(" No está determinado el 0 como par ")
        else:
            print("\t PAR ",i)
    else:
        print("IMPAR",i,end=" ")