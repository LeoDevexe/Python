#Ingrese un numero de cédula por teclado, y utilizando una función determinar si la cédula ingresada es valida o no si la longitud es igual a 10 escribirá "Su número de cédula xxxx es correcto", caso contrario escribirá "El número de cédula ingresado xxxx, es incorrecto ya que la longitud de ser igual a 10 y el ingresado tiene xx digitos"


def cedula (valor): #se crea la funcion
    cedula = input("Ingrese su numero de cedula: ")#En esta variable se ingresara los diguitos de la cedula del usuario
    print("Los Digitos de su cedula son: " ,cedula,end=" ")#se ejecutara al momento de invocar la funcion
    if len(cedula) == 10: #se va a validar los 10 diguitos
        print("Su numero de cedula es correcta")
    else:
        print("Numero de cedula incorrecto ,diguite numero de cedula valido")#Mensaje si el numero sobrepasa de los 10 diguitos
cedula(cedula)#se invoca la funcion
