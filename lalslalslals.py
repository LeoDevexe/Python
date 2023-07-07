dibujo=''
anchura=20
altura=20


for i in range(0,altura):


    for j in range(0,anchura):
        if i ==0 or i == altura-1:
            dibujo+='*'
        elif j ==0 or j==anchura-1:
            dibujo+='*'
        else:
            dibujo +='-'
    dibujo+='\n'



print ("\n"*2)
print (dibujo)