# HACER SISTEMA DETERMINE MAYOR DE EDAD O MENOR DE EDAD si pongo numero negativo print esta edad no existe y mayor de 100 años esta edad no existe
# LEONARDO ALARCON 3 "A"


print("Ingrese la edad ")
edad = int(input())
if edad <= 100:
    if edad >= 18:
        print("Usted es mayor de edad")
else:
    print("INGRESE UN NUMERO VALIDO")
if edad >= 0:
    if edad <= 17:
        print("Usted es menor de edad")
else:
    print("Ingrese un numero valido")
