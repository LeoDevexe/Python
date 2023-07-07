alto = int(input(" INGRESE LA ALTURA "))
ancho = int(input(" INGRESE EL ANCHO "))
caracter = input(" INGRESE UN SIMBOLO O LETRA ")
if alto > 0 and alto > 0:
    for i in range(0, alto):
        for j in range(0, ancho):
            if j == 0 or j == ancho-1:
                print("* ", end="")
            else:
                if i == 0 or i == alto-1:
                    print("* ", end="")
                else:
                    print(caracter, end=" ")
        print("")
else:
    print("LOS VALORES NO PUEDEN SER  0 O MENORES QUE 0")
