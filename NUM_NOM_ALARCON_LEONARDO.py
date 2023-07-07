rango = int(input("INGRESE EL NUMERO DEL RANGO DESEADO QUE SEA PAR  "))

par = rango % 2
if par == 0:
    if rango >= 0:
        for a in range (0,rango+1):
            mitad = rango/2
            if a < mitad:
                print(float(a), " LEONARDO ")
            else:
                if a > mitad:
                    print(float(a), " ALARCON ")
                else:
                    if a == mitad:
                        print(float(a), " ----ESTA ES LA MITAD DEL RANGO ----- ")
        if rango == 0:
            print(" EL 0 NO ESTA DETERMINADO COMO PAR ")
    else:
        for a in range(rango, 0+1):
            mitad = rango/2
            if a < mitad:
                print(float(a), " LEONARDO ")
            else:
                if a > mitad:
                    print(float(a), " ALARCON ")
                else:
                    if a == mitad:
                        print(float(a), " ----ESTA ES LA MITAD DEL RANGO ----- ")
else:
    print("INGRESE UN NUMERO PAR PORFAVOR ")
