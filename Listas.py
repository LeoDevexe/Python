# list=[1,5,6,8,4,2,5,5,5,5,8]
# print(len(list))
# print(list)
# i=0
# while i<=len(list):
#     if 5 in list:
#         list.remove(5)
#     i+=1
# print(list)
# *******************************
# list=[1,5,6,8,4,2,5,5,5,5,8,4,3,2,7,8]
# print(len(list))
# print(list)
# i=0
# while i<=len(list):
#     if 5 in list:
#         list.remove(5)
#         print(list)
#     i+=1
# *******************************
# print("\n**** El elemento 5 de la lista ")
# my_list1 = [2,5,'ALARCON',7,'ALARCON','ALARCON',1.2]

# print(my_list1.index('ALARCON'))
# i=0
# while i <len(my_list1):
#     if my_list1[i]=="ALARCON":
#         print(i)
#     i+=1
# *************************
# lista=[1,"ALARCON","2","MOSQUERA","3",4,5.5]
# lista.reverse()
# print(lista)
# *************************
# listas=['A','L','A','R','C','O','N']
# tup=[]
# print(listas)
# rango=int(input("INGRESE HASTA DONDE DESEE VISUALIZAR "))
# if rango <=len(listas):
#     i=0
#     while i+1<=rango:
#         tup.append(*listas[i])
#         i+=1
#         print(tup)
#     else:
#         print('Fin del proceso')
# else:
#     print('Invalido')
#***************************
listas=['A','L','A','R','C','O','N']
tup=[]
print(listas)
rango=int(input("INGRESE HASTA DONDE DESEE VISUALIZAR "))
if rango <=len(listas):
    i=0
    while i+1<=rango:
        tup.append(listas[i])
        i+=1
    print(tup)
    print('Fin del proceso')
else:
    print('Invalido')