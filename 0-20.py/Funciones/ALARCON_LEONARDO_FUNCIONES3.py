
#FUNCIÓN PARA VALIDAR QUE EXISTEN  DÍGITOS EN EL INGRESO DE LA CÉDULA
def validar_cedula(longitud):
    longitud = input("INGRESE SU NÚMERO DE CÉDULA ")    #EL PARAMETRO LONGUITD TOMARÁ EL VALOR INGRESADO
    if len(longitud) == 10:                             #LA CONDICIÓN INDICA QUE SI LA LONGUITUD DEL PARAMETRO ES IGUAL A DIEZ ES CORRECTO
        print("Su número de cédula", longitud, "es correcto")
    else:
        if len(longitud)!= 10:      #LA CONDICIÓN INDICA QUE SI LA LONGITUD ES MENOR QUE 10 O MAYOR QUE 10 EL INGRESO ES INCORRECTO
            print("El número de cédula ingresado", longitud,"es incorrecto ya que la longitud de ser igual a 10 y el ingresado tiene", len(longitud), "digitos")


validar_cedula(longitud="")
