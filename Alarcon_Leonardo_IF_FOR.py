
# MENÚ DE OPERACIONES
print("MENÚ")
print("1. SUMA")
print("2. RESTA")
print("3. MULTIPLICACIÓN")
print("4. DIVISON")
print("5. POTENCIA")
opciones = input("INGRESE LA OPERACION QUE DESEA REALIZAR :")
if opciones == '1':
    print("Usted escogió SUMA ")
    for a in range(0, 11):
        print("TABLA DE SUMA DEL ", a)
        for b in range(0, 11):
            print(a, '+', b, '=', a+b)
else:
    if opciones == '2':
        print("Usted escogió RESTA")
        for c in range(0, 11):
            print("TABLA DE RESTA ", c)
            for d in range(0, 11):
                print(c, '-', d, '=', c-d)
    else:
        if opciones == '3':
            print("Usted escogió MULTIPLICACION",)
            for e in range(0, 11):
                print("TABLA DE MULTIPLICACIÓN ", e,"NOTA:TODO NUMERO MULTIPLICADO PARA 0 DA 0 ")
                for f in range(0, 11):
                    print(e, 'x', f, '=', e*f)
        else:
            if opciones == '4':
                print("Usted escogió DIVISION")            
                for g in range(0, 11):
                    print("TABLA DE DIVISION ", g,)
                    for h in range (0,11):
                        if h==0:
                            print(h,"/",g,"= "" NO EXISTE DIVISION PARA 0")
                        else : 
                            print(g,"/",h,"=",g/h)      
            else:   
                if opciones == '5':
                    print("NOTA:CUALQUIER NÚMERO DIFERENTE DE CERO ELEVADO A LA POTENCIA CERO ES IGUAL A UNO LE PRESENTAMOS LA TABLA")
                    print("Usted escogió POTENCIACIÓN")
                    for k in range(0, 11):
                        print("TABLA DE POTENCIA ", k)
                        for l in range(0, 11):
                            print(k, '^', l, '=', k**l)
                else:
                    print("INGRESE UNA OPCIÓN CORRECTA")
