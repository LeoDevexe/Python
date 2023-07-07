print('***********1er EJERCICIO***********')
a = {'nombre':'LEONARDO','apellido':'ALARCON','universidad':'ISU SUCRE', 'carrera': 'SOFTWARE', 'email':'leonardoalar1819@outlook.com'}
print(a)
print("LONGITUD ORIGINAL: ")
print(len(a))
a['cedula']='1750496331'
a['edad']='21'
a['fecha de nacimiento']='29 de mayo'
print(a)
print("LONGITUD NUEVA: ")
print(len(a)) 
a.pop('apellido') 
print(a)
a = {'nombre':'LEONARDO','apellido':'ALARCON','universidad':'ISU SUCRE', 'carrera': 'SOFTWARE', 'email':'leonardoalar1819@outlook.com'}
print("EL VALOR MÍNIMO ORIGINAL DE a es: ")
print(min(a))
a['cedula']='1750496331'
a['edad']='21'
a['fecha de nacimiento']='29 de mayo'
a.pop('apellido') 
print("EL VALOR MÍNIMO NUEVO DE a es: ")
print(min(a))
a = {'nombre':'LEONARDO','apellido':'ALARCON','universidad':'ISU SUCRE', 'carrera': 'SOFTWARE', 'email':'leonardoalar1819@outlook.com'}
print("---ITEM 6---")
for clave in a:
    print(clave,":",a[clave],end=", ")
a['cedula']='1750496331'
a['edad']='21'
a['fecha de nacimiento']='29 de mayo'
a.pop('apellido') 
print()
for clave in a:
    print(clave,":",a[clave],end=", ")
###################################################################
# EJERCICIO 2
print()
print('***********2do EJERCICIO***********')
clothes={'Camiseta':20 ,'Jens':25 ,'Zapatos':80 }
subtotal=0
for i in clothes.values():
    subtotal+=i
iva=0.12*subtotal
total=iva+subtotal
print("SUBTOTAL : ",subtotal)
print("IVA : ",iva)
print("TOTAL : ",total)