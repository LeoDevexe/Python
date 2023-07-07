
altura = int(input("INTRODUZCA LA ALTURA--- : "))
ancho = int(input("INTRODUZCA EL ANCHO---: "))
dibujo = input("INGRESE UN SIMBOLO O LETRA ")
aste = ''
dibujo += ' '
if altura > 0 and ancho > 0:
    for i in range(0, altura):
        for j in range(0, ancho):
            if i == 0 or i == altura-1:
                aste += '* '
            else:
                if j == 0 or j == ancho-1:
                    aste += '* '
                else:
                    aste += dibujo
        aste += '\n'
    print(aste)
else:   
    print("LOS VALORES NO PUEDEN SER  0 O MENORES QUE 0")