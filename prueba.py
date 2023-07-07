altura=int (input(" INGRESE LA ALTURA "))
ancho=int (input(" INGRESE EL ANCHO "))
caracter=str(input(" INGRESE UN SIMBOLO O LETRA "))

for i in range(altura):
    if i % 2 == 0:
        print("*", " ")
    else:
        print(" ", " ")

print()
for j in range(ancho):
    for i in range(altura):
        if i == 0:
            print("*", end="")
        elif i == 18:
            print("*")
            break
        else:
            print(" ",end="")

for i in range(altura):
    if i % 2 == 0:
        print("*", end=" ")
    else:
        print(" ", end=" ")
        
        ancho=int(input("dame el ancho de tu figura"))
alto=int(input("dame el alto de tu figura"))

for i in range(0,alto):
    for j in range(0,ancho):
        if j==0 or j==ancho-1:
            print("*",end="")
        elif  (i==0 or i==alto-1):
            print("*",end="")
        else:
            print("-",end="")
    print("")