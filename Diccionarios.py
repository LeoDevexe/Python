#Un diccionario es una colección de pares formados por una clave y un valor asociado a la clave.


a = {'nombre':'EDISON', 'carrera': 'SOFTWARE', 'email':'emeneses@emenesesdevelopers.com','año':1986}

# print("**********")
# print(a['nombre'])
# print(a['carrera'])
# print(a['email'])
# print(a['año'])

# print("**********")
# print(a.get('carrera'))
# print(a.get('universidad','ISUS'))



# print("**********")
# print(len(a))
# print(min(a))#Devuelve la minima clave de un diccionario siempre y cuando sean comparables
# print(a.keys())#Devuelve las claves de un diccionario
# print(a.values())#Devuelve los valores que toman cada clave de un diccionario
# print(a.items())#Devuele los pares de clave-valor de un diccionario

# print("**********")
# #operaciones
# a['universidad']='ISUS' #Agrega una clave-valor al diccionario
# print(a)

# a.pop('carrera') #Elimina la clave-valor del diccionario
# print(a)

# a.clear()#Elimina toda el contenido del diccionario

# print(a)
# for clave in a:
#     print(clave,":",a[clave],end=", ")

print(a)
for valor in a.values():
    print(valor,end=", ")