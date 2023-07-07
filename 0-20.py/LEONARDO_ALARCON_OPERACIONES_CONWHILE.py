while True:
    print("MENÚ")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACIÓN")
    print("4. DIVISON")
    print("5. SALIR DEL MENÚ")
    op = int(input("INGRESE LA OPERACIÓN A REALIZAR  "))
    if op == 5:
        print("!! ADIOS - HAS SALIDO DEL MENÚ !! ")
        break
    if op !=1 and op !=2 and op !=3 and op !=4 and op !=5 :
        print("INGRESE UNA OPCIÓN CORRECTA PORFAVOR")
        print("")
    else:
        num = int(input("INGRESE UN NÚMERO INICIAL "))
        numfinal = int(input("INGRESE UN NÚMERO FINAL "))
        if op == 1:
            i = 0
            print("TABLA DEL ", num)
            while i <= numfinal:
                print(num, "+", i, "=", num+i)
                i += 1
        else:
            if op == 2:
                i = 0
                print("TABLA DEL ", num)
                while i <= numfinal:
                    print(num, "-", i, "=", num-i)
                    i += 1
            else:
                if op == 3:
                    i = 0
                    print("TABLA DEL ", num)
                    while i <= numfinal:
                        print(num, "x", i, "=", num*i)
                        i += 1
                else:
                    if op == 4:
                        i=0
                        print("TABLA DEL ", num)
                        print(num, "/", i, "="," NO EXISTE DIVISION ENTRE 0")
                        i+=1
                        while i <= numfinal :
                            print(num, "/", i, "=", num/i)
                            i+=1
