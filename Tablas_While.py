num=0
rango=0
while rango<10:
    rango+=1
    print(num,"x",rango,"=",num*rango)
    if rango==10:
        num+=1
        rango=0
        print("************")
    if num>10 :break